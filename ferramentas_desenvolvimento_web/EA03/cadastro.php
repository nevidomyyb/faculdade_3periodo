<!DOCTYPE html>
<html>
<head>
    <title>Cadastro de Moradias</title>
</head>
<body>
    <h1>Cadastro de Moradias</h1>
    <form action="processar_cadastro.php" method="POST">
        <label for="nome">Nome do Morador:</label>
        <input type="text" id="nome" name="nome" required><br><br>

        <label for="telefone">Telefone para Contato:</label>
        <input type="text" id="telefone" name="telefone" required><br><br>

        <label for="idade">Idade:</label>
        <input type="number" id="idade" name="idade" required><br><br>

        <label for="local">Local:</label>
        <input type="text" id="local" name="local" required><br><br>

        <input type="submit" value="SALVAR" name="salvar">
    </form>
</body>
</html>