#!/usr/bin/node
// prints the addition of 2 integers
// first argument is the first integer
// second argument is the second integer
function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
