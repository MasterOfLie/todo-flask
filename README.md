Sobre o Projeto
Esse projeto faz parte de um trabalho acadêmico para a disciplina de Linguagem de Programação. O trabalho foi dividido em grupos, onde uma equipe ficou responsável pela parte do front-end e outra equipe pela parte do back-end.
Este projeto se refere à parte do back-end, onde foi desenvolvida uma API REST para uma aplicação TODO (gerenciamento de tarefas). O usuário pode enviar informações no formato JSON para criar, editar, concluir e excluir tarefas.
/listar (GET): Retorna a lista de tarefas.
/criar (POST): Recebe dados em JSON para criar uma nova tarefa.
/atualizar/status/<int:id> (PUT): Atualiza o status de uma tarefa específica pelo ID.
/deletar/<int:id> (DELETE): Deleta uma tarefa específica pelo ID.
/atualizar/nome/<int:id> (PUT): Atualiza o nome de uma tarefa específica pelo ID.
/atualizar/descricao/<int:id> (PUT): Atualiza a descrição de uma tarefa específica pelo ID.
