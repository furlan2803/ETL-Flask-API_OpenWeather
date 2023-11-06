from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime
import json
import pytz

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///etl_database.db'
db = SQLAlchemy(app)

brasil_timezone = pytz.timezone('America/Sao_Paulo')

def get_brasil_datetime():
    return datetime.now(brasil_timezone)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingestion_date = db.Column(db.DateTime, default=get_brasil_datetime)
    data_type = db.Column(db.String(50))
    values = db.Column(db.String(100))
    usage = db.Column(db.String(100))


def perform_etl():
    
    api_key = '402d6b30685d4ddcf2b466aa8f35c18b'
    cities = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador', 'Recife', 'Fortaleza']
    
    weather_data_list = []  
    
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            
            weather_data_json = json.dumps(weather_data)
            
            weather_entry = WeatherData(
                data_type='openweather',
                values=weather_data_json,
                usage='previsao_climatica'
            )
            
            db.session.add(weather_entry)
            db.session.commit()
            
            weather_data_list.append(weather_data_json)  
            
        else:
            return f'Erro na extração dos dados da API OpenWeather para {city}', 500

    return weather_data_list

@app.route('/etl', methods=['GET'])
def etl_route():
    weather_data_list = perform_etl()
    return 'Dados extraídos e armazenados no banco de dados'


@app.route('/weather_data', methods=['GET'])
def display_weather_data():
    weather_data = WeatherData.query.all()
    return render_template('weather_table.html', weather_data=weather_data)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
