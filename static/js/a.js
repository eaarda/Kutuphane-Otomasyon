function Validate() {
    // Getting All Input Text Objects
    var input_username = document.forms["form_signup"]["username"];
    var input_name = document.forms["form_signup"]["name"];
    var input_email = document.forms["form_signup"]["email"];
    var input_email2 = document.forms["form_signup"]["email2"];
    var input_password = document.forms["form_signup"]["password"];
    var input_confirm_password =
        document.forms["form_signup"]["password_confirm"];

    // Getting All Error Display Objects
    var username_error = document.querySelector("#username_error");
    var name_error = document.querySelector("#name_error");
    var email_error = document.querySelector("#email_error");
    var email2_error = document.querySelector("#email2_error");
    var password_error = document.querySelector("#password_error");

    // Setting All Event Listeners
    input_username.addEventListener("blur", usernameVerify, true);
    input_name.addEventListener("blur", nameVerify, true);
    input_email.addEventListener("blur", emailVerify, true);
    input_email2.addEventListener("blur", email2Verify, true);
    input_password.addEventListener("blur", passwordVerify, true);

    // Username Validation
    if (input_username.value == "") {
        input_username.style.border = "1px solid red";
        username_error.textContent = "Username Is Required";
        input_username.focus();
        return false;
    }

    // Name Validation
    if (input_name.value == "") {
        input_name.style.border = "1px solid red";
        name_error.textContent = "Name Is Required";
        input_name.focus();
        return false;
    }

    // Email Validation
    if (input_email.value == "") {
        input_email.style.border = "1px solid red";
        email_error.textContent = "Email Is Required";
        input_email.focus();
        return false;
    }

    // Alternative Email Validation
    if (input_email2.value == "") {
        input_email2.style.border = "1px solid red";
        email2_error.textContent = "Alternative Email Is Required";
        input_email2.focus();
        return false;
    }

    // Password Validation
    if (input_password.value == "") {
        input_password.style.border = "1px solid red";
        password_error.textContent = "Password Is Required";
        input_password.focus();
        return false;
    }

    // Check If The Tow Passwords Match
    if (input_password.value != input_confirm_password.value) {
        input_password.style.border = "1px solid red";
        input_confirm_password.style.border = "1px solid red";
        password_error.innerHTML = "The Tow Passwords Do Not Match";
        return false;
    }

    // Event Handler Function
    function usernameVerify() {
        if (input_username.value != "") {
            input_username.style.border = "1px solid #ccc";
            username_error.innerHTML = "";
            return true;
        }
    }

    function nameVerify() {
        if (input_name.value != "") {
            input_name.style.border = "1px solid #ccc";
            name_error.innerHTML = "";
            return true;
        }
    }

    function emailVerify() {
        if (input_email.value != "") {
            input_email.style.border = "1px solid #ccc";
            email_error.innerHTML = "";
            return true;
        }
    }

    function email2Verify() {
        if (input_email2.value != "") {
            input_email2.style.border = "1px solid #ccc";
            email2_error.innerHTML = "";
            return true;
        }
    }

    function passwordVerify() {
        if (input_password.value != "") {
            input_password.style.border = "1px solid #ccc";
            password_error.innerHTML = "";
            return true;
        }
    }
}
//# sourceURL=pen.js


var hoverOver = ".header";
// document, '.header', '.logo'

$(hoverOver).on("mousemove", function(e) {
    $(".cube").css({
        transform: "rotateY(" + e.pageX / 4 + "deg) rotateX(" + e.pageY / 2 + "deg)"
    });
});