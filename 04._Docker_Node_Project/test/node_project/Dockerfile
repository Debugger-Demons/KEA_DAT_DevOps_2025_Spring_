.FROM node
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
# Install nodemon globally

RUN npm install -g nodemon

COPY . .

CMD npm config set prefer-offline true && nodemon app.js
