from flask import Flask, render_template, request

app = Flask(__name__)

abc = ["Santo André", "São Bernardo do Campo", "São Caetano do Sul", "Diadema", "Mauá", "Ribeirão Pires", "Rio Grande da Serra"]
sa = "Santo André"

# Dados dos impostos municipais para Santo André
sa_impostos_municipais = [
    {'ano': 2013, 'IPTU': 182885856.6, 'ITBS': 58775236.68, 'ISS': 220675566.8},
    {'ano': 2014, 'IPTU': 206129515.3, 'ITBS': 60106994.67, 'ISS': 252571525.3},
    {'ano': 2015, 'IPTU': 218152633.4, 'ITBS': 52743717.12, 'ISS': 270456026.8},
    {'ano': 2016, 'IPTU': 249884466.3, 'ITBS': 56295067.95, 'ISS': 294671851.2},
    {'ano': 2017, 'IPTU': 269017392.9, 'ITBS': 53289653.04, 'ISS': 319956257.1},
    {'ano': 2018, 'IPTU': 310753436.5, 'ITBS': 58214311.55, 'ISS': 432016904.1},
    {'ano': 2019, 'IPTU': 298008778.1, 'ITBS': 56467105.95, 'ISS': 500905568.2},
    {'ano': 2020, 'IPTU': 303588586.9, 'ITBS': 65593934.97, 'ISS': 455354380.5},
    {'ano': 2021, 'IPTU': 345514436.5, 'ITBS': 93521921.94, 'ISS': 538284856.6},
    {'ano': 2022, 'IPTU': 409377801.6, 'ITBS': 88897001.02, 'ISS': 592933509.1}
]

@app.route('/')
def home():
    return render_template('index.html', abc=abc)
    

@app.route('/busca', methods=['POST'])
def busca():
    municipio = request.form['nome']
    if municipio == "Santo André":
        return render_template('sa.html', sa_impostos_municipais=sa_impostos_municipais)
    else:
        return 'Município não encontrado.'

if __name__ == "__main__":
    app.run(debug=True)
