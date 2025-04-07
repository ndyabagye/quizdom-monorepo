# Development stage
FROM node:18-alpine as development

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend .

# Explicitly run build for production files
RUN if [ "$ENVIRONMENT" = "production" ]; then \
	npm run build; \
	fi

EXPOSE 5173

CMD if [ "$ENVIRONMENT" = "production" ]; then \
	npm install -g serve && serve -s build -l 5173; \
	else \
	npm run dev; \
	fi

# Production stage
FROM node:18-alpine as production

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install --production

COPY --from=development /app/build ./build

EXPOSE 5173

# Install serve and run the app
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "5173"]