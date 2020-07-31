function delUser(userId){
    var con = confirm('Are you sure you want to delete this User?')
    if(con==true){
        location.href='/user/del/'+userId;
    }
    else{
    alert("no!")
    }
}