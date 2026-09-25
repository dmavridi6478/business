# 5 Trading Power GitHub Repos

Source: @theromanknox (skool.com/knox)

---

## 1. pmxt-dev/pmxt — Unified Prediction Markets API
One API for Polymarket, Kalshi, and Limitless. CCXT-style patterns — zero learning curve for algo traders.
```
pip install pmxt
```
★1.3k | Python | MIT

---

## 2. caiovicentino/polymarket-mcp-server — Claude × Polymarket Trading
45-tool MCP server linking Claude Desktop to live Polymarket trading with built-in safety rails.
- Demo mode needs no wallet
- Hard limits on order size and exposure
- Real-time WebSocket monitoring
```
pip install -e . && ./install.sh --demo
```
★206 | Python | MIT

---

## 3. Polymarket/agents — AI Trading Agents Framework
Official Polymarket framework for autonomous, LLM-powered trading agents. Uses LLMs, RAG, superforecasting.
- Modular architecture — swap any LLM without rewriting core logic
- Full CLI from setup to live autonomous trading in one session
```
pip install poetry && poetry install
```
★2.3k | Python | MIT

---

## 4. PrefectHQ/fastmcp — MCP Server Framework
The fast, Pythonic way to build MCP servers. Powers 70% of all MCP servers.
- Decorate a Python function with @mcp.tool → instant MCP tool
- Supports filesystem, OpenAPI, proxy providers
- Built-in OAuth and JWT auth
```
pip install fastmcp
```
★24.2k | Python | MIT

---

## 5. txbabaxyz/polyrec — BTC Terminal Dashboard
Real-time terminal dashboard aggregating Chainlink, Binance, and Polymarket data for BTC markets.
- Aggregates 70+ technical indicators with live orderbook depth
- Auto-logs all price and orderbook data to CSV for backtesting
- Built-in backtesting scripts for balance replication and impulse fade
```
pip install -r requirements.txt && python dash.py
```
★89 | Python | MIT
