ARG NODE_VERSION=20
FROM node:${NODE_VERSION}

ARG PYTHON_VERSION=3.11
RUN apt-get update && apt-get install -y \
  python${PYTHON_VERSION} \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/home/node/.cache \
  --mount=type=cache,target=/home/node/.npm \
  npm install
COPY . .

CMD ["npm", "start"]
