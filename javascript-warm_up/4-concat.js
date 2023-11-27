#!/usr/bin/node

let argv2 = process.argv[2]
let argv3 = process.argv[3]

if (argv2 == null) {
  argv2 == 'undefined'
}
if (argv3 == null) {
  argv3 == 'undefined'
}

console.log(argv2 + ' is ' + argv3)