# 构建阶段
FROM node:18-alpine as build-stage

WORKDIR /app
COPY . .
RUN npm install
RUN rm -rf dist && npm run build

# 生产阶段：用 nginx 托管静态文件
FROM nginx:alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ../nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
