#!/usr/bin/node
const request = require('request');

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body);
      const characters = data.characters;
      characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          } else {
            console.error('Failed to retrieve character data:', error);
          }
        });
      });
    } else {
      console.error('Failed to retrieve movie data:', error);
    }
  });
}

// Retrieve movie ID from command line arguments
const movieId = process.argv[2];

if (movieId) {
  getMovieCharacters(movieId);
} else {
  console.log('Please provide a movie ID as a command-line argument.');
}
