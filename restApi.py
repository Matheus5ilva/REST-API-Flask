from flask import Blueprint, Response
from api import Api

ws = Blueprint('ws', __name__, template_folder='templates', )
@ws.route('/ws/')
def index():
    pesquisa = ""
    api = Api(pesquisa)
    return Response(api.reader(), mimetype='application/json')

@ws.route('/ws/<string:teste>', methods=['GET',])
def pesquisa(teste):
    api = Api(teste)
    return Response(api.detalhes(teste), mimetype='application/json')

@ws.route('/ws/<string:teste>/<string:dirUm>', methods=['GET',])
def pesquisaDetalhada(teste, dirUm):
    dirDois = ''
    dirTres = ''
    api = Api(teste)
    t = api.readerDetalhes(teste,dirUm, dirDois, dirTres)
    return Response(t, mimetype='application/json')

@ws.route('/ws/<string:teste>/<string:dirUm>/<string:dirDois>', methods=['GET',])
def pesquisaDetalhadaDois(teste, dirUm, dirDois):
    dirTres = ''
    api = Api(teste)
    t = api.readerDetalhes(teste,dirUm, dirDois, dirTres)
    return Response(t, mimetype='application/json')

@ws.route('/ws/<string:teste>/<string:dirUm>/<string:dirDois>/<string:dirTres>', methods=['GET',])
def pesquisaDetalhadaTres(teste, dirUm, dirDois, dirTres):
    api = Api(teste)
    t = api.readerDetalhes(teste,dirUm, dirDois, dirTres)
    return Response(t, mimetype='application/json')


@ws.route('/ws/<string:teste>', methods=['POST',])
def inserir(teste):
    api = Api(teste)
    api.create()
    return pesquisa(teste)

@ws.route('/ws/<string:teste>/<string:dirUm>/<string:dirDois>/<string:editar>', methods=['PUT',])
def update(teste, dirUm, dirDois, editar):
    dirTres = ''
    api = Api(teste)
    api.updateWs(dirUm, dirDois, dirTres, editar)
    return pesquisa(teste)

@ws.route('/ws/<string:teste>/<string:dirUm>/<string:dirDois>/<string:dirTres>/<string:editar>', methods=['PUT',])
def updateTres(teste, dirUm, dirDois, dirTres,editar):
    api = Api(teste)
    api.updateWs(dirUm, dirDois, dirTres, editar)
    return pesquisa(teste)

@ws.route('/ws/<string:teste>', methods=['DELETE',])
def delete(teste):
    api = Api(teste)
    api.delete(teste)
    return index()
