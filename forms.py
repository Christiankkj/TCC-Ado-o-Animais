from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegisterForm(FlaskForm):
    tipo = SelectField('Tipo', choices=[('pessoa', 'Pessoa'), ('empresa', 'Empresa')], validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    nome_dono = StringField('Nome do Dono (se for empresa)')
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Registrar')
