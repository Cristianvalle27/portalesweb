from flask import Flask, render_template, url_for
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
#def home():
def index():
    empresas = [
        "Autochevrolet", "Automarcol", "autotropical", "BIOPHARMA", "CARGRANEL",
        "CENPI", "Colacteos", "Colegas", "diesellamontana", "DISDROBLAN", "DistriMayor", "Distrimedical",
        "DynamicE", "Dynamic", "drogueriaparis", "Dromedics", "Econnabis", "ESTYMA", "EUROAUTOS",
        "Fedco", "Filicudi", "BARUMOTORS", "ferreterialarebaja", "massymotor", "automontana",
        "Autogalias", "Proxxon", "Sincromotors", "grupolizcano", "gruporoldan", "grupoautama",
        "Grupoconhydra", "Herson", "Adoquinar", "ISUZU", "JoyeriaInter", "medicalsupplies",
        "Medife", "grupomonaco", "aliadas", "Morarci", "MOTOBLU", "Pasumotos", "NOVAMOTORS",
        "Pijaos", "ellas", "Redihos", "Redllantas", "Rylsa", "Sida", "Subocol", "Suky_Moto",
        "SUMOTO", "Surtizora", "Tiendas", "Vialactea", "yamahasports","Casab","PortalA","PortalE"
    ]

 # Diccionario de logos
    logos = {name: url_for('static', filename=f"{name}.jpg") for name in empresas}
    logos.update({
        "imagen_url": url_for('static', filename='NomiwebLogo.jpg'),
        "favicon": url_for('static', filename='favicon.jpg')
    })

    return render_template("portales.html", logos=logos, now=datetime.now())

if __name__ == "__main__":
    #app.run(debug=True)
    try:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Error iniciando la app: {e}")
