#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length <= 3) {
  console.log('0');
} else {
  argv.sort().reverse();
  console.log(argv[1]);
}
