$(function(){
    $(document).on("click", "#Login", function(){
        let email = $("#user").val();
        let password = $("#password").val();
        let dados = JSON.stringify({email: email, senha: password});
        $.ajax({
            url: "http://localhost:5000/logar",
            type: "POST",
            dataType: 'json',
            contentType: 'text/plain',
            data: dados,
            //xhrFields: { withCredentials: true },
            success: deucerto,
            error: function(){
                alert("a");
            }
        });
        function deucerto(x){
            if(x.resultado == "ok"){
                sessionStorage.setItem('email', email);
                sessionStorage.setItem('cargo', x.detalhes)
                window.location = `${x.detalhes}.html`;
                $("#user").val(' ');
                $("#password").val(" ")
            }else{
                alert('error')
            };
        };
    });

});