# Development stage
FROM node:18-alpine as development

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 5173

# Use conditional command based on environment variable
CMD if ["$ENVIRONMENT" = "production"]; then \
	npm run build && npm install -g serve && serve -s build -l 5173; \
	else \
	npm run dev; \
	fi

# Production stage
FROM node:18-alpine as production

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install --production

COPY --from=development /app/build ./build

EXPOSE 5173

# Install serve and run the app
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "5173"]