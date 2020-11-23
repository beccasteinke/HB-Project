"use-strict";

var url = 'http://newsapi.org/v2/everything?' +
          'q=Health&' +
          'from=2020-11-01&' +
          'sortBy=popularity&' +
          'apiKey=d6f70533f3c5412583e8af7a54430e6e';


$.get(url, function( data ) {
    //display only the first 3 news items
    for (var i=0; i<3; i++)
    {
      $('#newsResults').append(`<br>Author: ${data.articles[i]['author']}`);
      $('#newsResults').append(`<br>Published At: ${data.articles[i]['publishedAt']}`);
      $('#newsResults').append(`<br>Title: ${data.articles[i]['title']}`);
      $('#newsResults').append(`<br><a href="${data.articles[i]['url']}">${data.articles[i]['description']}</a>`);
      $('#newsResults').append(`<br><img src="${data.articles[i]['urlToImage']}">`);
    }
})

var req = new Request(url);

fetch(req)
    .then(function(response) {
        console.log(response.json());
    })