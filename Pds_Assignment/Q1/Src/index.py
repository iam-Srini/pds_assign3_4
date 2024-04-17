import dash
from dash import dcc, html, Input, Output
import requests

# Default city
DEFAULT_CITY = "London"

# Fetching weather data function
def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7c429190c8ddf550f4a621e305713e8a"
    response = requests.get(url)
    return response.json()

# Creating the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Weather Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.Label("City:"),
        dcc.Input(id='city', type='text', value=DEFAULT_CITY, style={'marginRight': '10px'}),
        html.Button(id='submit-button', n_clicks=0, children='Submit', style={'marginBottom': '10px'}),
    ], style={'textAlign': 'center'}),
    html.Div(id='weather-info', className='container', style={'textAlign': 'center'})
])

# Callback to update weather info
@app.callback(
    Output('weather-info', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('city', 'value')]
)
def update_weather_info(n_clicks, city):
    weather_data = fetch_weather_data(city)
    temperature = round(weather_data['main']['temp'] - 273.15, 2)  # converting from Kelvin to Celsius
    feels_like = round(weather_data['main']['feels_like'] - 273.15, 2)
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']
    
    return html.Div([
        html.Div([
            html.H2("Location"),
            html.P(weather_data['name'])
        ], className='box'),
        html.Div([
            html.H2("Temperature"),
            html.P(f"{temperature}°C")
        ], className='box'),
        html.Div([
            html.H2("Feels Like"),
            html.P(f"{feels_like}°C")
        ], className='box'),
        html.Div([
            html.H2("Description"),
            html.P(description)
        ], className='box'),
        html.Div([
            html.H2("Wind Speed"),
            html.P(f"{wind_speed} m/s")
        ], className='box'),
        html.Div([
            html.H2("Humidity"),
            html.P(f"{humidity}%")
        ], className='box')
    ], style={'display': 'inline-block', 'textAlign': 'left'})

# Running the app
if __name__ == '__main__':
    app.run_server(debug=True)
