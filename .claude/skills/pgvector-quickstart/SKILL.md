---
name: pgvector-quickstart
description: Turn Postgres into a vector store with pgvector (what it is, when it beats a dedicated vector database, create the extension and a table, similarity search with the three distance operators, HNSW and IVFFlat indexes, filtered search for multi-tenant apps, production notes), with the filtered-search recall pitfall and iterative scans the source slides skip. Use when building RAG or semantic search on Postgres or Supabase.
---

# pgvector quickstart

Source: an eight-slide carousel by @panecci.solutions, "pgvector: turn Postgres into a vector database" (Batch 120). The SQL below was checked against the pgvector README (repo `pgvector/pgvector`, 23,483 stars on 26 October 2026, licence shown as "Other", which is the PostgreSQL licence). The slides stop short on filtered search; that section is added from the README.

## 1 What it is
An open-source extension for PostgreSQL: a `vector` column type and nearest-neighbour search in SQL. No new database to run. On Supabase it is enabled with one click.

## 2 Why not a dedicated vector database
The slide's argument: one database (relational and vector together), real SQL joins and filters, ACID transactions, no extra bill, one backup. Its rule of thumb is to reach for a dedicated vector database at tens of millions of vectors. [Guessing] That threshold depends on dimensions, recall target, latency and hardware; benchmark on your own data before you choose either way.

## 3 Setup
```sql
CREATE EXTENSION vector;
CREATE TABLE docs (
  id bigserial PRIMARY KEY,
  content text,
  embedding vector(1536)
);
```
The dimension must match your embedding model's output exactly, or inserts fail (1536 matches some OpenAI embedding models; check yours).

## 4 Search
```sql
SELECT content FROM docs ORDER BY embedding <=> $1 LIMIT 5;
```
Distance operators: `<->` Euclidean (L2), `<=>` cosine distance, `<#>` negative inner product. `$1` is your question, embedded with the same model; the nearest rows become context for the language model.

## 5 Index
Without an index every query scans every row. Add one once you have real data.
```sql
CREATE INDEX ON docs USING hnsw (embedding vector_cosine_ops);
```
HNSW is the usual pick (fast, accurate). IVFFlat is smaller but needs data present to build. Match the operator class to your distance operator: cosine index for `<=>` queries (`vector_l2_ops` for `<->`, `vector_ip_ops` for `<#>`).

## 6 Filter while you search (and the pitfall)
```sql
SELECT content FROM docs WHERE tenant_id = $2 ORDER BY embedding <=> $1 LIMIT 5;
```
This is easy in Postgres and useful for multi-tenant apps. **Pitfall the slide omits:** [Certain] with approximate indexes, the filter is applied after the index is scanned, so a filtered query can return fewer than LIMIT rows. Since pgvector 0.8.0 you can enable iterative scans so the index scan continues until enough rows pass the filter:
```sql
SET hnsw.iterative_scan = strict_order;   -- or relaxed_order for better recall
SET hnsw.max_scan_tuples = 20000;         -- the default cap
```
For an IVFFlat index use `ivfflat.iterative_scan` and `ivfflat.max_probes`. For hard tenant isolation do not rely on a WHERE clause alone: add row-level security, and consider a partial index per large tenant or partitioning.

## 7 Production notes (from the slide, with additions)
- **Match dimensions**: the table's vector size equals the model's output size.
- **Normalise vectors**: with unit-length vectors, cosine and inner product give the same ranking.
- **Index after loading**: build the index once the data is in; rebuilding on a loaded table is faster than inserting into an empty indexed one.
- **Store the text** beside the embedding so you can hand it to the model.
- **Re-embed on change**: stale vectors return stale results; also re-embed everything if you change the model (vectors from different models are not comparable).
- **Tune the speed and recall trade-off**: `hnsw.ef_search` raises recall at the cost of latency per query.
- (Added) Measure recall against exact search on a sample before you trust an index, and monitor index size and build time.
- (Added) Embeddings can leak information about the text; apply the same access control as the source rows.

## Related
`similarity-search-patterns`, `vector-index-tuning`, `embedding-strategies`, `hybrid-search-implementation`, `rag-implementation`, `rag-pipeline-architecture`, `postgresql-table-design`, `postgres-patterns`, `vector-database-engineer` (agent).
