from flask import Flask, render_template
from database import Base, engine, SessionLocal
from flask_login import LoginManager
from models import Usuario
from auth import bp as auth_bp

app = Flask(__name__)
app.secret_key = 'Dev'

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # rota para onde redirecionar se não estiver logado

# Função que carrega o usuário a partir do ID armazenado na sessão
@login_manager.user_loader
def load_user(user_id):
    db = SessionLocal()
    user = db.query(Usuario).get(int(user_id))
    db.close()
    return user


app.register_blueprint(auth_bp, url_prefix='/auth')

# Criar as tabelas se ainda não existirem
if not engine.dialect.has_table(engine.connect(), "usuarios"):
    Base.metadata.create_all(bind=engine)

# Rota principal
@app.route("/")
def home():
    return render_template('home.html')

# Iniciar o servidor
if __name__ == "__main__":
    app.run(debug=True)
