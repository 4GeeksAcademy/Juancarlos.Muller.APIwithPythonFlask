from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_data = request.get_json()  # Obtener el contenido JSON del cuerpo de la solicitud
    new_todo = {
        "label": request_data.get("label", "Default task"),  # Obtener "label" del JSON o usar "Default task" si no está presente
        "done": False
    }
    todos.append(new_todo)  # Agregar el nuevo elemento a la lista todos
    return jsonify(todos)  # Devolver la lista actualizada todos en formato JSON

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400

    del todos[position]  # Elimina el elemento en la posición especificada
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
