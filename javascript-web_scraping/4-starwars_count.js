#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, body) {
  if (err) throw err;

    /* Changes JSON data to a JS Object */
    /* Results opens up the arrays */
    const dataPull = JSON.parse(body).results;
    let count = 0;

    for (let x = 0; x < dataPull.length; x++) {
      const dataPull2 = dataPull[x].characters;

      for (let y = 0; y < dataPull2.length; y++) {
        if (dataPull2[y].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
});
