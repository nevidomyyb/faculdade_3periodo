<?php
session_start();

if(isset($_POST['entrar'])){
    $email = $_POST['email'];

    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['email'] = $email;
        echo "Bem-vindo, " . $_SESSION['email'];
        echo "<form action='processar.php' method='POST'>
                <input type='submit' value='Sair' name='sair'>
              </form>";
    } else {
        echo "E-mail inválido.";
    }
} elseif(isset($_POST['sair'])) {
    unset($_SESSION['email']);
    echo "Sessão encerrada.";
    header("Location: index.php");
} else {
    if(isset($_SESSION['email'])) {
        echo "Bem-vindo, " . $_SESSION['email'];
    } else {
        echo "Faça login para continuar.";
        header("Location: index.php");
    }
}
?>