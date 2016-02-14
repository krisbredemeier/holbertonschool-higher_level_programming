var https = require ('https');

var options = {
  hostname: 'api.github.com',
  path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
  headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token 76cee11a2bc92e62615194f891ae4c0cd60cc9ab'
  }
};
const chunks = [];
var req = https.get(options, function(res) {
  res.on('data', (chunk) => {
     chunks.push(chunk);
   });
  res.on('end', () => {
    var jsonString = chunks.join('');
      var fs = require('fs');
  fs.writeFile("/tmp/34", jsonString, function(err) {
    if(err) {
      return console.log(err);
    }
    console.log("The file was saved!");
});


  });
});
