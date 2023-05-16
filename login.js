const submit = document.getElementById("submit");
submit.addEventListener("click", validate);

function validate(e){
    e.preventDefault();
    const loginField = document.getElementsById("idlogin"); //define a variavel login com referencia html 
    const passwordField = document.getElementById("idsenha"); //define a variavel senha com referencia html    
    let valid = true;

    if(!loginField.value){
        const loginError = document.getElementById("loginError"); //verifca se o valor digitado para login esta preenchido e retorna mensagem de erro        
        loginError.classList.add("visible");
        loginField.classList.add("invalid");
        loginError.setAttribute("aria-hidden", false);
        loginError.setAttribute("aria-invalid", true);
    }
    if(!passwordField.value){
        const passwordError = document.getElementById("passwordError"); //verifca se o valor digitado para senha esta preenchido e retorna mensagem de erro        
        passwordError.classList.add("visible"); 
        passwordField.classList.add("invalid");
        passwordError.setAttribute("aria-hidden", false);
        passwordError.setAttribute("aria-invalid", true);
    }
    return valid;
}//Função para verificar se existem dados nos campos de login e senha, ela retorna uma mensagem na tela solicitando que os campos sejam preenchidos

function logar(){
    var login = document.getElementById("idlogin").value; //pega o valor digitado no input    
    var senha = document.getElementById("idsenha").value; //pega o valor digitado no input
    if(login == "funcionarioSME" && senha == "%sme#portaria%"){
        alert('Login efetuado com sucesso');
        location.href = "http://127.0.0.1:5500/front-end/menu.html" 
    }
    else if(login == "admin" && senha == "admin"){
        location.href = "http://127.0.0.1:5500/front-end/menu.html"
    }
    else if(login == "administradorSME" && senha == "%admin*sme%"){
        alert('Login efetuado com sucesso');
        location.href = "http://127.0.0.1:5500/front-end/menu.html"
    }
    else{
        alert('USUARIO OU SENHA INCORRETOS');
    }
}