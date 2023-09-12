<?php
session_start();

if (isset($_SESSION['email'])) {
    echo "Bem-vindo, " . $_SESSION['email'];
    echo "<form action='processar.php' method='POST'>
            <input type='submit' value='Sair' name='sair'>
          </form>";
} else {
    echo '<h1>Autenticação</h1>
    <form action="processar.php" method="POST">
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="senha">Senha:</label>
        <input type="password" id="senha" name="senha" required><br><br>

        <input type="submit" value="Entrar" name="entrar">
    </form>';
}
?>