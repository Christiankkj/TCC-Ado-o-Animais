from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegisterForm(FlaskForm):
    tipo = SelectField('Tipo', choices=[('pessoa', 'Pessoa'), ('empresa', 'Empresa')], validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    nome_dono = StringField('Nome do Dono')
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Registrar')


#class CadasterForm(FlaskForm):
   # tipo = SelectField('Tipo', choices=[('cachorro','Cachorro'), ('gato','Gato')],validators=[DataRequired()])
    #cordenada = SelectField('Cordenada', validators=DataRequired())
   # quantidade = SelectField('Quantidade', validators=DataRequired())

class DenunciaForm(FlaskForm):
    tipo_animal = SelectField('Tipo de Animal',choices=[('gato', 'Gato'), ('cachorro', 'Cachorro'), ('ambos', 'Ambos')],validators=[DataRequired()]) 
    cordenada = SelectField('Cordenada', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade',validators=[DataRequired(), NumberRange(min=1, message="Deve ser pelo menos 1")])
    data_denuncia = DateField('Data da Denúncia',format='%Y-%m-%d',validators=[DataRequired()] )
    nome_denunciante = StringField('Nome do Denunciante',validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Enviar Denúncia')

class PontoAdocaoForm(FlaskForm):
    nome_local = StringField( 'Nome do Local',validators=[DataRequired(), Length(max=100)])
    tipo_animal = SelectField('Tipo de Animal',choices=[('gato', 'Gato'), ('cachorro', 'Cachorro'), ('ambos', 'Ambos')],validators=[DataRequired()])
    cordenada = SelectField('Cordenada', validators= [DataRequired()])
    responsavel_nome = StringField('Nome do Responsável',validators=[Length(max=100)])
    responsavel_contato = StringField('Contato do Responsável', validators=[Length(max=100)])
    submit = SubmitField('Cadastrar Ponto de Adoção')

