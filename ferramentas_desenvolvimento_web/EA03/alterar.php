<!DOCTYPE html>
<html>
<head>
    <title>Alteração de Dados</title>
</head>
<body>
    <h1>Alteração de Dados</h1>
    <form action="" method="POST">
        <label for="id">ID do Item a Ser Alterado:</label>
        <input type="number" id="id" name="id" required>
        <input type="submit" value="BUSCAR" name="buscar">
    </form>

    <?php
    include("conexao.php"); 

    if(isset($_POST['buscar'])){
        $id = $_POST['id'];
        $sql = "SELECT * FROM moradias WHERE id = $id";
        $resultado = $conn->query($sql);

        if ($resultado->num_rows > 0) {
            $row = $resultado->fetch_assoc();
    ?>
    <form action="processar_alteracao.php" method="POST">
        <input type="hidden" name="id" value="<?php echo $row['id']; ?>">

        <label for="nome">Nome do Morador:</label>
        <input type="text" id="nome" name="nome" value="<?php echo $row['nome']; ?>" required><br><br>

        <label for="telefone">Telefone para Contato:</label>
        <input type="text" id="telefone" name="telefone" value="<?php echo $row['telefone']; ?>" required><br><br>

        <label for="idade">Idade:</label>
        <input type="number" id="idade" name="idade" value="<?php echo $row['idade']; ?>" required><br><br>

        <label for="local">Local:</label>
        <input type="text" id="local" name="local" value="<?php echo $row['local']; ?>" required><br><br>

        <input type="submit" value="ATUALIZAR" name="atualizar">
    </form>
    <?php
        } else {
            echo "Item não encontrado.";
        }
    }

    $conn->close();
    ?>
</body>
</html>
