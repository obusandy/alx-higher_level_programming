#!/usr/bin/node
const area = Math.floor(Number(process.argv[2]));
if (isNaN(area)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < area; j++) {
    let line = '';
    for (let s = 0; s < area; s++) line += 'X';
    console.log(line);
  }
}
