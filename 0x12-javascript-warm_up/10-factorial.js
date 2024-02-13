#!/usr/bin/node
// script that computes and prints a factorial
// Factorial of NaN is 1

function factorial (i) {
  return i === 0 || isNaN(i) ? 1 : i * factorial(i - 1);
}
console.log(factorial(Number(process.argv[2])));
