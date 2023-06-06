document.getElementById('main-form').addEventListener('submit', checkForm);
function checkForm(event){
    event.preventDefault();
    var el = document.getElementById('main-form');
    var name = el.name.value;
    var surname = el.surname.value;
    var nickname = el.nickname.value;
    var state = el.state.value;
    var email = el.email.value;
    var pass = el.pass.value;
    var repass = el.repass.value;

    var fail = "";

    if(name == "" || surname == "" || nickname == "" || state == "" || email == "" || pass == "" || repass == "")
        fail = "Заполните все поля!";
    else if(pass != repass)
        fail = "Пароли не совпадают!";
    
    if(fail != ""){
        alert(fail);
    } else{
        alert("Все данные корректно заполнены")
        window.location.href = '';
    }
}
