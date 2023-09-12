<?php
include("conexao.php");

if(isset($_POST['salvar'])){
    $nome = $_POST['nome'];
    $telefone = $_POST['telefone'];
    $idade = $_POST['idade'];
    $local = $_POST['local'];

    $sql = "INSERT INTO moradias (nome, telefone, idade, local) VALUES ('$nome', '$telefone', $idade, '$local')";

    if ($conn->query($sql) === TRUE) {
        echo "Dados cadastrados com sucesso!";
    } else {
        echo "Erro ao cadastrar os dados: " . $conn->error;
    }
}

$conn->close(); 
?>