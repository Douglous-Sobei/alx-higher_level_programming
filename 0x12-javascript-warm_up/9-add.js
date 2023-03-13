#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

let firstArg = process.argv[3];
let secondArg = process.argv[4];

firstArg = parseInt(firstArg);
secondArg = parseInt(secondArg);

add(firstArg, secondArg);
