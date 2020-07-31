function delUser(userId){
    var con = confirm('Are you sure you want to delete this User?')
    if(con==true){
        location.href='/user/del/'+userId;
    }
    else{
    alert("no!")
    }
}

$(document).ready(function(){
	var actions = $("table td:last-child").html();

    $('#user_table').DataTable( {
        "pagingType": "full_numbers"
    } );
});
