#!/usr/bin/node
let x = process.argv[2];
if (!x || isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  x = parseInt(x);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
