#!/bin/bash

echo "=== CHECKING BACKEND PYTHON ==="
cd backend
python3 -m py_compile $(find . -name "*.py")

echo "=== CHECKING BACKEND DEPENDENCIES ==="
pip install -r requirements.txt --dry-run

echo "=== CHECKING FRONTEND ==="
cd ../frontend
npm install --dry-run
npm run lint

echo "=== CHECKING DOCKER ==="
cd ..
docker compose config

echo "=== FULL BUILD TEST ==="
docker compose build

echo "=== ALL CHECKS COMPLETED ==="
