"use-strict";



// var url = 'https://gnews.io/api/v4/search?q="health"&max=3&fomr=2020-11-01&token=967e4812b21a443c693f7ef5e41bc139';

// fetch('https://gnews.io/api/v4/search?q="health"&max=3&fomr=2020-11-01&token=967e4812b21a443c693f7ef5e41bc139')
//     .then(function (response) {
//         return response.json();
//     })
//     .then(function (data) {
//         console.log(data);
//     });

// for each article[a], i need to create a col-md-4 div and append all of the info to the div
for (var i = 0; i < 3; i++) {
// creating 3 new columns with incrementing id's
    $('.row').append($('<div/>', { id: 'col' + i, 'class' : 'col-md-4'}))
// append a set of info into each col[j]
}

for (var j = 0; j < 3; j++) {
    // $('.col-md-4').append(j)
// for each col-md-4, I want to append this whole set for each i
    $('#col' + j).append("<br><strong>link</strong>" + j);
    $('#col' + j).append("<br>Title");
    $('#col' + j).append("<br>Published");
    $('#col' + j).append("<br>image");
        // $('.col-md-4').append(j)


// $.get(url, function( data ) {
    //display only the first 3 news items
    // for (var j = 0; j < 1; j++)
    // {
    //     $('.col-md-4').append(j)
    
    // for (var i = 0; i < 3; i++) {
    //     for (var j = 0; j < 3; j++) {
    //         $('.col-md-4').append(j)
    // // for each col-md-4, I want to append this whole set for each i
    //         $('.col-md-4').append("liafdgdfgshdrgthsghsfghfshfdhdnkkkkkkkkkkkkkkkkkkkkkkkkkkkkk");
    //         $('.col-md-4').append("Title");
    //         $('.col-md-4').append("Published");
    //         $('.col-md-4').append("image");
            
    
            // $('.col-md-4').append(`<br><a href="${data.articles[i]['url']}">${data.articles[i]['description']}</a>`);
            // $('.col-md-4').append(`<br>Title: ${data.articles[i]['title']}`);
            // $('.col-md-4').append(`<br>Published At: ${data.articles[i]['publishedAt']}`);
            // $('.col-md-4').append(`<br>Author: ${data.articles[i]['author']}`);
            // $('.col-md-4').append(`<br><img src="${data.articles[i]['image']}">`);

    
        // for (var j = 0; j < 1; j++)
        
            // $('.col-md-4').append(j)
        }
    // }

    
// })
