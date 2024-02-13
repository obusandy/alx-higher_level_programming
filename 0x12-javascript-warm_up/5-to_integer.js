#!/usr/bin/node
// a script that prints My number:
// <first argument converted in integer>
const digit = Math.floor(Number(process.argv[2]));
console.log(isNaN(digit) ? 'Not a number' : `My number: ${digit}`);
