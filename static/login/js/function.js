async function login(){
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    if ((username == "") || (password) == ""){
        Ext.Msg.alert("Error", "請輸入帳號密碼")
    }

}