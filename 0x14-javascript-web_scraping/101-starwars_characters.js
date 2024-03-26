#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line in the same order of the list “characters” in the /films/ response
 * using the Star wars API
 */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const cs = JSON.parse(body).cs;
    printCharacters(cs, 0);
  }
});

function printCharacters (cs, index) {
  request(cs[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < cs.length) {
        printCharacters(cs, index + 1);
      }
    }
  });
}
