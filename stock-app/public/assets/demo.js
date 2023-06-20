
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
    setInterval(fetch, 30000)
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
        post(stock_obj)

    }
    xhttp.open('get',"http://127.0.0.1:5000/get-data")
    xhttp.send()
}

function post(obj){
    console.log("Post Function called successfully")
    let post_data = JSON.stringify(obj)
    
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        if(xhttp.status == 200 && xhttp.readyState == XMLHttpRequest.DONE){
            console.log("Successfully send data")
        }
        else{
            console.log("Error")
        }
    
    }
    xhttp.open('post','http://127.0.0.1:5000/send-mail')
    xhttp.setRequestHeader('Content-Type','application/json')
    xhttp.send(post_data);
}