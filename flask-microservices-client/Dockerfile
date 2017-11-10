FROM node:latest

# set working directory
RUN mkdir /app
WORKDIR /app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# add environment variables
ARG REACT_APP_USERS_SERVICE_URL
ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
ENV REACT_APP_USERS_SERVICE_URL $REACT_APP_USERS_SERVICE_URL

# install and cache app dependencies
ADD package.json /app/package.json
RUN npm install --silent
RUN npm install pushstate-server -g --silent

# add app
ADD . /app

# build react app
RUN npm run build

# start app
CMD ["pushstate-server", "build"]