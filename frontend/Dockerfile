# frontend/Dockerfile
FROM node:20

WORKDIR /frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend .

RUN npm run build

# Optional: use a simple static file server
RUN npm install -g serve

EXPOSE 5173
CMD ["serve", "-s", "dist", "-l", "5173"]

