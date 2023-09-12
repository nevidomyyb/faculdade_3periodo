# Documentação
- Foi usado MySQL e MySQLi (MySQL Improved) como extensão para realizar a comunicação entre o servidor MySQL e o PHP.
- Utilizando-se do XAMPP para replicar um ambiente de desenvolvimento que possa rodar PHP.
# Dependencias e Requisitos
- Um servidor MySQL
- Um banco de dados já criado
- Tabela já criada seguindo a estrutura:
- `CREATE TABLE moradias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(250),
    telefone VARCHAR(15),
    idade INT,
    local VARCHAR(250)
);`
# Configuração da conexão
- Configurações feitas no arquivo: [./conexao.php](https://github.com/nevidomyyb/faculdade_3periodo/blob/main/ferramentas_desenvolvimento_web/EA03/conexao.php).
- Variável servername para o host do servidor, utilizado localhost para ambiente local
- Variável username para o usuário que realizará conexão com o banco de dados
- Variável password para a senha do usuário da conexão
- Variável dbname para o nome do banco de dados, utilizado ea03 no desenvolvimento local.

