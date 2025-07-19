from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select, text
from database import SessionLocal
from models import Usuario, TipoUsuarioEnum
from forms import LoginForm, RegisterForm,DenunciaForm,PontoAdocaoForm

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    error = None

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
        tipo = form.tipo.data
        nome_dono = form.nome_dono.data if tipo == 'empresa' else None

        db = SessionLocal()
        try:
            exists = db.execute(
                select(Usuario).where((Usuario.nome == nome) | (Usuario.email == email))
            ).scalar()

            if exists:
                if exists.nome == nome:
                    error = "Nome já registrado."
                elif exists.email == email:
                    error = "Email já registrado."
            else:
                novo = Usuario(
                    nome=nome,
                    email=email,
                    senha=generate_password_hash(senha),
                    tipo=TipoUsuarioEnum(tipo),
                    nome_dono=nome_dono
                )
                db.add(novo)
                db.commit()
                flash("Cadastro realizado com sucesso!", "success")
                return redirect(url_for('auth.login'))

        except Exception as e:
            db.rollback()
            error = f"Erro ao registrar: {e}"
        finally:
            db.close()

        flash(error, "danger")

    return render_template('auth/register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        email = form.email.data
        senha = form.senha.data

        db = SessionLocal()
        try:
            result = db.execute(
                text("SELECT * FROM usuarios WHERE email = :email"),
                {'email': email}
            )
            user = result.mappings().first()

            if user is None:
                error = 'Email não encontrado.'
            elif not check_password_hash(user['senha'], senha):
                error = 'Senha incorreta.'
            else:
                session.clear()
                session['email'] = user['email']
                session['user_id'] = user.id
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('home'))

        except Exception as e:
            error = f"Erro ao fazer login: {str(e)}"
        finally:
            db.close()

        flash(error, 'danger')

    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@bp.route('/denunciar', methods = ['GET', 'POST'])
def denunciarAnimais():
    form = DenunciaForm()
    error = None
    if form.validate_on_submit():
        tipoAnimal = form.tipo_animal.data
        cordenada = form.cordenada.data
        quantidade = form.quantidade.data
        nomeDenunciante = form.nome_denunciante.data

    return render_template('auth/denunciar.html', form=form)
