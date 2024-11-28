function verSenha(id) {
    const input = document.getElementById(`cadastro-input-password-${id}`);
    const button = document.getElementById(`cadastro-button-password-${id}`);

    if (input.type === "password") {
        input.type = "text";
        button.style.backgroundImage = "url('/wwwroot/img/icons-eye.png')";
    } else {
        input.type = "password";
        button.style.backgroundImage = "url('/wwwroot/img/icons-closed-eye.png')";
    }
}
