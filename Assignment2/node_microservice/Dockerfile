FROM node:boron
ADD . /node
WORKDIR /node
RUN npm install
RUN npm install amqplib
EXPOSE 3000 15762
CMD ["npm", "start"]
