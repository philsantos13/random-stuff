# _*_ coding=utf-8 _*_

## Rodar no Linux! ##

import xmltodict, json
from gzip import GzipFile

def booleano(valor):
    boole = True
    if valor == 0:
        boole = False
    return str(boole)

def regiao(cidade,estado):
    reg = 'None'
    if estado == 'AL':
        if cidade in ["ARAPIRACA","CAMPO GRANDE","COITE DO NOIA","CRAIBAS","FEIRA GRANDE","GIRAU DO PONCIANO","LAGOA DA CANOA","LIMOEIRO DE ANADIA","OLHO D AGUA GRANDE","SAO SEBASTIAO","TAQUARANA","TRAIPU","SAO BRAS","JARAMATAIA"]:
            reg = "RMAGRESTEAL"
        elif cidade in ["MACEIO","RIO LARGO","MARECHAL DEODORO","PILAR","SAO MIGUEL DOS CAMPOS","BARRA DE SAO MIGUEL","BARRA DE SANTO ANTONIO","MESSIAS","SATUBA","COQUEIRO SECO","SANTA LUZIA DO NORTE","PARIPUEIRA","MURICI"]:
            reg = "RMMACEIOAL"
        elif cidade in ["SANTANA DO IPANEMA","DOIS RIACHOS","OLIVENCA","OLHO D AGUA DAS FLORES","CARNEIROS","SENADOR RUI PALMEIRA","POCO DAS TRINCHEIRAS","MARAVILHA","OURO BRANCO"]:
            reg = "RMMEDIOSERTAOAL"
        elif cidade in ["BELEM","CACIMBINHAS","ESTRELA DE ALAGOAS","IGACI","MAJOR ISIDORO","MINADOR DO NEGRAO","PALMEIRA DOS INDIOS"]:
            reg = "RMPALMEIRADOSINDIOSAL"
        elif cidade in ["ATALAIA","CAPELA","CAJUEIRO","VICOSA","MAR VERMELHO","CHA PRETA","PAULO JACINTO","QUEBRANGULO","MARIBONDO","ANADIA","BOCA DA MATA","TANQUE D ARCA","PINDOBA"]:
            reg = "RMVALEDOPARAIBAAL"
        elif cidade in ["BRANQUINHA","CAMPESTRE","COLONIA LEOPOLDINA","FLEXEIRAS","IBATEGUARA","JACUIPE","JOAQUIM GOMES","JUNDIA","MATRIZ DO CAMARAGIBE","NOVO LINO","PORTO CALVO","SANTANA DO MUNDAU","SAO JOSE DA LAJE","SAO LUIS DO QUITUNDE","UNIAO DOS PALMARES"]:
            reg = "RMZONADAMATAAL"
    elif estado == 'BA':
        if cidade in ["AMELIA RODRIGUES","CONCEICAO DA FEIRA","CONCEICAO DO JACUIPE","FEIRA DE SANTANA","SAO GONCALO DOS CAMPOS E TANQUINHO","ANGUERA","ANTONIO CARDOSO","CANDEAL","CORACAO DE MARIA","IPECAETA","IRARA","RIACHAO DO JACUIPE","SANTA BARBARA","SANTANOPOLIS","SERRA PRETA"]:
            reg = "RMFEIRADESANTANABA"
        elif cidade in ["CAMACARI","CANDEIAS","DIAS D AVILA","ITAPARICA","LAURO DE FREITAS","MADRE DE DEUS","MATA DE SAO JOAO","POJUCA","SALVADOR","SAO FRANCISCO DO CONDE","SAO SEBASTIAO DO PASSE","SIMOES FILHO","VERA CRUZ"]:
            reg = "RMSALVADORBA"
    elif estado == 'CE':
        if cidade in ["JUAZEIRO DO NORTE","CRATO","BARBALHA","CARIRIACU","FARIAS BRITO","JARDIM","MISSAO VELHA","NOVA OLINDA","SANTANA DO CARIRI"]:
            reg = "RMCARIRICE"
        elif cidade in ["FORTALEZA","CAUCAIA","MARANGUAPE","PACATUBA","AQUIRAZ","MARACANAU","EUSEBIO","ITAITINGA","GUAIUBA","CHOROZINHO","PACAJUS","HORIZONTE","SAO GONCALO DO AMARANTE","PINDORETAMA","CASCAVEL","PARACURU","PARAIPABA","TRAIRI","SAO LUIS DO CURU"]:
            reg = "RMFORTALEZACE"
        elif cidade in ["MASSAPE","SENADOR SA","URUOCA","SANTANA DO ACARAU","FORQUILHA","COREAU","MORAUJO","GROAIRAS","RERIUTABA","VARJOTA","CARIRE","PACUJA","GRACA","FRECHEIRINHA","MIRAIMA","MERUOCA","ALCANTARAS","SOBRAL"]:
            reg = "RMSOBRALCE"
    elif estado == 'MA':
        if cidade in ["SAO JOSE DE RIBAMAR","RAPOSA","PACO DO LUMIAR","ALCANTARA","BACABEIRA","SAO LUIS","ROSARIO","SANTA RITA"]:
            reg = "RMSAOLUISMA"
        elif cidade in ["IMPERATRIZ","JOAO LISBOA","SENADOR LA ROCQUE","BURITIRANA","DAVINOPOLIS","GOVERNADOR EDISON LOBAO","MONTES ALTOS","RIBAMAR FIQUENE"]:
            reg = "RMSUDOESTEMARANHANSEMA"
    elif estado == 'PB':
        if cidade in ["ARARUNA","CACIMBA DE DENTRO","DAMIAO","DONA INES","RIACHAO","TACIMA"]:
            reg = "RMARARUNAPB"
        elif cidade in ["BARAUNA","BARRA DE SANTA ROSA","CUITE","FREI MARTINHO","NOVA FLORESTA","NOVA PALMEIRA","PICUI","SOSSEGO"]:
            reg = "RMBARRADESANTAROSAPB"
        elif cidade in ["BERNARDINO BATISTA","BOM JESUS","BONITO DE SANTA FE","CACHOEIRA DOS INDIOS","CAJAZEIRAS","CARRAPATEIRA","JOCA CLAUDINO (SANTAREM)","MONTE HOREBE","POCO DANTAS","POCO DE JOSE DE MOURA","SANTA HELENA","SAO JOAO DO RIO DO PEIXE","SAO JOSE DE PIRANHAS","TRIUNFO","UIRAUNA"]:
            reg = "RMCAJAZEIRASPB"
        elif cidade in ["ALAGOA NOVA","AREIAL","AROEIRAS","BARRA DE SANTANA","BOA VISTA","BOQUEIRAO","CAMPINA GRANDE","CATURITE","ESPERANCA","FAGUNDES","GADO BRAVO","INGA","ITATUBA","LAGOA SECA","MASSARANDUBA","MATINHAS","MONTADAS","POCO REDONDO","PUXINANA","QUEIMADAS","RIACHAO DO BACAMARTE","SAO SEBASTIAO DE LAGOA DE ROCA","SERRA REDONDA","ALCANTIL","NATUBA","SANTA CECILIA","UMBUZEIRO"]:
            reg = "RMCAMPINAGRANDEPB"
        elif cidade in ["ALAGOA NOVA","ALGODAO DE JANDAIRA","AREIA","AREIAL","ESPERANCA","MONTADAS","POCINHOS","REMIGIO","SAO SEBASTIAO DE LAGOA DE ROCA"]:
            reg = "RMESPERANCAPB"
        elif cidade in ["ALAGOINHA","ARACAGI","ARARA","BANANEIRAS","BELEM","BORBOREMA","CAICARA","CUITEGI","DUAS ESTRADAS","GUARABIRA","LAGOA DE DENTRO","LOGRADOURO","MULUNGU","PILOES","PILOEZINHOS","PIRPIRITUBA","SERRA DA RAIZ","SERRARIA","SERTAOZINHO","SOLANEA"]:
            reg = "RMGUARABIRAPB"
        elif cidade in ["CALDAS BRANDAO","GURINHEM","INGA","ITABAIANA","JUAREZ TAVORA","JURIPIRANGA","MOGEIRO","PILAR","RIACHAO DO BACAMARTE","SALGADO DE SAO FELIX","SAO JOSE DOS RAMOS","SAO MIGUEL DE TAIPU"]:
            reg = "RMITABAIANAPB"
        elif cidade in ["BAYEUX","CABEDELO","CONDE","CRUZ DO ESPIRITO SANTO","JOAO PESSOA","LUCENA","RIO TINTO","SANTA RITA","ALHANDRA","PITIMBU","CAAPORA","PEDRAS DE FOGO"]:
            reg = "RMJOAOPESSOAPB"
        elif cidade in ["PATOS","QUIXABA","PASSAGEM","AREIA DE BARAUNAS","SALGADINHO","JUNCO DO SERIDO","SANTA LUZIA","SAO JOSE DO SABUGI","VARZEA","SAO MAMEDE","CACIMBA DE AREIA","CACIMBAS","DESTERRO","TEIXEIRA","SAO JOSE DO BONFIM","MATUREIA","MAE D AGUA","SANTA TERESINHA","CATINGUEIRA","EMAS","MALTA","CONDADO","SAO JOSE DE ESPINHARAS","VISTA SERRANA"]:
            reg = "RMPATOSPB"
        elif cidade in ["APARECIDA","LASTRO","MARIZOPOLIS","NAZAREZINHO","SANTA CRUZ","SAO FRANCISCO","SAO JOSE DA LAGOA TAPADA","SOUSA","VIEIROPOLIS"]:
            reg = "RMSOUSAPB"
        elif cidade in ["BAIA DA TRAICAO","CUITE DE MAMANGUAPE","CURRAL DE CIMA","ITAPOROROCA","JACARAU","MAMANGUAPE","MARCACAO","MATARACA","PEDRO REGIS"]:
            reg = "RMVALEDOMAMANGUAPEPB"
        elif cidade in ["AGUIAR","BOA VENTURA","CONCEICAO","COREMAS","CURRAL VELHO","DIAMANTE","IBIARA","IGARACY","ITAPORANGA","NOVA OLINDA","OLHO D AGUA","PEDRA BRANCA","PIANCO","SANTA INES","SANTANA DE MANGUEIRA","SANTANA DOS GARROTES","SAO JOSE DE CAIANA","SERRA GRANDE"]:
            reg = "RMVALEDOPIANCOPB"
    elif estado == 'PE':
        if cidade in ["JABOATAO DOS GUARARAPES","OLINDA","PAULISTA","IGARASSU","ABREU E LIMA","CAMARAGIBE","CABO DE SANTO AGOSTINHO","SAO LOURENCO DA MATA","ARACOIABA","ILHA DE ITAMARACA","IPOJUCA","MORENO","ITAPISSUMA","RECIFE"]:
            reg = "RMRECIFEPE"
    elif estado == 'RN':
        if cidade in ["ARES","CEARA-MIRIM","EXTREMOZ","GOIANINHA","IELMO MARINHO","MACAIBA","MAXARANGUAPE","MONTE ALEGRE","NATAL","NISIA FLORESTA","PARNAMIRIM","SAO GONCALO DO AMARANTE","SAO JOSE DE MIPIBU","VERA CRUZ"]:
            reg = "RMNATALRN"
    elif estado == 'SE':
        if cidade in ["ARACAJU","BARRA DOS COQUEIROS","NOSSA SENHORA DO SOCORRO","SAO CRISTOVAO"]:
            reg = "RMARACAJUSE"
    else:
        reg = 'None'
    return reg

