from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from pyterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()], render_kw={"placeholder": "E-mail"})
    senha = PasswordField("Senha", validators=[DataRequired()], render_kw={"placeholder": "Senha"})
    botao_confirmacao = SubmitField("Fazer Login")

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuario Inexistente...Crie uma Conta para Continuar!")


class FormCriarConta(FlaskForm):
    username = StringField("Nome de Usuario", validators=[DataRequired()], render_kw={"placeholder": "Usuario"})
    email = StringField("E-mail", validators=[DataRequired(), Email()], render_kw={"placeholder": "E-mail"})
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)], render_kw={"placeholder": "Senha"})
    confirmar_senha = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já esta Cadastrado ... Faça Login para Continuar!")


class FormFoto(FlaskForm):
    foto = FileField(validators=[DataRequired()])
    botao_confirmacao = SubmitField("")
