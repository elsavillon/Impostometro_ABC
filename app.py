from flask import Flask, render_template, request

app = Flask(__name__)

# Rota 1
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/busca', methods=['POST'])
def busca():
    ano = int(request.form['ano'])
    for municipio in sa:
        if municipio["ano"] == ano:
            resposta = municipio
            break
    else:
        resposta = None
    return render_template('resultado_busca.html', resultado=resposta)


@app.route('/sa')
def about():
    return 'Confira os impostos municipais por de Santo André de 2013 a 2022 por tipo e ano:'

def mostrar_detalhes(ano):
    ano = int(ano)
    for municipio in sa:
        if municipio["ano"] == ano:
            return render_template('detalhes.html', municipio=municipio)
    return "Ano não encontrado"


if __name__ == '__main__':
       sa = [
        {'ano': 2013, 'IPTU': 182885856.6, 'ITBS': 58775236.68, 'ISS': 220675566.8},
        {'ano': 2014, 'IPTU': 206129515.3, 'ITBS': 60106994.67, 'ISS': 252571525.3},
        {'ano': 2015, 'IPTU': 218152633.4, 'ITBS': 52743717.12, 'ISS': 270456026.8},
        {'ano': 2016, 'IPTU': 249884466.3, 'ITBS': 56295067.95, 'ISS': 294671851.2},
        {'ano': 2017, 'IPTU': 269017392.9, 'ITBS': 53289653.04, 'ISS': 319956257.1},
        {'ano': 2018, 'IPTU': 310753436.5, 'ITBS': 58214311.55, 'ISS': 432016904.1},
        {'ano': 2019, 'IPTU': 298008778.1, 'ITBS': 56467105.95, 'ISS': 500905568.2},
        {'ano': 2020, 'IPTU': 303588586.9, 'ITBS': 65593934.97, 'ISS': 455354380.5},
        {'ano': 2021, 'IPTU': 345514436.5, 'ITBS': 93521921.94, 'ISS': 538284856.6},
        {'ano': 2022, 'IPTU': 409377801.6, 'ITBS': 88897001.02, 'ISS': 592933509.1}]
    
        sbc = [{'ano': 2013, 'IPTU': 269200068.7, 'ITBS': 66942773.34, 'ISS': 298149955.5},
            {'ano': 2014, 'IPTU': 281721220.9, 'ITBS': 65008090.61, 'ISS': 310935415.8},
            {'ano': 2015, 'IPTU': 300202768.6, 'ITBS': 67411002.62, 'ISS': 367050234.5},
            {'ano': 2016, 'IPTU': 330039197.1, 'ITBS': 65698105.62, 'ISS': 393366779.4},
            {'ano': 2017, 'IPTU': 360759265.2, 'ITBS': 73815167.2, 'ISS': 391367995.6},
            {'ano': 2018, 'IPTU': 401342090.2, 'ITBS': 79227250.41, 'ISS': 479089222.8},
            {'ano': 2019, 'IPTU': 436783456.6, 'ITBS': 91399020.67, 'ISS': 518502997.8},
            {'ano': 2020, 'IPTU': 431566278.7, 'ITBS': 97356343.44, 'ISS': 491386551.4},
            {'ano': 2021, 'IPTU': 501321866.2, 'ITBS': 122384334.6, 'ISS': 590951066.5},
            {'ano': 2022, 'IPTU': 541135098.7, 'ITBS': 108925918.2, 'ISS': 708945777.3}]

