#!/usr/bin/node

/* Import File System */
const fs = require('fs');

const filePath = process.argv[2];
const toWrite = process.argv[3];

fs.writeFile(filePath, toWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
