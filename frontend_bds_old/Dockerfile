FROM node:18-alpine AS builder

WORKDIR /app

# Cài dependencies
COPY package*.json ./
RUN npm install

# Copy toàn bộ source
COPY . .

# Build Next.js
RUN npm run build

# Stage 2: chạy Next.js
FROM node:18-alpine

WORKDIR /app

# Copy code đã build từ stage 1
COPY --from=builder /app ./

EXPOSE 3000

CMD ["npm", "run", "start"]
