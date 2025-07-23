from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select, text
from database import SessionLocal
from models import Usuario, TipoUsuarioEnum
from forms import LoginForm, RegisterForm,DenunciaForm,PontoAdocaoForm
from flask_login import current_user, logout_user

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


from flask_login import login_user

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        email = form.email.data
        senha = form.senha.data

        db = SessionLocal()
        try:
            user = db.query(Usuario).filter_by(email=email).first()

            if user is None:
                error = 'Email não encontrado.'
            elif not check_password_hash(user.senha, senha):
                error = 'Senha incorreta.'
            else:
                login_user(user)
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
    logout_user()
    session.clear()
    return redirect(url_for('home'))

@bp.route('/denunciar', methods=['GET', 'POST'])
@login_required
def denunciarAnimais():
    form = DenunciaForm()
    error = None

    if form.validate_on_submit():
        tipo_animal = form.tipo_animal.data
        coordenada = form.cordenada.data
        quantidade = form.quantidade.data
        id_usuario = current_user.id

        db = SessionLocal()
        try:
            db.execute(
                text("""
                    INSERT INTO denuncia_animais (tipo_animal, quantidade, cordenada, id_usuario)
                    VALUES (:tipo_animal, :quantidade, :coordenada, :id_usuario)
                """),
                {
                    'tipo_animal': tipo_animal,
                    'quantidade': quantidade,
                    'coordenada': coordenada,
                    'id_usuario': id_usuario
                }
            )
            db.commit()
            flash('Denúncia registrada com sucesso!', 'success')
            return redirect(url_for('map'))
        except Exception as e:
            db.rollback()
            error = f"Erro ao registrar denúncia: {str(e)}"
            flash(error, 'danger')
        finally:
            db.close()
    return render_template('auth/denunciar.html', form=form)
