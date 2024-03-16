from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def root():
    return "welcome to tokped"

@app.route('/yutub')
def Yutub():
    url = "https://minecraft-servers-list.p.rapidapi.com/getall"

    querystring = {"limit":"30"}

    headers = {
        "X-RapidAPI-Key": "d7b77aea13msh27e5a2f1c5f8580p1677c9jsn7eecc6e217c6",
        "X-RapidAPI-Host": "minecraft-servers-list.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    server = response.json()

    return render_template('minecraft.html', server = server)

if __name__ == '__main__':
    app.run(debug=True)