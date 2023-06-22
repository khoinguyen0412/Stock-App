
$(function(){
	$('div[onload]').trigger('onload');
});

$('#form').submit(function(e) {
    console.log('submit');
    toastr.success("Susccesfully submitted!")
});


$("document").ready(function(){
    console.log('In Progress');
    setTimeout(function(){
        $('div.alert').remove();
    },3000)

})

function updateDialog(e){
    document.getElementById("input_stock").value = `${e.id}`
    
} 

function uncheck(){
    let input = document.getElementById("input_stock").value
    document.getElementById(`${input}`).checked = false
    $('#form')[0].reset()
}

function fetch_timer(){
    fetch()
    setInterval(fetch, 120000)
}

function updateContent(element,content){
    // console.log(element,content)
    element.innerHTML = content
    element.style.backgroundColor =  "rgba(128,128,128,0.5)"
    // change the background color back (with a delay equal to transition length)
        setTimeout(() => { element.style.backgroundColor = 'white'; }, 500)
}


function fetch(){
    console.log("Function called successfully")
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        stock_obj = null
        if(this.status == 200){
            try{
                const obj = JSON.parse(this.responseText);
                stock_obj = obj
            }
            catch(e){
                console.log('Error parsing')
            }
        }
        else{
            console.warn('Did not receive 200 OK from response')
        }   


        stock_obj.forEach(function(value){
            updateContent(document.getElementById(`price-${value.stock_code}`), value.current_price);
        }
      
        )

    }
    xhttp.open('get',"http://127.0.0.1:8080/get-data")
    xhttp.send()
}

