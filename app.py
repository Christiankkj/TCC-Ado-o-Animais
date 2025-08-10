from flask import Flask, render_template
from database import Base, engine, SessionLocal
from flask_login import LoginManager
from models import Usuario
from auth import bp as auth_bp
from sqlalchemy import text

app = Flask(__name__)
app.secret_key = 'Dev'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  

# Função que carrega o usuário a partir do ID armazenado na sessão
@login_manager.user_loader
def load_user(user_id):
    db = SessionLocal()
    user = db.query(Usuario).get(int(user_id))
    db.close()
    return user


app.register_blueprint(auth_bp, url_prefix='/auth')

if not engine.dialect.has_table(engine.connect(), "usuarios"):
    Base.metadata.create_all(bind=engine)


@app.route('/')
def home():
    db = SessionLocal()
    try:
        # Transforma RowMapping em dicionário com list comprehension
        denuncias = [dict(row) for row in db.execute(text("SELECT * FROM denuncia_animais")).mappings().all()]
        pontos = [dict(row) for row in db.execute(text("SELECT * FROM ponto_adocao")).mappings().all()]
    finally:
        db.close()

    return render_template("home.html", denuncias=denuncias, pontos=pontos)

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)

