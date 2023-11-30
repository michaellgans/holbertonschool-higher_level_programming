#!/usr/bin/node

const argv2 = process.argv[2];

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}

for (let x = 0; x < argv2; x++) {
  console.log('C is fun');
}
