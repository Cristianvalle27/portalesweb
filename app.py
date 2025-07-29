from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
#def home():
def index():
    empresa_archivos = [
        "Autochevrolet", "Automarcol", "autotropical", "BIOPHARMA", "CARGRANEL",
        "CENPI", "Colacteos", "Colegas", "diesellamontana", "DISDROBLAN", "DistriMayor", "Distrimedical",
        "DynamicE", "Dynamic", "drogueriaparis", "Dromedics", "Econnabis", "ESTYMA", "EUROAUTOS",
        "Fedco", "Filicudi", "BARUMOTORS", "ferreterialarebaja", "massymotor", "automontana",
        "Autogalias", "Proxxon", "Sincromotors", "grupolizcano", "gruporoldan", "grupoautama",
        "Grupoconhydra", "Herson", "Adoquinar", "ISUZU", "JoyeriaInter", "medicalsupplies",
        "Medife", "grupomonaco", "aliadas", "Morarci", "MOTOBLU", "Pasumotos", "NOVAMOTORS",
        "Pijaos", "ellas", "Redihos", "Redllantas", "Rylsa", "Sida", "Subocol", "Suky_Moto",
        "SUMOTO", "Surtizora", "Tiendas", "Vialactea", "yamahasports","Casab","portalA","portalE"
    ]

    logos = {name: url_for('static', filename=f"{name}.jpg") for name in empresa_archivos}
    logos["imagen_url"] = url_for('static', filename='NomiwebLogo.jpg')
    logos["favicon"] = url_for('static', filename='favicon.jpg')

    return render_template("portales.html", logos=logos)

if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
