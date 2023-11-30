#!/usr/bin/node

const argv2 = process.argv[2];
const args = process.argv.slice(2);

if (!argv2 || argv2 === 1) {
  console.log('0');
} else {
  let lastArg = 0;
  let secondToLast = 0;
  args.sort((a, b) => a - b);
  lastArg = Number(args.length);
  secondToLast = lastArg - 2;
  console.log(args[secondToLast]);
}
