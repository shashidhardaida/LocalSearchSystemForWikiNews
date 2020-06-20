
//This function is used to validate the login form once user entered credentials and hit login button
function validateForm() {
    var user_name = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var dummy_user_name = 'admin'
    var dummy_password = 'p@ssword!23'
    if (user_name === "" & password ==="") {
        alert("Please enter credentials");
    }
    else if (password === "") {
        alert("Password must be filled out");
    }
    else if (user_name === "") {
        alert("User Name must be filled out");
    }
    else if(user_name == "admin" && password == "admin")
    { 
        window.location="http://www.w3schools.com";
    }
    else{
        window.location = 'Src/search.html';  
    }
    return false;
}
    
    
