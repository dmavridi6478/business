#!/usr/bin/env bash
# Run this on YOUR machine (not Claude Code remote) to stand up all self-hosted services.
# Prerequisites: git, docker, docker compose, python3/pip

set -e
REPOS_DIR="$HOME/repos"
mkdir -p "$REPOS_DIR"
cd "$REPOS_DIR"

echo "=== Cloning repos ==="
repos=(
  "dani-garcia/vaultwarden"
  "brightbeanxyz/brightbean-studio"
  "every-app/open-seo"
  "bagisto/bagisto"
  "browser-use/browser-use"
  "topoteretes/cognee"
  "openclaw/openclaw"
  "n8n-io/n8n"
  "kestra-io/kestra"
  "node-red/node-red"
  "windmill-labs/windmill"
  "NousResearch/hermes-agent"
)
for r in "${repos[@]}"; do
  name="${r##*/}"
  if [ ! -d "$name" ]; then
    git clone --depth 1 "https://github.com/$r" "$name"
  else
    echo "$name already cloned"
  fi
done

# ----------------------------------------------------------------
# 1. VAULTWARDEN — password manager (bitwarden-compatible)
# ----------------------------------------------------------------
echo ""
echo "=== Starting Vaultwarden (port 8880) ==="
mkdir -p "$HOME/vaultwarden-data"
docker run -d \
  --name vaultwarden \
  -v "$HOME/vaultwarden-data:/data/" \
  -p 8880:80 \
  --restart unless-stopped \
  vaultwarden/server:latest
echo "   -> http://localhost:8880"

# ----------------------------------------------------------------
# 2. BRIGHTBEAN STUDIO — social media scheduler
# ----------------------------------------------------------------
echo ""
echo "=== Setting up Brightbean Studio (port 8000) ==="
cd "$REPOS_DIR/brightbean-studio"
if [ ! -f .env ]; then
  cp .env.example .env
  SECRET_KEY=$(openssl rand -hex 32)
  ENC_SALT=$(openssl rand -hex 16)
  sed -i "s|SECRET_KEY=change-me-to-a-random-string|SECRET_KEY=$SECRET_KEY|" .env
  sed -i "s|ENCRYPTION_KEY_SALT=change-me-to-a-random-string|ENCRYPTION_KEY_SALT=$ENC_SALT|" .env
  sed -i "s|DATABASE_URL=postgres://postgres:postgres@localhost:5432/brightbean|DATABASE_URL=postgres://postgres:postgres@postgres:5432/brightbean|" .env
  echo "   .env created (SECRET_KEY and ENCRYPTION_KEY_SALT auto-generated)"
fi
docker compose up -d
echo "   -> http://localhost:8000"

# ----------------------------------------------------------------
# 3. OPEN-SEO — SEO analytics dashboard
# ----------------------------------------------------------------
echo ""
echo "=== Setting up Open-SEO (port 3001) ==="
cd "$REPOS_DIR/open-seo"
if [ ! -f .env ]; then
  cp .env.example .env
  echo "AUTH_MODE=local_noauth" >> .env
  echo "DATAFORSEO_API_KEY=" >> .env
  echo "   .env created (no API key — add DATAFORSEO_API_KEY= to enable SEO data)"
fi
docker compose up -d
echo "   -> http://localhost:3001"

# ----------------------------------------------------------------
# 4. BAGISTO — e-commerce platform
# ----------------------------------------------------------------
echo ""
echo "=== Setting up Bagisto (port 8080) ==="
cd "$REPOS_DIR/bagisto"
if [ ! -f .env ]; then
  cp .env.example .env
  sed -i "s|DB_HOST=127.0.0.1|DB_HOST=mysql|" .env
  sed -i "s|DB_DATABASE=|DB_DATABASE=bagisto|" .env
  sed -i "s|DB_USERNAME=|DB_USERNAME=bagisto|" .env
  sed -i "s|DB_PASSWORD=|DB_PASSWORD=bagisto|" .env
  APP_KEY="base64:$(openssl rand -base64 32 | tr -d '\n')"
  sed -i "s|APP_KEY=|APP_KEY=$APP_KEY|" .env
  sed -i "s|APP_URL=http://localhost|APP_URL=http://localhost:8080|" .env
  # Patch mysql service vars to match our .env values
  sed -i "s|MYSQL_DATABASE: '\${DB_DATABASE}'|MYSQL_DATABASE: 'bagisto'|" docker-compose.yml
  sed -i "s|MYSQL_USER: '\${DB_USERNAME}'|MYSQL_USER: 'bagisto'|" docker-compose.yml
  sed -i "s|MYSQL_PASSWORD: '\${DB_PASSWORD}'|MYSQL_PASSWORD: 'bagisto'|" docker-compose.yml
  sed -i "s|MYSQL_ROOT_PASSWORD: '\${DB_PASSWORD}'|MYSQL_ROOT_PASSWORD: 'bagisto'|" docker-compose.yml
