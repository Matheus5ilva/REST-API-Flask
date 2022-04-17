#IPORTACAO DAS BIBLIOTECAS USADAS
import wikipedia
import wikipediaapi
from mediawiki import MediaWiki
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from datetime import date
import re
import sys

class Wiki:
    # COLOCANDO PESQUISAS DO WIKIPEDIA EM PORTUGUES
    wikipedia.set_lang("pt")

    __pesquisa = ""
    __idWiki = ""
    __tituloWiki = ""
    __linguagemWiki = ""
    __descricaoWiki = ""
    __palavraChaveWiki = ""
    __coberturaWiki = ""
    __estruturaWiki = ""
    __nivelDeAgregacaoWiki = ""
    __versaoWiki = ""
    __statusWiki = ""
    __entidadeWiki = ""
    __papelWiki = ""
    __catalogoWiki = ""
    __entradaWiki = ""
    __dateWiki = ""
    __esquemaMetadadosWiki = ""
    __formatoWiki = ""
    __tamanhoWiki = ""
    __localizacaoWiki = ""
    __requisitosWiki = ""
    __observacoesDeInstalacoesWiki = ""
    __outrosRequisitosDeSistemaWiki = ""
    __duracaoWiki = ""
    __tipoDeInteratividadeWiki = ""
    __tipoDeRecursoDeAprendizagemWiki = ""
    __nivelDeInteratividadeWiki = ""
    __densidadeSemanticaWiki = ""
    __usuarioFinalWiki = ""
    __contextoDeAprendizagemWiki = ""
    __idadeRecomendadaWiki = ""
    __grauDeDificuldadeWiki = ""
    __descricaoMetaWiki = ""
    __custosWiki = ""
    __direitosAutoraisWiki = ""
    __generoWiki = ""
    __referenciasWiki = ""
    __linkExternosWiki = ""
    __finalidadeWiki = ""
    __diretorioWiki = ""
    __descricaoClassWiki = ""
    __palavraChaveClassWiki = ""
    __entidadeConteudoWiki = ""
    __imagemWiki = ""
    __anotacaoWiki = ""
    __tempoDeAprendizadoWiki = ""
    __descricaoAspectosWiki = ""
    __descricaoDireitosWiki = ""

    def __init__(self, __pesquisa):
        self.setPesquisa(__pesquisa)

    def apiWiki(self):
        return wikipedia.page(self.getPesquisa())

    def apiWikiApi(self):
        wiki_wiki = wikipediaapi.Wikipedia(
            language='pt',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )
        return wiki_wiki.page(self.getPesquisa())

    def apiMediaWiki(self):
        media_wiki = MediaWiki(lang='pt')
        return media_wiki.page(self.getPesquisa())

    def qtd_palavras_wiki(self, text):
        texto_minerado = nltk.word_tokenize(text, "portuguese")
        vectorizer = CountVectorizer()
        vectorizer.fit_transform(texto_minerado).todense()
        return len(vectorizer.vocabulary_)

    #Getters e Setters

    def setPesquisa(self, __pesquisa):
        self.__pesquisa = __pesquisa

    def getPesquisa(self):
        return self.__pesquisa

    def setIdWiki(self, __idWiki):
        self.__idWiki = __idWiki

    def getIdWiki(self):
        self.__idWiki = self.apiWiki()
        return self.__idWiki.pageid

    def get_idWiki(self):
        return self.__idWiki

    def setTituloWiki(self, __tituloWiki):
        self.__tituloWiki = __tituloWiki

    def getTituloWiki(self):
        self.__tituloWiki = self.apiWiki()
        return self.__tituloWiki.title

    def get_tituloWiki(self):
        return self.__tituloWiki

    def setLinguagemWiki(self, __linguagemWiki):
        self.__linguagemWiki = __linguagemWiki

    def getLinguagemWiki(self):
        self.__linguagemWiki = wikipedia.languages()['pt']
        return self.__linguagemWiki

    def get_linguagemWiki(self):
        return self.__linguagemWiki

    def setDescricaoWiki(self, __descricaoWiki):
        self.__descricaoWiki = __descricaoWiki

    def getDescricaoWiki(self):
        self.__descricaoWiki = self.apiWiki()
        return self.__descricaoWiki.summary

    def get_descricaoWiki(self):
        return self.__descricaoWiki

    def setPalavraChaveWiki(self, __palavraChaveWiki):
        self.__palavraChaveWiki = __palavraChaveWiki

    def getPalavraChaveWiki(self):
        self.__palavraChaveWiki = self.apiWikiApi()
        return self.__palavraChaveWiki.title.split()

    def get_palavraChaveWiki(self):
        return self.__palavraChaveWiki

    def setCoberturaWiki(self, __coberturaWiki):
        self.__coberturaWiki = __coberturaWiki

    def get_coberturaWiki(self):
        return self.__coberturaWiki

    def setEstruturaWiki(self, __estruturaWiki):
        self.__estruturaWiki = __estruturaWiki

    def get_estruturaWiki(self):
        return self.__estruturaWiki

    def setNivelDeAgregacaoWiki(self, __nivelDeAgregacaoWiki):
        self.__nivelDeAgregacaoWiki = __nivelDeAgregacaoWiki

    def get_nivelDeAgregacaoWiki(self):
        return self.__nivelDeAgregacaoWiki

    def setVersaoWiki(self, __versaoWiki):
        self.__versaoWiki = __versaoWiki

    def getVersaoWiki(self):
        self.__versaoWiki = self.apiWiki()
        return self.__versaoWiki.revision_id

    def get_versaoWiki(self):
        return self.__versaoWiki

    def setStatusWiki(self, __statusWiki):
        self.__statusWiki = __statusWiki

    def get_statusWiki(self):
        return self.__statusWiki

    def setEntidadeWiki(self, __entidadeWiki):
        self.__entidadeWiki = __entidadeWiki

    def get_entidadeWiki(self):
        return self.__entidadeWiki

    def setPapelWiki(self, __papelWiki):
        self.__papelWiki = __papelWiki

    def get_papelWiki(self):
        return self.__papelWiki

    def setCatalogoWiki(self, __catalogoWiki):
        self.__catalogoWiki = __catalogoWiki

    def getCatalogoWiki(self):
        self.__catalogoWiki = self.apiWiki()
        return self.__catalogoWiki.categories

    def get_catalogoWiki(self):
        return self.__catalogoWiki

    def setEntradaWiki(self, __entradaWiki):
        self.__entradaWiki = __entradaWiki

    def getEntradaWiki(self):
        self.__entradaWiki = self.apiWiki()
        return self.__entradaWiki.pageid

    def get_entradaWiki(self):
        return self.__entradaWiki

    def setDateWiki(self, __dateWiki):
        self.__dateWiki = __dateWiki

    def getDateWiki(self):
        self.__dateWiki = date.today().strftime('%d/%m/%Y')
        return self.__dateWiki

    def get_dateWiki(self):
        return self.__dateWiki

    def setEsquemaMetadadosWiki(self, __esquemaMetadadosWiki):
        self.__esquemaMetadadosWiki = __esquemaMetadadosWiki

    def get_esquemaMetadadosWiki(self):
        return self.__esquemaMetadadosWiki

    def setFormatoWiki(self, __formatoWiki):
        self.__formatoWiki = __formatoWiki

    def getFormatoWiki(self):
        self.__formatoWiki = self.apiWikiApi()
        return self.__formatoWiki.contentmodel

    def get_formatoWiki(self):
        return self.__formatoWiki

    def setTamanhoWiki(self, __tamanhoWiki):
        self.__tamanhoWiki = __tamanhoWiki

    def getTamanhoWiki(self):
        teste = self.apiWikiApi().text
        self.__tamanhoWiki = self.qtd_palavras_wiki(teste)
        return self.__tamanhoWiki

    def get_tamanhoWiki(self):
        return self.__tamanhoWiki

    def setLocalizacaoWiki(self, __localizacaoWiki):
        self.__localizacaoWiki = __localizacaoWiki

    def getLocalizacaoWiki(self):
        self.__localizacaoWiki = self.apiWiki()
        return self.__localizacaoWiki.url

    def get_localizacaoWiki(self):
        return self.__localizacaoWiki

    def setRequisitosWiki(self, __requisitosWiki):
        self.__requisitosWiki = __requisitosWiki

    def get_requisitosWiki(self):
        return self.__requisitosWiki

    def setObservacoesDeInstalacoesWiki(self, __observacoesDeInstalacoesWiki):
        self.__observacoesDeInstalacoesWiki = __observacoesDeInstalacoesWiki

    def get_observacoesDeInstalacoesWiki(self):
        return self.__observacoesDeInstalacoesWiki

    def setOutrosRequisitosDeSistemaWiki(self, __outrosRequisitosDeSistemaWiki):
        self.__outrosRequisitosDeSistemaWiki = __outrosRequisitosDeSistemaWiki

    def get_outrosRequisitosDeSistemaWiki(self):
        return self.__outrosRequisitosDeSistemaWiki

    def setDuracaoWiki(self, __duracaoWiki):
        self.__duracaoWiki = __duracaoWiki

    def getDuracaoWiki(self):
        self.__DuracaoWiki = (self.__tamanhoWiki/100)
        return self.__DuracaoWiki

    def get_duracaoWiki(self):
        return self.__DuracaoWiki

    def setTipoDeInteratividadeWiki(self, __tipoDeInteratividadeWiki):
        self.__tipoDeInteratividadeWiki = __tipoDeInteratividadeWiki

    def get_tipoDeInteratividadeWiki(self):
        return self.__tipoDeInteratividadeWiki

    def setTipoDeRecursoDeAprendizagemWiki(self, __tipoDeRecursoDeAprendizagemWiki):
        self.__tipoDeRecursoDeAprendizagemWiki = __tipoDeRecursoDeAprendizagemWiki

    def get_tipoDeRecursoDeAprendizagemWiki(self):
        return self.__tipoDeRecursoDeAprendizagemWiki

    def setNivelDeInteratividadeWiki(self, __nivelDeInteratividadeWiki):
        self.__nivelDeInteratividadeWiki = __nivelDeInteratividadeWiki

    def get_nivelDeInteratividadeWiki(self):
        return self.__nivelDeInteratividadeWiki

    def setDensidadeSemanticaWiki(self, __densidadeSemanticaWiki):
        self.__densidadeSemanticaWiki = __densidadeSemanticaWiki

    def get_densidadeSemanticaWiki(self):
        return self.__densidadeSemanticaWiki

    def setUsuarioFinalWiki(self, __usuarioFinalWiki):
        self.__usuarioFinalWiki = __usuarioFinalWiki

    def get_usuarioFinalWiki(self):
        return self.__densidadeSemanticaWiki

    def setContextoDeAprendizagemWiki(self, __contextoDeAprendizagemWiki):
        self.__contextoDeAprendizagemWiki = __contextoDeAprendizagemWiki

    def get_contextoDeAprendizagemWiki(self):
        return self.__contextoDeAprendizagemWiki

    def setIdadeRecomendadaWiki(self, __idadeRecomendadaWiki):
        self.__idadeRecomendadaWiki = __idadeRecomendadaWiki

    def get_idadeRecomendadaWiki(self):
        return self.__idadeRecomendadaWiki

    def setGrauDeDificuldadeWiki(self, __grauDeDificuldadeWiki):
        self.__grauDeDificuldadeWiki = __grauDeDificuldadeWiki

    def get_grauDeDificuldadeWiki(self):
        return self.__grauDeDificuldadeWiki

    def setDescricaoMetaWiki(self, __descricaoMetaWiki):
        self.__descricaoMetaWiki = __descricaoMetaWiki

    def get_descricaoMetaWiki(self):
        return self.__descricaoMetaWiki

    def setCustosWiki(self, __custosWiki):
        self.__custosWiki = __custosWiki

    def get_custosWiki(self):
        return self.__custosWiki

    def setDireitosAutoraisWiki(self, __direitosAutoraisWiki):
        self.__direitosAutoraisWiki = __direitosAutoraisWiki

    def get_direitosAutoraisWiki(self):
        return self.__direitosAutoraisWiki

    def setGeneroWiki(self, __generoWiki):
        self.__generoWiki = __generoWiki

    def get_generoWiki(self):
        return self.__generoWiki

    def setReferenciasWiki(self, __referenciasWiki):
        self.__referenciasWiki = __referenciasWiki

    def getReferenciasWiki(self):
        self.__referenciasWiki = self.apiWiki()
        return self.__referenciasWiki.references

    def get_referenciasWiki(self):
        return self.__referenciasWiki

    def setLinkExternosWiki(self, __linkExternosWiki):
        self.__linkExternosWiki = __linkExternosWiki

    def getLinkExternosWiki(self):
        self.__linkExternosWiki = self.apiWiki()
        return self.__linkExternosWiki.links

    def get_linkExternosWiki(self):
        return self.__linkExternosWiki

    def setFinalidadeWiki(self, __finalidadeWiki):
        self.__finalidadeWiki = __finalidadeWiki

    def get_finalidadeWiki(self):
        return self.__finalidadeWiki

    def setDiretorioWiki(self, __diretorioWiki):
        self.__diretorioWiki = __diretorioWiki

    def getDiretorioWiki(self):
        self.__diretorioWiki = self.apiWiki()
        return self.__diretorioWiki.url

    def get_diretorioWiki(self):
        return self.__diretorioWiki

    def setDescricaoClassWiki(self, __descricaoClassWiki):
        self.__descricaoClassWiki = __descricaoClassWiki

    def get_descricaoClassWiki(self):
        return self.__descricaoClassWiki

    def setPalavraChaveClassWiki(self, __palavraChaveClassWiki):
        self.__palavraChaveClassWiki = __palavraChaveClassWiki

    def get_palavraChaveClassWiki(self):
        return self.__palavraChaveClassWiki

    def setEntidadeConteudoWiki(self, __entidadeConteudoWiki):
        self.__entidadeConteudoWiki = __entidadeConteudoWiki

    def getEntidadeConteudoWiki(self):
        self.__entidadeConteudoWiki = self.apiWiki()
        return " ".join(re.split(r"\n+", self.__entidadeConteudoWiki.content))

    def get_entidadeConteudoWiki(self):
        return self.__entidadeConteudoWiki

    def setImagemWiki(self, __imagemWiki):
        self.__imagemWiki = __imagemWiki

    def getImagemWiki(self):
        self.__imagemWiki = self.apiWiki()
        return self.__imagemWiki.images

    def get_imagemWiki(self):
        return self.__imagemWiki

    def setAnotacaoWiki(self, __anotacaoWiki):
        self.__anotacaoWiki = __anotacaoWiki

    def getAnotacaoWiki(self):
        self.__anotacaoWiki = self.apiMediaWiki()
        return self.__anotacaoWiki.hatnotes

    def get_anotacaoWiki(self):
        return self.__anotacaoWiki

    def setTempoDeAprendizadoWiki(self, __tempoDeAprendizadoWiki):
        self.__tempoDeAprendizadoWiki = __tempoDeAprendizadoWiki

    def get_tempoDeAprendizadoWiki(self):
        return self.__tempoDeAprendizadoWiki

    def setDescricaoAspectosWiki(self, __descricaoAspectosWiki):
        self.__descricaoAspectosWiki = __descricaoAspectosWiki

    def get_descricaoAspectosWiki(self):
        return self.__descricaoAspectosWiki

    def setDescricaoDireitosWiki(self, __descricaoDireitosWiki):
        self.__descricaoDireitosWiki = __descricaoDireitosWiki

    def get_descricaoDireitosWiki(self):
        return self.__descricaoDireitosWiki
