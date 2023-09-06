#Informações sobre o projeto:
Foram usadas tecnologias como: Python com Django para criação do servidor web.
HTML + CSS com SASS e GULP para criação do frontend.

#Como rodar localmente:
1.Após clonar o repositório certifique-se de iniciar um ambiente de desenvolvimento python com o comando:
`python -m venv venv`
2.Iniciar o ambiente de desenvolvimento:
**Dependendo do sistema operacional essa linha de comando pode mudar**
`.venv/Scripts/activate`
2.Instalar dependências python do projeto:
`pip install -r requirements.txt`
3.Iniciar o servidor local:
`python manage.py runserver`
4.Passo adicional: **Em caso de alteração no SCSS**
4.1.Instalar dependências do node:
`npm install`
`npm run gulp watch`
4.2.Salvar o arquivo scss alterado
O gulp irá compilar o arquivo diretamente para o static folder correspondente.

#Em relação ao banco de dados:
O banco utilizado para desenvolvimento foi o sqlite porém pode-se utilizar outros alterando nas configurações do Django no folder: [./pi/settings.py](https://github.com/nevidomyyb/faculdade_3periodo/blob/main/projeto_integrador/pi/settings.py)
