function VerSenha(){
    const input = document.getElementById("login-input-password")
    const button = document.getElementById("login-button-password")

    if (input.type == "password"){
        input.type = "text"
        button.style.backgroundImage = "url('/wwwroot/img/icons-eye.png')"
    }else{
        input.type = "password"
        button.style.backgroundImage = "url('/wwwroot/img/icons-closed-eye.png')"
    }
}