fi
docker compose up -d
echo "   -> http://localhost:8080"

# ----------------------------------------------------------------
# 5. BROWSER-USE — AI browser automation
# ----------------------------------------------------------------
echo ""
echo "=== Installing browser-use (pip) ==="
pip install browser-use
echo "   -> python3 -c 'from browser_use import Agent'"

# ----------------------------------------------------------------
# 6. COGNEE — AI knowledge graph / second brain
# ----------------------------------------------------------------
echo ""
echo "=== Installing cognee (pip) ==="
pip install cognee
echo "   -> python3 -c 'import cognee'"

# ----------------------------------------------------------------
# 7. OPENCLAW — self-hosted persistent AI agent
# ----------------------------------------------------------------
echo ""
echo "=== Setting up OpenClaw (ports 18789/18790) ==="
cd "$REPOS_DIR/openclaw"
if [ ! -f .env ]; then
  cp .env.example .env
  GW_TOKEN=$(openssl rand -hex 32)
  sed -i "s|OPENCLAW_GATEWAY_TOKEN=|OPENCLAW_GATEWAY_TOKEN=$GW_TOKEN|" .env
  echo "   .env created (OPENCLAW_GATEWAY_TOKEN auto-generated)"
fi
docker compose up -d
echo "   -> http://localhost:18789 (gateway)"

# ----------------------------------------------------------------
# 8. N8N — visual AI automation workflows
# ----------------------------------------------------------------
echo ""
echo "=== Starting n8n (port 5678) ==="
mkdir -p "$HOME/.n8n"
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v "$HOME/.n8n:/home/node/.n8n" \
  --restart unless-stopped \
  docker.io/n8nio/n8n
echo "   -> http://localhost:5678"

# ----------------------------------------------------------------
# 9. KESTRA — complex AI orchestration / data pipelines
# ----------------------------------------------------------------
echo ""
echo "=== Starting Kestra (port 8085) ==="
docker run -d \
  --name kestra \
  --pull=always \
  -p 8085:8080 \
  --restart unless-stopped \
  kestra/kestra:latest server local
echo "   -> http://localhost:8085"

# ----------------------------------------------------------------
# 10. NODE-RED — visual flows connecting AI to infrastructure
# ----------------------------------------------------------------
echo ""
echo "=== Starting Node-RED (port 1880) ==="
mkdir -p "$HOME/.node-red"
docker run -d \
  --name node-red \
  -p 1880:1880 \
  -v "$HOME/.node-red:/data" \
  --restart unless-stopped \
  nodered/node-red
echo "   -> http://localhost:1880"

# ----------------------------------------------------------------
# 11. WINDMILL — developer-heavy automation + AI agents
# ----------------------------------------------------------------
echo ""
echo "=== Setting up Windmill (port 8090) ==="
cd "$REPOS_DIR/windmill"
# Remap port 80 -> 8090 to avoid conflicts
sed -i 's/- 80:80/- 8090:80/' docker-compose.yml
docker compose up -d
echo "   -> http://localhost:8090"

# ----------------------------------------------------------------
# 12. HERMES AGENT — AI agent with persistent memory (Nous Research)
# ----------------------------------------------------------------
echo ""
echo "=== Installing Hermes Agent (uv / pip) ==="
cd "$REPOS_DIR/hermes-agent"
if command -v uv &>/dev/null; then
  uv pip install -e ".[all]"
else
  pip install -e ".[all]"
fi
echo "   -> python3 -c 'from agent import HermesAgent'"

echo ""
echo "============================================"
echo "All services started. Endpoints:"
echo "  Vaultwarden (passwords):   http://localhost:8880"
echo "  Brightbean Studio (social):http://localhost:8000"
echo "  Open-SEO:                  http://localhost:3001"
echo "  Bagisto (e-commerce):      http://localhost:8080"
echo "  OpenClaw (AI agent):       http://localhost:18789"
echo "  n8n (automation):          http://localhost:5678"
echo "  Kestra (orchestration):    http://localhost:8085"
echo "  Node-RED (visual flows):   http://localhost:1880"
echo "  Windmill (dev automation): http://localhost:8090"
echo ""
echo "Optional API keys to add in .env files:"
echo "  open-seo:   DATAFORSEO_API_KEY= (for SEO data)"
echo "  brightbean: PLATFORM_*_APP_ID/SECRET (social logins)"
echo "  n8n:        Add AI credentials inside n8n UI"
echo "  openclaw:   Edit ~/.openclaw/openclaw.json to add LLM API key"
echo "============================================"
