#!/usr/bin/node

const argv2 = Number(process.argv[2]);

if (!isNaN(argv2)) {
  console.log('My number: ' + Math.floor(argv2));
} else if (process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('Not a number');
}
