import plotly.express as px
import pandas as pd
from dash import Dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Leitura dos dados
dados_csv = pd.read_csv("athlete_events.csv")

#ID[0],"Name"[1],"Sex"[2],"Age"[3],"Height"[4],"Weight"[5],"Team"[6],
# "NOC"[7],"Games"[8],"Year"[9],"Season"[10],"City"[11],"Sport"[12],
# "Event"[13],"Medal"[14]

agrupado_por_ano = {}

# Monta um dicionário a partir dos anos como chaves, e dentro de cada 
# ano existe outro dicionário que contém o nome dos atletas como chaves 
# e um dicionário com as medalhas como valores. 

'''Apagar depois!

 Ex: agrupado_por_ano = {2016: {'Michael Fred Phelps':{'Gold': 5, 'Silver': 1, 'Bronze':0 },
                               'Ding Ning': {'Gold': 4, 'Silver': 1, 'Bronze':0 }
                               }
                        }
'''

for linha in dados_csv.values:  
    if type(linha[14]) != str:
        continue
    nome= linha[1]
    ano= linha[9]
    medalha= linha[14]
    
    if agrupado_por_ano.get(ano) == None:
        agrupado_por_ano[ano] = {}
    if agrupado_por_ano[ano].get(nome) == None:
        agrupado_por_ano[ano][nome] = {'Gold': 0, 'Silver': 0, 'Bronze':0 }

    agrupado_por_ano[ano][nome][medalha]+=1 

#Lista dos nomes em ordem decrescente
anos_ordenados = sorted(agrupado_por_ano, reverse = True) 


app = Dash(__name__)

app.layout = html.Div(
    children = [
    dcc.Dropdown(
        id = "ano_selecionado",
        options = [{"label": str(ano), "value": ano} for ano in anos_ordenados],
        value = anos_ordenados[0],
        style = {"width": "100px"}
    ),
    dcc.Graph(
        id = "grafico",
        figure = [],
        style = {'height' : '70vh','width': '100%'}        
)])

@app.callback(
    Output(component_id = "grafico", component_property="figure"),
    [Input(component_id = "ano_selecionado", component_property = "value")]
)


def atualizar_grafico(ano_selecionado):
    copy = agrupado_por_ano[ano_selecionado].copy()

    # Ordenação dos atletas pelas medalhas por peso: 'Gold', 'Silver' e 'Bronze'.

    copy = dict(sorted(copy.items(), key  = lambda item: (item[1]['Gold'], item[1]['Silver'], item[1]['Bronze']),reverse=True))

    df = {'nome' : [], 'Gold' : [],'Silver':[],'Bronze':[]}  

    for nome, medalhas in zip(copy.keys(), copy.values()):    
        df['nome'].append(nome)
        df['Gold'].append(medalhas['Gold'])
        df['Silver'].append(medalhas['Silver'])
        df['Bronze'].append(medalhas['Bronze'])

    figure = px.bar(
            df,
            title="Olimpíadas - Medalhas por atleta",  
            x= 'nome'[:100],
            y= ['Gold','Silver','Bronze'][:100], 
            color_discrete_map={'Gold':'gold','Silver':'silver', 'Bronze':'rgb(148,93,65)'},                    
            labels={'value':'Quantidade de medalhas', 'variable':'Medalhas', 'nome':'Atletas'}    
        )
    return figure
    

app.run_server()

