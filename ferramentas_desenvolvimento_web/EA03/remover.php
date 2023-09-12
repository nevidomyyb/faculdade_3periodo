<!DOCTYPE html>
<html>
<head>
    <title>Remover Item</title>
</head>
<body>
    <h1>Remover Item do Banco de Dados</h1>
    <form action="" method="POST">
        <label for="id">ID do item a ser removido:</label>
        <input type="number" id="id" name="id" required>
        <input type="submit" value="REMOVER" name="remover">
    </form>

    <?php
    include("conexao.php");

    if(isset($_POST['remover'])){
        $id = $_POST['id'];

       
        $sql_linha = "DELETE FROM moradias WHERE id = $id";

        if ($conn->query($sql_linha) === TRUE) {
            echo "Item removido com sucesso!";
        } else {
            echo "Erro ao remover o item: " . $conn->error;
        }
    }

    $conn->close();
    ?>
</body>
</html>
