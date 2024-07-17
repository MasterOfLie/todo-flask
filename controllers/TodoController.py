from flask import Blueprint, jsonify, request
from services.todoService import todoService

todo_bp = Blueprint('tarefas', __name__)
tarefa_service = todoService()

@todo_bp.route('/listar', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefa_service.listar_tarefas())

@todo_bp.route('/criar', methods=['POST'])
def criar_tarefa():
    data = request.get_json()
    return tarefa_service.criar_tarefa(data)

@todo_bp.route('/atualizar/status/<int:id>', methods=['PUT'])
def mudar_status(id):
    data = request.get_json()
    return tarefa_service.atualizar_status(data, id)

@todo_bp.route('/deletar/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    return tarefa_service.deletar_tarefa(id)

@todo_bp.route('/atualizar/nome/<int:id>', methods=['PUT'])
def mudar_nome(id):
    data = request.get_json()
    return tarefa_service.editar_nome(data, id)
    
@todo_bp.route('/atualizar/descricao/<int:id>', methods=['PUT'])
def mudar_descricao(id):
    data = request.get_json()
    return tarefa_service.editar_descricao(data, id)