#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const idNum = process.argv[2];

request.get(url + idNum, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    /* Changes JSON data to a JS Object */
    const dataPull = JSON.parse(body);
    console.log(dataPull.title);
  }
});
