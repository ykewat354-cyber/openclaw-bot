#!/bin/bash
# OpenClaw-Bot Professional Installer
set -e
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🚀 Deploying OpenClaw-Bot Elite...${NC}"

# System Deps
apt-get update && apt-get install -y curl git python3 python3-pip

# UV Setup
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

INSTALL_DIR="$HOME/.openclaw-bot"
mkdir -p $INSTALL_DIR
cd $INSTALL_DIR

# Clone the PRO repo
git clone https://github.com/ykewat354-cyber/openclaw-bot.git .

# Python Env
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Wizard
echo -e "${GREEN}🧙‍♂️ Setup Wizard${NC}"
read -p "Enter Gemini API Key: " GEMINI_KEY
read -p "Enter Telegram Bot Token: " BOT_TOKEN

cat <<EOF > .env
GEMINI_API_KEY=$GEMINI_KEY
TELEGRAM_BOT_TOKEN=$BOT_TOKEN
EOF

# Launch
nohup .venv/bin/python3 src/telegram_gateway.py > bot.log 2>&1 &

echo -e "${GREEN}✅ OpenClaw-Bot is now LIVE and Immortal!${NC}"
