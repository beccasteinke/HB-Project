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



// Change icon when button clicked
// TODO: when clicked twice, the button changes to two checkmarks
function changeIcon(evt) {
    // evt.preventDefault()
    evt.target.src="static/icons/checkmark-50.png";
    alert("Business added to profile!")
}

const allIcons = document.querySelectorAll('.fave-btn')

for (const icon of allIcons) {
    icon.addEventListener('click', changeIcon)
}
const iconId = icon.attr('id');
// const formData = {
//     user_id: $()
// }

// $.get('/directory', (data) => {
//     alert(data)
// })

// $.post('/add-favorite', iconId, (response) => {
//     alert(response)
// })

// now I need to update the DB with id with button clicked
// on click, add bus_id(buttonId) to userbus table associated with user_id



// $('button.fave-btn').on('click', (evt) => {
//     const button = $(evt.target);
//     const buttonId = button.attr('id'); // the button is now the bus_id

    // notes example: $('body').css('fontfamily', buttonId);
        // this changes the font family to whatever the button id is
        // button id's in this example are "monospace", "sans-serif", "sans"
    // on click I want to add the business to the faves list for user in session




