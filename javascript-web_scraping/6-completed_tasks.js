#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dictionary = {};

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const dataPull = JSON.parse(body);
    for (let x = 0; x < dataPull.length; x++) {
      /* Pulls tasks that are completed */
      if (dataPull[x].completed === true) {
        /* Is the user listed yet? */
        if (dataPull[x].userId in dictionary) {
          /* If yes, generate next ID */
          dictionary[dataPull[x].userId] += 1;
        } else {
          /* If no, first ID is 1 */
          dictionary[dataPull[x].userId] = 1;
        }
      }
    }
    console.log(dictionary);
  }
});
