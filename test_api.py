import sqlite3
import json
from flask.testing import FlaskClient
from api import perform_etl, WeatherData, app, db

def testar_conexao_com_db():
    with app.app_context():
        conn = sqlite3.connect('etl_database.db')
        assert conn is not None
        assert isinstance(conn, sqlite3.Connection)
        conn.close()

def testar_conteudo_da_tabela():
    with app.app_context():
        tabela = WeatherData.query.all()
        print("Conteúdo da tabela:", tabela)
        assert len(tabela) > 0
        
def testar_resposta_html():
    with app.test_client() as client: 
        resposta = client.get('/weather_data')
        assert resposta.status_code == 200
        assert resposta.content_type == 'text/html; charset=utf-8'
        assert b'Ingestion Date' in resposta.data
        assert b'Data Type' in resposta.data
        assert b'Values' in resposta.data
        assert b'Usage' in resposta.data

def testar_rotas_existentes():
    with app.test_client() as client:
        assert '/' in [rule.rule for rule in app.url_map.iter_rules()]
        assert '/weather_data' in [rule.rule for rule in app.url_map.iter_rules()]

if __name__ == '__main__':
    testar_conexao_com_db()
    testar_conteudo_da_tabela()
    testar_resposta_html()
    testar_rotas_existentes()
    print("Todos os testes passaram!")
