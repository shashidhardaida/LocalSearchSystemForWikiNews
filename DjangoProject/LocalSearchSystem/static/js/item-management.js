$(document).ready(function(){
	var actions = $("table td:last-child").html();

    $('#item_table').DataTable( {
        "pagingType": "full_numbers"
    } );
});

function delItem(itemId){
    var con = confirm('Are you sure you want to delete the item?')
    if(con==true){
//        location.href = '/WikiNews/item/del/'+itemId;
        location.href='/wikinews/item/del/'+itemId;
    }
    else{
    alert("no!")
    }
}

function itemDetail(itemTitle){

location.href = '/wikinews/itemdetails/'+itemTitle;

}