FROM node:20-alpine

WORKDIR /app

COPY package.json .
RUN npm install --production

COPY main.js .

# Create non-root user for security
RUN adduser -D -s /bin/sh runner

EXPOSE 5000

CMD ["node", "main.js"]
