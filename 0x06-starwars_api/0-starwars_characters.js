#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharactersName(characters, 0);
  }
});

function printCharactersName (characters, index) {
  request(characters[index], function (error, response, body) {
    if (error === null) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharactersName(characters, index + 1);
      }
    }
  });
}
