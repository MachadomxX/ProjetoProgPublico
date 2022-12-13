let dados = JSON.stringify({email: sessionStorage.getItem("email"), cargo: sessionStorage.getItem("cargo")});
$.ajax({
    url: "http://localhost:5000/validar",
    type: "POST",
    dataType: 'json',
    contentType: 'text/plain',
    data: dados,
    success: deucerto,
    error: function(){
        alert("erro");
    }
});
function deucerto(x){
    if(x.resultado != "ok"){
        alert('não logado')
        window.location = `index.html`;

    }else if(x.resultado == 'no'){
        alert('você não tem perm')

        window.location = `${x.detalhes}.html`;
    }

    }
