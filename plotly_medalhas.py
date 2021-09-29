import plotly.express as px
import pandas as pd

#leitura dos dados
dados_csv = pd.read_csv("athlete_events.csv") 

#ID[0],"Name"[1],"Sex"[2],"Age"[3],"Height"[4],"Weight"[5],"Team"[6],"NOC"[7],"Games"[8],"Year"[9],"Season"[10],"City"[11],"Sport"[12],"Event"[13],"Medal"[14]

agrupado_por_ano = {}

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

df = {'nome' : [], 'medalhas' : []}  

for nome, medalhas in zip(agrupado_por_ano[ano].keys(), agrupado_por_ano[ano].values()):    
    df['nome'].append(nome)
    df['medalhas'].append(medalhas)

figure = px.bar(
        df,
        title="Olimpíadas - Medalhas por atleta",  
        x= 'nome',
        y= 'medalhas',
         
        
        
        labels={'value':'Quantidades de medalhas', 'variable':'Medalhas', 'nome':'Atletas'}    
    )
figure.show()

















'''
from dash import Dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div(
    children = [
    dcc.Dropdown(
        id = "ano_selecionado",
        options = [{"label": str(ano), "value": ano} for ano in sorted(agrupado_por_ano)],
        value = sorted(agrupado_por_ano)[0],
        style = {"width": "100 px"}
    ),
    dcc.Graph(
        id = "grafico",
        figure = []
        
)])

@app.callback(
    [Output(component_id = "grafico",component_property="figure")],
    [Input(component_id = "ano_selecionado", component_property = "value")]
)

def atualizar_grafico(ano_selecionado):
    copy = agrupado_por_ano[ano_selecionado].copy()

    df = {'nome' : [], 'medalhas' : []}  

    for nome, medalhas in zip(copy.keys(), copy.values()):    
        df['nome'].append(nome)
        df['medalhas'].append(medalhas)
    
    
    figure = px.bar(
            df,
            title="Olimpíadas - Medalhas por atleta",  
            x= 'nome',
            y= 'medalhas', 
            
            
            labels={'value':'Quantidades de medalhas', 'variable':'Medalhas', 'nome':'Atletas'}    
        )
    return figure

app.run_server()
'''