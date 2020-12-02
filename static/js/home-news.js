// "use-strict";



// var url = 'https://gnews.io/api/v4/search?q="health"&max=3&fomr=2020-11-01&token=967e4812b21a443c693f7ef5e41bc139';

// fetch('https://gnews.io/api/v4/search?q="health"&max=3&fomr=2020-11-01&token=967e4812b21a443c693f7ef5e41bc139')
//     .then(function (response) {
//         return response.json();
//     })
//     .then(function (data) {
//         console.log(data);
//     });

// // for each article[a], i need to create a col-md-4 div and append all of the info to the div
// // for (var i = 0; i < 3; i++) {
// // // creating 3 new columns with incrementing id's
// //     $('.row').append($('<div/>', { id: 'col' + i, 'class' : 'col-md-4'}))
// // // append a set of info into each col[j]
// // }

// // for (var j = 0; j < 3; j++) {
// //     // $('.col-md-4').append(j)
// // // for each col-md-4, I want to append this whole set for each i
// //     $('#col' + j).append("<br><strong>link</strong>" + j);
// //     $('#col' + j).append("<br>Title");
// //     $('#col' + j).append("<br>Published");
// //     $('#col' + j).append("<br>image");



// $.get(url, function( data ) {
//     // display only the first 3 news items

//     for (var i = 0; i < 3; i++) {
//         $('.row').append($('<div/>', { id: 'col' + i, 'class' : 'col-md-4 card', 'style' : 'width: 18rem;'}))
//     }

//     for (var j = 0; j < 3; j++) {

//         $('#col' + j).append(`<br><a href="${data.articles[j]['url']}" class="btn btn-primary">${data.articles[j]['title']}</a>`);
//         $('#col' + j).append(`<br>${data.articles[j]['description']}`);
//         // $('#col' + j).append(`<br>Published At: ${data.articles[j]['publishedAt']}`);
//         // $('#col' + j).append(`<br>Author: ${data.articles[j]['author']}`);
//         $('#col' + j).append(`<br><img class="card-img-bottom" src="${data.articles[j]['image']}">`);


//     }

    
});
