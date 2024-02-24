#!/usr/bin/node
// script that searches the second biggest integer in the list of args.
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const secnd = arr.sort(function (i, j) { return j - i; })[1];
  console.log(secnd);
}
