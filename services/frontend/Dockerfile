FROM node:latest

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .
COPY yarn.lock ./
RUN yarn add @vue/cli-service --dev
RUN yarn install --frozen-lockfile
RUN yarn add @vue/cli-service --dev

COPY . .
EXPOSE 8080

CMD ["yarn", "serve", "--watch"]