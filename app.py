from flask import Flask, render_template
from flask_migrate import Migrate
from models.TodoModel import db
from flasgger import Swagger
from controllers.TodoController import todo_bp
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://dev:dev@localhost/dev' 
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)
swagger = Swagger(app, template_file='resource/swagger_config.yml')
app.register_blueprint(todo_bp, url_prefix='/')



app.run(debug=True, host='0.0.0.0', port=5000)