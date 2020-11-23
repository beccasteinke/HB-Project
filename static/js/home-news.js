"use-strict";



var url = 'https://gnews.io/api/v4/search?q="health"&max=3&fomr=2020-11-01&token=967e4812b21a443c693f7ef5e41bc139';

fetch('https://gnews.io/api/v4/search?q="health"&max=3&fomr=2020-11-01&token=967e4812b21a443c693f7ef5e41bc139')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        console.log(data);
    });


$.get(url, function( data ) {
    //display only the first 3 news items
    for (var i=0; i<3; i++)
    {
        $('#newsResults').append(`<br><a href="${data.articles[i]['url']}">${data.articles[i]['description']}</a>`);
        $('#newsResults').append(`<br>Title: ${data.articles[i]['title']}`);
        $('#newsResults').append(`<br>Published At: ${data.articles[i]['publishedAt']}`);
        // $('#newsResults').append(`<br>Author: ${data.articles[i]['author']}`);
        $('#newsResults').append(`<br><img src="${data.articles[i]['image']}">`);
        
    }
})