def faixa(valor,div):
    n1 = int(valor/div)
    n2 = n1*div
    nd = 0 
    st = ''
    cl = div*10
    if div > 1:
        nd = n2+div-1
        if n2 < cl:
            st = str(n2)+'-'+str(nd)
        else:
            st = "\'acima de "+str(cl)+"\'"
    else:
        nd = n2+div
        st = str(n2)+'-'+str(nd)
    return st

def nota(n):
    st = ''
    nt = int(n)
    if nt < 300:
        st = 'None'
    else:
        n1 = int((nt-300)/100)
        n2 = n1*100
        n2 += 300
        st = str(n2)+'-'+str(n2+99)
    return st

def transforma(v,i):
    ret = ''
    if i == 32:
        if v == 1:
            ret = 'Federal'
        elif v == 2:
            ret = 'Estadual'
        elif v == 3:
            ret = 'Municipal'
        elif v == 4:
            ret = 'Privada'
    elif i == 96:
        if v == 0:
            ret = 'Sim'
        elif v == 1:
            ret = 'Não'
        elif v == 2:
            ret = '\'Em tramitação\''
    elif i == 110:
        if v == 1:
            ret = '\'Em atividade\''
        elif v == 2:
            ret = 'Paralisada'
        elif v == 3:
            ret = 'Extinta'
        elif v == 4:
            ret = '\'Extinta no ano anterior\''
    elif i == 112:
        if v == 1:
            ret = 'Urbana'
        elif v == 2:
            ret = 'Rural'
    return ret


