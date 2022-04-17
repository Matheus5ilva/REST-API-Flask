from flask import Blueprint, render_template, request, redirect, jsonify
import json
from api import Api

repositorio = Blueprint('repositorio', __name__, template_folder='templates')

@repositorio.route('/')
def index():
    return render_template('index.html')

@repositorio.route('/pesquisa', methods=['POST',])
def pesquisa():
    pesquisa = request.form['search']
    if(pesquisa == ''):
        return index()
    return viewReader(pesquisa)

@repositorio.route('/view')
def viewReader(pesquisa):
    api = Api(pesquisa)
    return render_template('search.html', pesquisa=json.loads(api.detalhes(pesquisa)))

@repositorio.route('/create', methods=['GET',])
def create():
    pesquisa = request.args.get('pesquisa')
    api = Api(pesquisa)
    api.create()
    return redirect('/lista')

@repositorio.route('/lista')
def reader():
    pesquisa = ''
    api = Api(pesquisa)
    return render_template('lista.html', pesquisas=json.loads(api.reader()))

@repositorio.route('/detalhes', methods=['GET',])
def detalhes():
    pesquisa = ''
    name = request.args.get('name')
    api = Api(pesquisa)
    editar = json.loads(api.detalhes(name))
    return render_template('detalhes.html', pesquisa=editar)

@repositorio.route('/editar', methods=['GET',])
def editar():
    pesquisa = ''
    name = request.args.get('name')
    api = Api(pesquisa)
    editar = json.loads(api.detalhes(name))
    return render_template('editar.html', pesquisa=editar)

@repositorio.route('/edit', methods=['POST',])
def edit():
    pesquisa = request.form
    construtor = request.form['tituloWiki']
    api = Api(construtor)
    api.update(pesquisa)
    return redirect("/lista")



@repositorio.route('/delete', methods=['GET',])
def delete():
    pesquisa = ''
    name = request.args.get('name')
    api = Api(pesquisa)
    api.delete(name)
    return redirect('/lista')


