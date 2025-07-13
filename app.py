from flask import Flask, render_template, url_for, session, request, redirect, flash, g
from database import Base, engine, SessionLocal
from models import Usuario, AnimaisAdocao 
from auth import bp as auth_bp  # importa o blueprint

app = Flask(__name__)
app.secret_key = 'Dev'

# registra blueprint
app.register_blueprint(auth_bp)

@app.before_request
def carregar_usuario_logado():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db = SessionLocal()
        g.user = db.query(Usuario).filter_by(id=user_id).first()
        db.close()

if not engine.dialect.has_table(engine.connect(), "usuarios"):
    Base.metadata.create_all(bind=engine)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
