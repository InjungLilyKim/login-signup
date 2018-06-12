$(document).ready(function() {
    $("#signup-container").hide();

    $('#login-button').click(function(e){
        e.stopPropagation();
        e.preventDefault();
        login();
        return false;
    });

    $('#signup-button').click(function(e){
        e.stopPropagation();
        e.preventDefault();
        signup();
        return false;
    });
});

function login(){
    var postData = $("#login-form input");
    $.post( "/login", { "login-username" : postData[0].value, "login-password": (postData[1].value) } )
        .done(function( data ) {
            window.location.replace("http://localhost:3000");
            $("#login-container").hide();
            $("#signup-container").hide();
            console.log(data)
        })
        .fail(function(data) {
            $("#login-flash").text(data.responseJSON.error);
        }); 
}

function signup(){
    var postData = $("#signup-form input");
    $.post( "/signup", { "signup-username" : postData[0].value, "signup-password": (postData[1].value), "signup-password-confirm": (postData[2].value) } )
        .done(function( data ) {
            window.location.replace("http://localhost:3000");
            $("#login-container").hide(); 
            $("#signup-container").hide();
            console.log(data)
        })
        .fail(function(data) {
            $("#signup-flash").text(data);
            console.log(data);
        });
}

function showSignUpForm(){
  $("#login-container").hide();
  $("#signup-container").show();
}

function showLogInForm(){
  $("#signup-container").hide();
  $("#login-container").show();
}
