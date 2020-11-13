"use strict";

// const addFaveToProfile = (fave) => {
//     $('#user-faves').append(`
//         <tr>
//             <td>${fave}</td>
//         </tr>
//         `);
// };

// $('#add-faves').on('click', (fave) => {
//     addFaveToProfile(`${fave}`);
// });


// $.get('/route from which ajax is getting data', (data its receiving) => {
//     $('#thingyouwanttodosomethingto').text(data its receiving);


// })
$('button.fave-btn').on('click', (evt) => {
    const button = $(evt.target);
    const buttonId = button.attr('id'); // the button is now the bus_id
    // alert("heloo")
    $.get('/directory', (data) => {
        // $('#user-faves').append(bus_id);
        alert(data);

// on click, add bus_id(buttonId) to userbus table associated with user_id
})});



// getting button by the class fave-btn, then getting it by the id
// because for each id, we want to do the same thing, basically

// $('button.fave-btn').on('click', (evt) => {
//     const button = $(evt.target);
//     const buttonId = button.attr('id'); // the button is now the bus_id

    // notes example: $('body').css('fontfamily', buttonId);
        // this changes the font family to whatever the button id is
        // button id's in this example are "monospace", "sans-serif", "sans"
    // on click I want to add the business to the faves list for user in session




