from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .models import User, Veicles
from app import db
import os

# Cria o blue print
main = Blueprint('main', __name__)

@main.route('/')
def cad():
    return render_template('register.html')

@main.route('/menu')
def inicial():
    return render_template('index.html')

@main.route('/veiculos')
def veiculos():
    veiculos_list = Veicles.query.all()
    return render_template('veiculos.html', veiculos=veiculos_list)

@main.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_veiculo(id):
    if 'user_id' not in session or session['username'] != 'admin':
        flash('pode n man', 'danger')
        return redirect(url_for('main.veiculos'))

    veiculo = Veicles.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()

    flash('sumiu em', 'success')
    return redirect(url_for('main.veiculos'))

@main.route('/formularios', methods=['POST', 'GET'])
def formu():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        placa = request.form['placa']
        valor = request.form['valor']
        file = request.files['file']
        
        filename = file.filename
        
        veicles = Veicles(Marca=marca, Modelo=modelo, Placa=placa, Valor=valor, Img=filename)
        db.session.add(veicles)
        db.session.commit()
        
        upload_folder = 'app/static/uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        file.save(os.path.join(upload_folder, file.filename))
        return render_template('formularios.html', res="adicionou de boa")
        
    return render_template('formularios.html')        

@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']
        cpf = request.form['cpf']

        existing_user = User.query.filter_by(Usuario=user).first()

        if existing_user:
            flash('esse ja tem man, usa oto', 'danger')
            return redirect(url_for('main.register'))

        usuario = User(Usuario=user, senha=senha, CPF=cpf)
        db.session.add(usuario)
        db.session.commit()

        flash('bem vindo, faça seu login', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']

        usuario = User.query.filter_by(Usuario=user).first()

        if usuario and usuario.senha == senha:
            session['user_id'] = usuario.id
            session['username'] = usuario.Usuario
            
            flash('entrou amigão', 'success')
            return redirect(url_for('main.inicial'))
        else:
            flash('tem algo errado ai em ( ͡° ͜ʖ ͡°)', 'danger')
    return render_template('login.html')

