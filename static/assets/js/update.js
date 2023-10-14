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