#!/usr/bin/node
let initialArg = process.argv[2];
if (!initialArg || isNaN(initialArg)) {
  console.log('Not a number');
} else {
  initialArg = parseInt(initialArg);
  console.log('My number: ' + initialArg);
}
