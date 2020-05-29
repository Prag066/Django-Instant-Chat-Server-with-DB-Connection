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
    if((messageInputDom.value).trim().length != 0){
        chatSocket.send(JSON.stringify({
        'message': message,
        'uname' : uname
        }));
        messageInputDom.value = '';
//        $('.emojionearea-editor img').remove();

    }
}

