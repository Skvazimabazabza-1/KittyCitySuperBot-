#!/bin/bash

echo "🐱 Starting Kitty City Bot..."
echo "📅 $(date)"
echo "🐍 Python version: $(python --version)"
echo "📦 Installing dependencies..."

# Установка зависимостей
pip install -r requirements.txt

echo "🔧 Starting bot..."
python main.py

echo "❌ Bot stopped unexpectedly"
echo "🔄 Restarting in 5 seconds..."
sleep 5
exec bash start.sh