def handle(a,what):
    dump = json.dumps(what)
    doc = json.loads(dump)
    if type(doc)!=str:
        # evitando o cabeçalho do gzip
        linha = doc['Cell']
        if linha[0]['Data']['#text'] != "cod":
            # evitando a primeira linha de dados, que só faz referência aos atributos de escola
            arff = open('escolas-nordeste-enem-2013-1.arff','a')
            if linha[118]['Data']['#text'] == '0' or linha[118]['Data']['#text'] == 0:
                pass # se não houver nota do enem, "pega o beco". próxima linha!
            else:
                i = 1 #ja começa ignorando cod. porque pra esse trabalho se mostrou inútil.
                while i < len(linha):
                    # alguns dados são ignorados. 
                    # edit: retirei região (só tem NE mesmo); adicionados nota objetiva e nota da redação.
                    # há uns critérios do MEC acerca de não usar só média geral.
                    if i in range(23,26) or i in range(114,118) or i==60  or i==65 or i==76 or i==77 or i==95 or i==120 or i ==121 or i in range(125,128):
                        pass
                    elif i==78:
                        arff.write('\"'+str(linha[i]['Data']['#text'])+'\",') # insere a cidade
                        data = regiao(str(linha[i]['Data']['#text']),str(linha[108]['Data']['#text'])) # funcao de regiao metropolitana
                        arff.write(data+',') # insere a região metropolitana (se tiver; se não, vai None)
                    else:
                        dado = linha[i]['Data']
                        try:
                            if dado['@ss:Type']=='String':
                                # se o dado já vier como string, apenas adicione aspas, e vai como tá
                                arff.write('\"'+str(dado['#text'])+'\"')
                            else:
                                # se o dado for booleano (0,1), vira {True,False}
                                if i in range(1,12) or i in range(14,23) or i==30 or i in range(33,35) or i in range(36,60) or i==61 or i in range(66,76) or i in range(79,95) or i in range(98,101) or i in range(103,108):
                                    data = booleano(int(dado['#text']))
                                    arff.write(data)
                                # transforma o dado em faixas de 10: {0-9,10-19,20-29...}
                                elif i == 111 or i == 64 or i == 31 or i == 27 or i == 28 or i == 123:
                                    data = faixa(int(float(dado['#text'])),10)
                                    arff.write(data)
                                # transforma o dado em faixas de 5
                                elif i == 113 or i == 35 or i == 29 or i == 97 or i == 13 or i == 62:
                                    data = faixa(int(dado['#text']),5)
                                    arff.write(data)
                                # transforma o dado em faixas de 20
                                elif i == 26 or i == 63:
                                    data = faixa(int(dado['#text']),20)
                                    arff.write(data)
                                # transforma o dado em faixas de 15
                                elif i == 102 or i == 101:
                                    data = faixa(int(dado['#text']),15)
                                    arff.write(data)
                                # transforma a nota do enem em faixas de 100: {300-399,400-499 etc}
                                elif i == 118 or i == 119 or i == 122:
                                    data = nota(float(dado['#text']))
                                    arff.write(data)
                                # casos específicos de transformação
                                elif i == 32 or i == 96 or i == 110 or i == 112:
                                    data = transforma((int(dado['#text'])),i)
                                    arff.write(data)
                                # se nada cair nas categorias acima, o dado vai como está.
                                else:
                                    arff.write(str(dado['#text']))
                                
                        except:
                            arff.write('None')
                        if i < (len(linha))-4: # está -4 porque os últimos 3 itens estão comentados no arff.
                            arff.write(',')
                    i+=1
                arff.write('\n')
            arff.close()
        else:
            pass
    else:
        pass
    return True

dic = xmltodict.parse(GzipFile('EscolasNordeste.xml.gz'),item_depth=4,item_callback=handle)

print('done')
