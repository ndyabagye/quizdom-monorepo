# Development stage
FROM node:18-alpine as development

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install --include=dev
COPY frontend .

EXPOSE 5173
CMD ["npm", "run", "dev"]

# Production stage
FROM node:18-alpine as production

WORKDIR /app
COPY --from=development /app .
RUN npm run build && \
    npm install -g serve

EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]