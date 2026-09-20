# Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido para auxiliar micro e pequenos empreendimentos no gerenciamento de produtos e movimentações de estoque.
O sistema permite cadastrar e consultar produtos, registrar entradas e saídas, acompanhar o histórico de movimentações, verificar o estoque mínimo, consultar valores de estoque e gerar relatórios.

## Objetivo

O projeto tem como objetivo oferecer uma alternativa simples para o controle de estoque, permitindo organizar informações sobre produtos e suas movimentações de forma prática.

## Tecnologias utilizadas
-Python
-SQLite

## Funcionalidades

O sistema possui as seguintes funcionalidades:
1. **Cadastrar produto** - permite cadastrar novos produtos informando código, nome, categoria, preços e estoque mínimo.
2. **Consultar produtos** - permite visualizar os produtos cadastrados e suas respectivas informações.
3. **Alterar produto** - permite modificar informações de um produto já cadastrado.
4. **Excluir produto** - permite excluir um produto cadastrado, respeitando o histórico de movimentações.
5. **Registrar entrada** - registra a entrada de produtos e atualiza automaticamente a quantidade disponível em estoque.
6. **Registrar saída** - registra a saída de produtos, realizando a validação da quantidade disponível antes de atualizar o estoque.
7. **Consultar histórico** - permite visualizar as movimentações de entrada e saída realizadas no sistema.
8. **Verificar estoque mínimo** - identifica produtos cuja quantidade em estoque está igual ou abaixo do estoque mínimo definido.
9. **Consultar valores de estoque** - apresenta o valor dos produtos em estoque com base no preço de compra.
10. **Relatórios** - apresenta informações gerais sobre o estoque, como quantidade de produtos, itens armazenados, produtos com estoque mínimo, valor total do estoque e quantidade de movimentações.

## Como executar o projeto

### Pré-requisitos

- Python 3 instalado
- SQLite, utilizado pelo próprio Python


### Execuçao

1. Faça o download ou clone este repositório.
2. Abra a pasta do projeto no computador.
3. Execute o arquivo `Atividade.py` utilizando o python.
