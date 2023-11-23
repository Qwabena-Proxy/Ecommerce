function updatecheckbox(){
    let checkbtn= document.querySelector('#fid').value
    if (checkbtn == 'no'){
        checkbtn= 'yes';
        document.querySelector('#fid').value= checkbtn
    } else{
        checkbtn= 'no';
        document.querySelector('#fid').value= checkbtn
    }
    console.log(document.querySelector('#fid').value)
}


function updateImagePreview(event) {
    const imageInput = event.target;
    const previewImage = document.getElementById('preview-image');
    
    if (imageInput.files && imageInput.files[0]) {
      const reader = new FileReader();
      
      reader.onload = function (e) {
        previewImage.src = e.target.result;
      }
      
      reader.readAsDataURL(imageInput.files[0]);
    }
  }

