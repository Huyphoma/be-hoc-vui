#!/bin/bash
echo "=== BH2 RESTART SCRIPT ==="

cd /root/project || exit

echo "1) Dừng containers..."
docker compose down

echo "2) Xóa container cũ còn sót..."
docker rm -f behocvui-backend >/dev/null 2>&1
docker rm -f behocvui-frontend >/dev/null 2>&1

echo "3) Kiểm tra port 8000..."
PID=$(lsof -t -i:8000)
if [ ! -z "$PID" ]; then
    echo " - Port 8000 đang bị chiếm, kill PID: $PID"
    kill -9 $PID
else
    echo " - Port 8000 OK, không bị chiếm."
fi

echo "4) Khởi động lại docker compose..."
docker compose up -d --build

echo "5) Hiển thị trạng thái..."
docker ps | grep behocvui

echo "6) Xem log backend..."
docker logs -f behocvui-backend
