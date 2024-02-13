#!/usr/bin/node
// a script that prints x times “C is fun”
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const y = Number(process.argv[2]);
  let j = 0;
  while (j < y) {
    console.log('C is fun');
    j++;
  }
}
