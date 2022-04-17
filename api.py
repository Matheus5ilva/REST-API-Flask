#IPORTACAO DAS BIBLIOTECAS USADAS
from wiki import Wiki
from pymongo import MongoClient
import wikipedia
import json
from bson import json_util
from flask import Flask, render_template, request, redirect, jsonify



class Api:
    wikipedia.set_lang("pt")
    __pesquisa = ""

    def __init__(self, __pesquisa):
        self.setPesquisa(__pesquisa)
        self.wiki = Wiki(__pesquisa)
        self.conexao()

    #   Getters e Setters
    def setPesquisa(self, __pesquisa):
        self.__pesquisa = __pesquisa

    def getPesquisa(self):
        return self.__pesquisa

    def conexao(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.Wikipedia.wiki
        return self.db

    def create(self):
        self.conexao().insert_one(
            {
                "Geral": {
                    "Id": self.wiki.getIdWiki(),
                    "Titulo": self.wiki.getTituloWiki(),
                    "Linguagem": self.wiki.getLinguagemWiki(),
                    "Descricao": self.wiki.getDescricaoWiki(),
                    "Palavras_chave": self.wiki.getPalavraChaveWiki(),
                    "Cobertura": self.wiki.get_coberturaWiki(),
                    "Estrutura": self.wiki.get_estruturaWiki(),
                    "Nivel_de_agregacao": self.wiki.get_nivelDeAgregacaoWiki()
                },
                "Ciclo_de_vida": {
                    "Versao": self.wiki.getVersaoWiki(),
                    "Status": self.wiki.get_statusWiki(),
                    "Contribuinte": {
                        "Entidade": self.wiki.get_entidadeWiki(),
                        "Data": self.wiki.getDateWiki(),
                        "Papel": self.wiki.get_papelWiki(),
                    }
                },
                "Meta_Metadados": {
                    "Identificador": {
                        "Catalogo": self.wiki.getCatalogoWiki(),
                        "Entrada": self.wiki.getEntradaWiki(),
                    },
                    "Contribuintes": {
                        "Entidade": self.wiki.get_entidadeWiki(),
                        "Data": self.wiki.getDateWiki(),
                        "Papel": self.wiki.get_papelWiki(),
                    },
                    "Esquema_de_Metadados": self.wiki.get_esquemaMetadadosWiki(),
                    "Idioma": self.wiki.getLinguagemWiki(),
                },
                "Metadados_Tecnicos": {
                    "Formato": self.wiki.getFormatoWiki(),
                    "Tamanho": self.wiki.getTamanhoWiki(),
                    "Localizacao": self.wiki.getLocalizacaoWiki(),
                    "Requisitos": self.wiki.get_requisitosWiki(),
                    "Observacoes_de_Instalacoes": self.wiki.get_observacoesDeInstalacoesWiki(),
                    "Outros_Requisitos_de_Sistema": self.wiki.get_outrosRequisitosDeSistemaWiki(),
                    "Duracao": self.wiki.getDuracaoWiki(),
                },
                "Aspectos_Educacionais": {
                    "Tipo_de_Interatividade": self.wiki.get_tipoDeInteratividadeWiki(),
                    "Tipo_de_recurso_de_aprendizagem": self.wiki.get_tipoDeRecursoDeAprendizagemWiki(),
                    "Nivel_de_Interatividade": self.wiki.get_nivelDeInteratividadeWiki(),
                    "Densidade_semantica": self.wiki.get_densidadeSemanticaWiki(),
                    "Usuario_final": self.wiki.get_usuarioFinalWiki(),
                    "Contexto_de_aprendizagem": self.wiki.get_contextoDeAprendizagemWiki(),
                    "Idade_recomendada": self.wiki.get_idadeRecomendadaWiki(),
                    "Grau_de_dificuldade": self.wiki.get_grauDeDificuldadeWiki(),
                    "Tempo_de_aprendizagem": self.wiki.get_tempoDeAprendizadoWiki(),
                    "Descricao": self.wiki.get_descricaoAspectosWiki(),
                    "linguagem": self.wiki.getLinguagemWiki()
                },
                "Direitos": {
                    "Custo": self.wiki.get_custosWiki(),
                    "Direitos_autorais": self.wiki.get_direitosAutoraisWiki(),
                    "Descricao": self.wiki.get_descricaoDireitosWiki(),
                },
                "Relacoes": {
                    "Genero": self.wiki.get_generoWiki(),
                    "Recurso": {
                        "Referencias": self.wiki.getReferenciasWiki(),
                        "Links_externos": self.wiki.getLinkExternosWiki()
                    },
                },
                "Classificacao": {
                    "Finalidade": self.wiki.get_finalidadeWiki(),
                    "Diretorio": self.wiki.getDiretorioWiki(),
                    "Descricao": self.wiki.get_descricaoClassWiki(),
                    "Palavra_Chave": self.wiki.get_palavraChaveClassWiki(),
                },
                "Conteudo": {
                    "Data": self.wiki.getDateWiki(),
                    "Entidade": self.wiki.getEntidadeConteudoWiki(),
                    "Imagens": self.wiki.getImagemWiki(),
                    "Anotacao": self.wiki.getAnotacaoWiki(),
                },
            }
        )

    def update(self, editar):
        titulo = {'Geral.Titulo': self.wiki.getTituloWiki()}
        teste = {'$set':
            {
                "Geral": {
                    "Id": editar['idWiki'],
                    "Titulo": editar['tituloWiki'],
                    "Linguagem": editar['linguagemWiki'],
                    "Descricao": editar['descricaoWiki'],
                    "Palavras_chave": editar['palavraChaveWiki'],
                    "Cobertura": editar['coberturaWiki'],
                    "Estrutura": editar['estruturaWiki'],
                    "Nivel_de_agregacao": editar['nivelDeAgregacaoWiki']
                },
                "Ciclo_de_vida": {
                    "Versao": editar['versaoWiki'],
                    "Status": editar['statusWiki'],
                    "Contribuinte": {
                        "Entidade": editar['entidadeWiki'],
                        "Data": editar['dateWiki'],
                        "Papel": editar['papelWiki'],
                    }
                },
                "Meta_Metadados": {
                    "Identificador": {
                        "Catalogo": editar['catalogoWiki'],
                        "Entrada": editar['entradaWiki'],
                    },
                    "Contribuintes": {
                        "Entidade": editar['entidadeWiki'],
                        "Data": editar['dateWiki'],
                        "Papel": editar['papelWiki'],
                    },
                    "Esquema_de_Metadados": editar['esquemaMetadadosWiki'],
                    "Idioma": editar['linguagemWiki'],
                },
                "Metadados_Tecnicos": {
                    "Formato": editar['formatoWiki'],
                    "Tamanho": editar['tamanhoWiki'],
                    "Localizacao": editar['localizacaoWiki'],
                    "Requisitos": editar['requisitosWiki'],
                    "Observacoes_de_Instalacoes": editar['observacoesDeInstalacoesWiki'],
                    "Outros_Requisitos_de_Sistema": editar['outrosRequisitosDeSistemaWiki'],
                    "Duracao": editar['duracaoWiki'],
                },
                "Aspectos_Educacionais": {
                    "Tipo_de_Interatividade": editar['tipoDeInteratividadeWiki'],
                    "Tipo_de_recurso_de_aprendizagem": editar['tipoDeRecursoDeAprendizagemWiki'],
                    "Nivel_de_Interatividade": editar['nivelDeInteratividadeWiki'],
                    "Densidade_semantica": editar['densidadeSemanticaWiki'],
                    "Usuario_final": editar['usuarioFinalWiki'],
                    "Contexto_de_aprendizagem": editar['contextoDeAprendizagemWiki'],
                    "Idade_recomendada": editar['idadeRecomendadaWiki'],
                    "Grau_de_dificuldade": editar['grauDeDificuldadeWiki'],
                    "Tempo_de_aprendizagem": editar['tempoDeAprendizadoWiki'],
                    "Descricao": editar['descricaoAspectosWiki'],
                    "linguagem": editar['linguagemWiki']
                },
                "Direitos": {
                    "Custo": editar['custosWiki'],
                    "Direitos_autorais": editar['direitosAutoraisWiki'],
                    "Descricao": editar['descricaoDireitosWiki'],
                },
                "Relacoes": {
                    "Genero": editar['generoWiki'],
                    "Recurso": {
                        "Referencias": editar['referenciasWiki'],
                        "Links_externos": editar['linkExternosWiki']
                    },
                },
                "Classificacao": {
                    "Finalidade": editar['finalidadeWiki'],
                    "Diretorio": editar['diretorioWiki'],
                    "Descricao": editar['descricaoClassWiki'],
                    "Palavra_Chave": editar['palavraChaveClassWiki'],
                },
                "Conteudo": {
                    "Data": editar['dateWiki'],
                    "Entidade": editar['entidadeConteudoWiki'],
                    "Imagens": editar['imagemWiki'],
                    "Anotacao": editar['anotacaoWiki'],
                },
            }
        }
        self.conexao().update_one(titulo, teste)

    def updateWs(self, dirUm, dirDois, dirTres, editar):
        titulo = {'Geral.Titulo': self.wiki.getTituloWiki()}
        if(dirTres == ''):
            teste = {'$set': {"{}.{}".format(dirUm, dirDois): editar}}
            self.conexao().update_one(titulo, teste)
        else:
            teste = {'$set': {"{}.{}.{}".format(dirUm, dirDois, dirTres): editar}}
            self.conexao().update_one(titulo, teste)

    def delete(self, name):
        self.conexao().delete_one({"Geral.Titulo": name})

    def detalhes(self, name):
        wiki_detalhes = self.conexao().find_one({'Geral.Titulo': name})
        resultado = json.dumps(wiki_detalhes, default=json_util.default)
        if(resultado == "null"):
            return self.readerRest()
        else:
            return resultado

    def reader(self):
        wiki_list = list(self.conexao().find())
        return json.dumps(wiki_list, default=json_util.default)

    def readerDetalhes(self, titulo, dirUm, dirDois, dirTres):
        title = {"Geral.Titulo":titulo}
        if(dirDois == ''):
            pesquisa = {"{}".format(dirUm)}
            wiki_detalhes = self.conexao().find_one(title, pesquisa)
            return json.dumps(wiki_detalhes, default=json_util.default)
        if(dirTres == ''):
            pesquisa = {"{}.{}".format(dirUm, dirDois)}
            wiki_detalhes = self.conexao().find_one(title, pesquisa)
            return json.dumps(wiki_detalhes, default=json_util.default)
        else:
            pesquisa = {"{}.{}.{}".format(dirUm, dirDois, dirTres)}
            wiki_detalhes = self.conexao().find_one(title, pesquisa)
            return json.dumps(wiki_detalhes, default=json_util.default)

    def readerRest(self):
        rest = {
                "Informacoes_retirada":"API do Wikipedia",
                "Geral": {
                    "Id": self.wiki.getIdWiki(),
                    "Titulo": self.wiki.getTituloWiki(),
                    "Linguagem": self.wiki.getLinguagemWiki(),
                    "Descricao": self.wiki.getDescricaoWiki(),
                    "Palavras_chave": self.wiki.getPalavraChaveWiki(),
                    "Cobertura": self.wiki.get_coberturaWiki(),
                    "Estrutura": self.wiki.get_estruturaWiki(),
                    "Nivel_de_agregacao": self.wiki.get_nivelDeAgregacaoWiki()
                },
                "Ciclo_de_vida": {
                    "Versao": self.wiki.getVersaoWiki(),
                    "Status": self.wiki.get_statusWiki(),
                    "Contribuinte": {
                        "Entidade": self.wiki.get_entidadeWiki(),
                        "Data": self.wiki.getDateWiki(),
                        "Papel": self.wiki.get_papelWiki(),
                    }
                },
                "Meta_Metadados": {
                    "Identificador": {
                        "Catalogo": self.wiki.getCatalogoWiki(),
                        "Entrada": self.wiki.getEntradaWiki(),
                    },
                    "Contribuintes": {
                        "Entidade": self.wiki.get_entidadeWiki(),
                        "Data": self.wiki.getDateWiki(),
                        "Papel": self.wiki.get_papelWiki(),
                    },
                    "Esquema_de_Metadados": self.wiki.get_esquemaMetadadosWiki(),
                    "Idioma": self.wiki.getLinguagemWiki(),
                },
                "Metadados_Tecnicos": {
                    "Formato": self.wiki.getFormatoWiki(),
                    "Tamanho": self.wiki.getTamanhoWiki(),
                    "Localizacao": self.wiki.getLocalizacaoWiki(),
                    "Requisitos": self.wiki.get_requisitosWiki(),
                    "Observacoes_de_Instalacoes": self.wiki.get_observacoesDeInstalacoesWiki(),
                    "Outros_Requisitos_de_Sistema": self.wiki.get_outrosRequisitosDeSistemaWiki(),
                    "Duracao": self.wiki.getDuracaoWiki(),
                },
                "Aspectos_Educacionais": {
                    "Tipo_de_Interatividade": self.wiki.get_tipoDeInteratividadeWiki(),
                    "Tipo_de_recurso_de_aprendizagem": self.wiki.get_tipoDeRecursoDeAprendizagemWiki(),
                    "Nivel_de_Interatividade": self.wiki.get_nivelDeInteratividadeWiki(),
                    "Densidade_semantica": self.wiki.get_densidadeSemanticaWiki(),
                    "Usuario_final": self.wiki.get_usuarioFinalWiki(),
                    "Contexto_de_aprendizagem": self.wiki.get_contextoDeAprendizagemWiki(),
                    "Idade_recomendada": self.wiki.get_idadeRecomendadaWiki(),
                    "Grau_de_dificuldade": self.wiki.get_grauDeDificuldadeWiki(),
                    "Tempo_de_aprendizagem": self.wiki.get_tempoDeAprendizadoWiki(),
                    "Descricao": self.wiki.get_descricaoAspectosWiki(),
                    "linguagem": self.wiki.getLinguagemWiki()
                },
                "Direitos": {
                    "Custo": self.wiki.get_custosWiki(),
                    "Direitos_autorais": self.wiki.get_direitosAutoraisWiki(),
                    "Descricao": self.wiki.get_descricaoDireitosWiki(),
                },
                "Relacoes": {
                    "Genero": self.wiki.get_generoWiki(),
                    "Recurso": {
                        "Referencias": self.wiki.getReferenciasWiki(),
                        "Links_externos": self.wiki.getLinkExternosWiki()
                    },
                },
                "Classificacao": {
                    "Finalidade": self.wiki.get_finalidadeWiki(),
                    "Diretorio": self.wiki.getDiretorioWiki(),
                    "Descricao": self.wiki.get_descricaoClassWiki(),
                    "Palavra_Chave": self.wiki.get_palavraChaveClassWiki(),
                },
                "Conteudo": {
                    "Data": self.wiki.getDateWiki(),
                    "Entidade": self.wiki.getEntidadeConteudoWiki(),
                    "Imagens": self.wiki.getImagemWiki(),
                    "Anotacao": self.wiki.getAnotacaoWiki(),
                },
            }
        return json.dumps(rest, default=json_util.default)
