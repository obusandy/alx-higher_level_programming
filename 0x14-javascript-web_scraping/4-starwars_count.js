#!/usr/bin/node
/**
 * Below is a script that prints the number
 * of movies where the character “Wedge Antilles” is present.
 * The first argument is the API URL of the Star wars API:
 * https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18
 */
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((intcount, movieitem) => {
      return movieitem.characters.find((character) => character.endsWith('/18/'))
        ? intcount + 1
        : intcount;
    }, 0));
  }
});
