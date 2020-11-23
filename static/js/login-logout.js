"use strict";

// const loginNav = document.getElementById('#login-navbar');

// document.querySelector('#login-submit').addEventListener('click' => {
//     const loginNav = document.getElementById('#login-navbar');
//     console.log(loginNav);

//     if (loginNav.innerHTML === 'Login') {
//         loginNav.innerHTML = 'Logout';
//     } else {
//         loginNav.innerHTML = 'Login';
//     }
// });

const loginNav = document.getElementById("login-navbar");

$.get('/isloggedin', (res) => {
    // alert(res)
    if (res === true) {
        loginNav.innerHTML = 'Logout';
        // $(loginNav).attr("href","/logout");
    };
});

if (loginNav.innerHTML == 'Logout') {
    const oldUrl = $(loginNav).attr("href");
    const newUrl = oldUrl.replace("/signin", "logout");
    $(loginNav).attr("href", newUrl);
}


//function replaceLoginHTML(){
    // alert("what the fuckkkk")
    //console.log(
   
    // if (loginNav.innerHTML === 'Login') {
    //     loginNav.innerHTML = 'Logout';
    // } else {
    //     loginNav.innerHTML = 'Login';
    // }

//};

//$('#login-submit').on('click', replaceLoginHTML)



// const loginBtn = document.querySelector('#login-navbar');
// const loginSubmit = document.querySelector('#login-submit');
// loginSubmit.on('click' => 
//     if (loginBtn.innerHTML === 'Login') {
//         loginBtn.innerHTML = 'Logout';
//     } else {
//         loginBtn.innerHTML = 'Login';
//     }
// });

// function changeLogin (evt) {
//     $.get('/', (evt) => {
//         $('login-navbar').html("Logout");
//     });
// };

// $('#login-submit').on('click', => {
//     $.get('#login-navbar').text("Logout")
// });