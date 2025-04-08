# Development stage
FROM node:18-alpine AS development

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install --include=dev
COPY frontend .

EXPOSE 5173
CMD ["npm", "run", "dev"]

# Production stage
FROM node:18-alpine AS production

WORKDIR /app
# Install only production dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install --omit=dev

# Copy source code and build the app
COPY frontend .
RUN npm run build

# Install a simple static file server
RUN npm install -g serve

# Serve the production build on port 3000
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]