#!/usr/bin/node

/* Import File System (fs) */
const fs = require('fs');

/* Where is the JSON coming from */
const filePath = process.argv[2];

/* Read the JSON and handle errors */
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  /* Print JSON */
  console.log(data);
});
