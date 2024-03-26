#!/usr/bin/node
/**
 * Below is a script that gets the contents of a webpage and stores it in a file.
 * Arguments:
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 */
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
