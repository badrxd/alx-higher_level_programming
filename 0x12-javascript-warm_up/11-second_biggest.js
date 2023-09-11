#!/usr/bin/node
const argv = process.argv;
const biger = [];
if (argv.length <= 3) {
  console.log('0');
} else {
  for (let i = 2; i < argv.length; i++) {
    biger[i - 2] = Number(argv[i]);
  }
  biger.sort();
  console.log(biger[biger.length - 2]);
}
