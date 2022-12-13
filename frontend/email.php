<?php

if(isset($_POST(['email']) && !empty($_POST(['email'])){
$nome = addcslashes($_POST(['name']))
$email = addcslashes($_POST(['email']))
$mensagem = addcslashes($_POST(['message']))

$to = "warmlinglarissa1@gmail.com";
$subject = "Contato = Programa";
$body = "Nome:".$nome. ""

}

?>