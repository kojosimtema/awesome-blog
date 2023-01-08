
function readMore () {

        if (document.querySelector('#dots').style.display == "none") {
            document.querySelector('#dots').style.display = "inline";
            document.querySelector('#btn').innerHTML = "Show more"
            document.querySelector('#readmore').style.display = "none";
            
      } else {
            document.querySelector('#dots').style.display = "none";
            document.querySelector('#btn').innerHTML = "Show less"
            document.querySelector('#readmore').style.display = "inline";
    
           
        
       
  }
        console.log(views)
        console.log(count)
 }


function deleteAlert(){
      alert('Are you sure you want to delete this post?')
}

function hideAlert () {
      document.querySelector('#alert-2').style.display = "none";
}


