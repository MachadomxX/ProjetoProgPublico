
$(function(){ 
     $(document).on("click", ".editar_aluno", function () {
         eu = $(this).attr('id').split(",")[0];
         id = $(this).attr('id').split(",")[1];
         $("#CampoId").val(id)
         $("#campoNomeatualizarestudante").val($(`#nome${eu}`).text())
         $("#campoIdadeatualizarestudante").val($(`#idade${eu}`).text())
         $("#campoEmailatualizarestudante").val($(`#email${eu}`).text())
         $("#campoTelefoneatualizarestudante").val($(`#telefone${eu}`).text())
         $("#campoDataatualizarestudante").val($(`#data${eu}`).text().split("/")[2]+'-'+$(`#data${eu}`).text().split("/")[1]+'-'+ $(`#data${eu}`).text().split("/")[0])
         $("#campoMatriculaatualizarestudante").val($(`#matricula${eu}`).text())
     });

    function listar_aluno() {
        $.ajax({ 
            url: 'http://localhost:5000/listar/Estudante',
            method: 'GET',
            dataType: 'json', 
            success: listar_a,  
            error: function (x) {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar_a(pessoas) {
            $('#corpoTabelaAlunos').empty(); 
            console.log(pessoas)
            for (var i in pessoas) { 
                var lin = `<tr>
                    <td id = "nome${i}">${pessoas[i].nome}</td>
                    <td id = "idade${i}">${pessoas[i].idade}</td>
                    <td id = "email${i}">${pessoas[i].email}</td>
                    <td id = "telefone${i}">${pessoas[i].telefone}</td>
                    <td id = "matricula${i}">${pessoas[i].matricula}</td>
                    <td id = "data${i}">${pessoas[i].data}</td>
                    <td><a href=#modalatualizarestudante id="${i},${pessoas[i].id} " 
                           class="editar_aluno">editar</a>
                    </tr>`;
                $('#corpoTabelaAlunos').append(lin);
            }
        }
    }
    
    function listar_func() {
        $.ajax({ 
            url: 'http://localhost:5000/listar/Funcionario',
            method: 'GET',
            dataType: 'json', 
            success: listar_f,  
            error: function (x) {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar_f(pessoas) {
            $('#corpoTabelaFunc').empty(); 

            for (var i in pessoas) { 
                var lin = `<tr>
                    <td>${pessoas[i].nome}</td>
                    <td>${pessoas[i].idade}</td>
                    <td>${pessoas[i].email}</td>
                    <td>${pessoas[i].telefone}</td>
                    <td>${pessoas[i].cargaH}</td>
                    <td>${pessoas[i].salario}</td>
                    <td>${pessoas[i].cargo}</td>
                    <td><a href=# id="editar_pessoa_${pessoas[i].id}" 
                           class="link_editar_pessoa">editar</a>
                    </tr>`;
                $('#corpoTabelaFunc').append(lin);
            }
        }
    }
    listar_aluno();
    listar_func();
    $(document).on("click", "#btupdateAluno", function (){
        dados =  JSON.stringify({ id: $("#CampoId").val(), nome: $("#campoNomeatualizarestudante").val(), email: $("#campoEmailatualizarestudante").val(), telefone: $("#campoTelefoneatualizarestudante").val(), idade: $("#campoIdadeatualizarestudante").val(), data:$("#campoDataatualizarestudante").val(), matricula: $("#campoMatriculaatualizarestudante").val(), escolaId:$("#campoEscolaatualizarestudante").val()});
        console.log(dados)
        $.ajax({
            url: 'http://localhost:5000/atualizar/Estudante',
            type: 'PUT',
            dataType: 'json',
            contentType: 'application/json', 
            data: dados,
            success: EstudanteAtualizada,
            error: function erroAoAtualizar(x){
                alert("Erro: " + x.resultado + ":" + x.detalhes);
                    }
                })
            
                function EstudanteAtualizada(x){
                    if (x.resultado == "ok") {
                        alert("Estudante atualizado");
                        window.location = "#alunos";
                    }else{
                        alert("Erro: " + x.resultado + ":" + x.detalhes);
                    }
                }
            })
    $(document).on("click", "#btcadastrarAluno", function (){
        dados =  JSON.stringify({nome: $("#campocadastroNomeEstudante").val(), email: $("#campocadastroEmailEstudante").val(), telefone: $("#campocadastroTelefoneEstudante").val(), idade: $("#campocadastroIdadeEstudante").val(), data:$("#campocadastroDataEstudante").val(), matricula: $("#campocadastroMatriculaEstudante").val(), escolaId:$("#campocadastroEscolaEstudante").val(), senha:$("#campocadastroSenhaEstudante").val(), identidade:$("#campocadastroIdentidadeEstudante").val()  });
        console.log(dados)
        $.ajax({
            url: 'http://localhost:5000/cadastrar/Estudante',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json', 
            data: dados,
            success: Estudantecadastrado,
            error: function erroAocadastrar(x){
                alert("Erro: " + x.resultado + ":" + x.detalhes);
                    }
                })
            
                function Estudantecadastrado(x){
                    if (x.resultado == "ok") {
                        alert("Estudante cadastrado");
                        window.location = "#alunos";
                    }else{
                        alert("Erro: " + x.resultado + ":" + x.detalhes);
                    }
                }
            })

    $(document).on("click", "#btcadastraFuncionario", function (){
        if($("#campocadastroSenhaFuncionario").val() != ""){
            dados =  JSON.stringify({nome: $("#campocadastroNomeFuncionario").val(), email: $("#campocadastroEmailFuncionario").val(), telefone: $("#campocadastroTelefoneFuncionario").val(), idade: $("#campocadastroIdadeFuncionario").val(), data:$("#campocadastroDataFuncionario").val(), salario: $("#campocadastroSalarioFuncionario").val(), escolaId:$("#campocadastroEscolaFuncionario").val(), senha:$("#campocadastroSenhaFuncionario").val(), identidade:$("#campocadastroIdentidadeFuncionario").val(), cargaH:$("#campocadastroCargaHFuncionario").val(), cargos:$("#campocadastroCargoFuncionario").val()});
            console.log(dados)
            $.ajax({
                url: 'http://localhost:5000/cadastrar/Autenticado',
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json', 
                data: dados,
                success: FuncAcadastrado,
                error: function erroAoAtualizar(x){
                    alert("Erro: " + x.resultado + ":" + x.detalhes);
                        }
                    })
            }else{
            dados =  JSON.stringify({nome: $("#campocadastroNomeFuncionario").val(), email: $("#campocadastroEmailFuncionario").val(), telefone: $("#campocadastroTelefoneFuncionario").val(), idade: $("#campocadastroIdadeFuncionario").val(), data:$("#campocadastroDataFuncionario").val(), salario: $("#campocadastroSalarioFuncionario").val(), escolaId:$("#campocadastroEscolaFuncionario").val(), identidade:$("#campocadastroIdentidadeFuncionario").val(), cargaH:$("#campocadastroCargaHFuncionario").val(), cargos:$("#campocadastroCargoFuncionario").val()});
            console.log(dados)
            $.ajax({
                url: 'http://localhost:5000/cadastrar/Funcionario',
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json', 
                data: dados,
                success: FuncAcadastrado,
                error: function erroAoAtualizar(x){
                    alert("Erro: " + x.resultado + ":" + x.detalhes);
                        }
                    })
            }
        
        
            
                function FuncAcadastrado(x){
                    if (x.resultado == "ok") {
                        alert("Funcionario cadastrado");
                        window.location = "#servidores";
                    }else{
                        alert("Erro: " + x.resultado + ":" + x.detalhes);
                    }
                }
            })
        });