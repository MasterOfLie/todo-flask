# Sobre o Projeto

Esse projeto faz parte de um trabalho acadêmico para a disciplina de Linguagem de Programação. O trabalho foi dividido em grupos, onde uma equipe ficou responsável pela parte do front-end e outra equipe pela parte do back-end.

Este projeto se refere à parte do back-end, onde foi desenvolvida uma API REST para uma aplicação TODO (gerenciamento de tarefas). O usuário pode enviar informações no formato JSON para criar, editar, concluir e excluir tarefas.

## Endpoints da API

### Listar Tarefas

`/listar` (GET): Retorna a lista de tarefas.

### Criar Tarefa

`/criar` (POST): Recebe dados em JSON para criar uma nova tarefa.

### Atualizar Status da Tarefa

`/atualizar/status/<int:id>` (PUT): Atualiza o status de uma tarefa específica pelo ID.

### Deletar Tarefa

`/deletar/<int:id>` (DELETE): Deleta uma tarefa específica pelo ID.

### Atualizar Nome da Tarefa

`/atualizar/nome/<int:id>` (PUT): Atualiza o nome de uma tarefa específica pelo ID.

### Atualizar Descrição da Tarefa

`/atualizar/descricao/<int:id>` (PUT): Atualiza a descrição de uma tarefa específica pelo ID.
