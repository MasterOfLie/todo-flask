from flask import jsonify
from models.TodoModel import Tarefas, db

class todoService:
    def listar_tarefas(self):
        todas_tarefas = Tarefas.query.all()
        retorno = []
        for tarefa in todas_tarefas:
            tarefa_data = {
                'id': tarefa.id,
                'nome': tarefa.nome,
                'descricao': tarefa.descricao,
                'status': tarefa.status,
                'data': tarefa.data_criacao.strftime('%d/%m/%Y') if tarefa.data_criacao else None
            }
            retorno.append(tarefa_data)
        return retorno

    def criar_tarefa(self, data):
        if not data.get('nome') or not data.get('descricao'):
            return jsonify({'message': 'Dados Incompletos!'}), 400
        nome = data['nome']
        descricao = data['descricao']
        status = data.get('status', 0)
        nova_tarefa = Tarefas(nome=nome, descricao=descricao, status=status)
        db.session.add(nova_tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa criada com sucesso!', 'id': nova_tarefa.id}), 201

    def atualizar_status(self, data, id):
        tarefa = Tarefas.query.get(id)
        if not data.get('status'):
            return jsonify({'message': 'Dados Incompletos!'}), 400
        status = data['status']
        if not tarefa:
            return jsonify({'message': 'Tarefa não encontrada!'}), 404
        tarefa.status = status
        db.session.commit()
        return jsonify({'message': 'Status da tarefa atualizado com sucesso!'}), 202

    def deletar_tarefa(self, id):
        tarefa = Tarefas.query.get(id)
        if not tarefa:
            return jsonify({'message': 'Tarefa não encontrada!'}), 404
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa deletada com sucesso!'}), 202
    
    def editar_nome(self, data, id):
        tarefa = Tarefas.query.get(id)
        if not tarefa:
            return jsonify({'message': 'Tarefa não encontrada!'}), 404
        if not data.get('nome'):
            return jsonify({'message': 'Dados Incompletos!'}), 400
        nome = data['nome']
        tarefa.nome = nome
        db.session.commit()
        return jsonify({'message': 'Nome da tarefa atualizado com sucesso!'})

    def editar_descricao(self, data, id):
        tarefa = Tarefas.query.get(id)
        if not tarefa:
            return jsonify({'message': 'Tarefa não encontrada!'}), 404
        if not data.get('descricao'):
            return jsonify({'message': 'Dados Incompletos!'}), 400
        descricao = data['descricao']
        tarefa.descricao = descricao
        db.session.commit()
        return jsonify({'message': 'Descrição da tarefa atualizado com sucesso!'})