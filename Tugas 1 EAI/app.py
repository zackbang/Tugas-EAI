from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/film')
def film():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWeekTop10"
    
    headers = {
        "X-RapidAPI-Key": "d7b77aea13msh27e5a2f1c5f8580p1677c9jsn7eecc6e217c6",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
        }
    
    response = requests.get(url, headers=headers)
    
    film = response.json()['data']

    return render_template('film (endpoint 1).html', film = film)

if __name__ == '__main__':
    app.run(debug=True)