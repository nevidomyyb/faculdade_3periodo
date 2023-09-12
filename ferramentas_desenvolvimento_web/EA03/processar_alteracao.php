<?php
include("conexao.php");

if(isset($_POST['atualizar'])){
    $id = $_POST['id'];
    $nome = $_POST['nome'];
    $telefone = $_POST['telefone'];
    $idade = $_POST['idade'];
    $local = $_POST['local'];

    $sql_linha = "UPDATE moradias SET nome='$nome', telefone='$telefone', idade=$idade, local='$local' WHERE id = $id";

    if ($conn->query($sql_linha) === TRUE) {
        echo "Dados atualizados com sucesso!";
    } else {
        echo "Erro ao atualizar os dados: " . $conn->error;
    }
}

$conn->close();
?>