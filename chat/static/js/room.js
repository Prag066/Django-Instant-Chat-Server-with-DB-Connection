//$(document).ready(function() {
//    console.log("stating...");
//     $("#chat-message-input").emojioneArea({
//         pickerPosition:"top",
//         inline:true,
//         // autocompleteTones:true
//
//     });
//});



const userName = JSON.parse(document.getElementById('user-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + userName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    let selectClass="";
    const usernameInputDom = document.querySelector('#uname');
    const uname = usernameInputDom.value;
    if(uname == data.uname){
        selectClass = "outgoingMsg";
    }
    else{
        selectClass = "incomingMsg";
    }

    var d=document.getElementById('chat-data');
        if (data.message){
        d.innerHTML +=  '<div class="row '+ selectClass+' ">'+
                            '<div class="col-sm-12">'+
                                '<div class="userName">'+
                                    data.uname+
                                '</div>'+
                            '</div>'+

                            '<div class="col-sm-12">'+
                                '<div class="userMsg">'+
                                    data.message;
                                +'</div>'+
                            '</div>'+
                        '</div>';
    }
    else if(data.image){
        d.innerHTML +=  '<div class="row '+ selectClass+' ">'+
                            '<div class="col-sm-12">'+
                                '<div class="userName">'+
                                    data.uname+
                                '</div>'+
                            '</div>'+

                            '<div class="col-sm-12">'+
                                '<div class="userMsg">'+
                                    '<img src="'+data.image+'" height=200px width=280px>';
                                +'</div>'+
                            '</div>'+
                        '</div>';
    };


};


chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};
//imput box submit
document.querySelector('#chat-message-submit').onclick = function(e) {
  submitMsg();
};

$('#chat-message-submit i').onclick = function(){
  submitMsg();
}
//input box emotion submit
document.querySelector('#chat-message-submit').onclick = function(e) {
  submitMsg();
};



function submitMsg(){
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    const usernameInputDom = document.querySelector('#uname');
    const uname = usernameInputDom.value;

    var fileReader = new FileReader();

    var filesSelected = document.getElementById("inputFileToLoad").files;
    if((messageInputDom.value).trim().length != 0){

            chatSocket.send(JSON.stringify({
                'image': '',
                'message': message,
                'uname' : uname
                }));
            messageInputDom.value = '';
        }
        else if(filesSelected.length > 0){
        var filesSelected = document.getElementById("inputFileToLoad").files;
        var fileToLoad = filesSelected[0];
        var fileReader = new FileReader();
        fileReader.onload = function(fileLoadedEvent){
            var srcData = fileLoadedEvent.target.result;

        chatSocket.send(JSON.stringify({
            'image': srcData,
            'message': '',
            'uname' : uname
            }));
                document.getElementById('inputFileToLoad').innerHTML = '';
        }
        fileReader.readAsDataURL(fileToLoad);
    }



//        chatSocket.send(JSON.stringify({
//        'message': message,
//        'uname' : uname
//        }));
//        messageInputDom.value = '';
//        $('.emojionearea-editor img').remove();

//    }
}

//function encodeImageAsUrl(){
//    const messageInputDom = document.querySelector('#chat-message-input');
//    const message = messageInputDom.value;
//
//    const usernameInputDom = document.querySelector('#uname');
//    const uname = usernameInputDom.value;
//
//    var filesSelected = document.getElementById("inputFileToLoad").files;
//    if(filesSelected.length > 0){
//        var fileToLoad = filesSelected[0];
//        var fileReader = new FileReader();
//        fileReader.onload = function(fileLoadedEvent){
//            var srcData = fileLoadedEvent.target.result;
////            console.log('src',srcData);
//
//        chatSocket.send(JSON.stringify({
//            'image': srcData ,
//            'message': '',
//            'uname' : uname
//            }));
//        }
//    }
//    fileReader.readAsDataURL(fileToLoad);
//}

