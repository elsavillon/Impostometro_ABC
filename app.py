from flask import Flask, render_template, request

app = Flask(__name__)

abc = ["Santo André", "São Bernardo do Campo", "São Caetano do Sul", "Diadema", "Mauá", "Ribeirão Pires", "Rio Grande da Serra"]
sa = "Santo André"
sbc= "São Bernardo do Campo"
scs= "São Caetano do Sul"
diadema= "Diadema"
maua= "Mauá"
rp= "Ribeirão Pires"
rgs= "Rio Grande da Serra"

# Dados dos impostos municipais
impostos_municipais = {
    'sa': [
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
    ],
    'sbc': [
        {'ano': 2013, 'IPTU': 269200068.7, 'ITBS': 66942773.34, 'ISS': 298149955.5},
        {'ano': 2014, 'IPTU': 281721220.9, 'ITBS': 65008090.61, 'ISS': 310935415.8},
        {'ano': 2015, 'IPTU': 300202768.6, 'ITBS': 67411002.62, 'ISS': 367050234.5},
        {'ano': 2016, 'IPTU': 330039197.1, 'ITBS': 65698105.62, 'ISS': 393366779.4},
        {'ano': 2017, 'IPTU': 360759265.2, 'ITBS': 73815167.2, 'ISS': 391367995.6},
        {'ano': 2018, 'IPTU': 401342090.2, 'ITBS': 79227250.41, 'ISS': 479089222.8},
        {'ano': 2019, 'IPTU': 436783456.6, 'ITBS': 91399020.67, 'ISS': 518502997.8},
        {'ano': 2020, 'IPTU': 431566278.7, 'ITBS': 97356343.44, 'ISS': 491386551.4},
        {'ano': 2021, 'IPTU': 501321866.2, 'ITBS': 122384334.6, 'ISS': 590951066.5},
        {'ano': 2022, 'IPTU': 541135098.7, 'ITBS': 108925918.2, 'ISS': 708945777.3}
    ],
    'scs': [
        {'ano': 2013, 'IPTU': 105428868.5, 'ITBS': 23209134.14, 'ISS': 146960306.4},
        {'ano': 2014, 'IPTU': 112423157.4, 'ITBS': 28074793.62, 'ISS': 152511229.9},
        {'ano': 2015, 'IPTU': 126825333.6, 'ITBS': 30784336.39, 'ISS': 164261087.4},
        {'ano': 2016, 'IPTU': 136022989, 'ITBS': 21332548.7, 'ISS': 163268331.4},
        {'ano': 2017, 'IPTU': 144792986.6, 'ITBS': 20946901.91, 'ISS': 169237344.6},
        {'ano': 2018, 'IPTU': 176065149.9, 'ITBS': 27476929.91, 'ISS': 222632296},
        {'ano': 2019, 'IPTU': 179559321.5, 'ITBS': 25887276.6, 'ISS': 227209481.7},
        {'ano': 2020, 'IPTU': 171838716.6, 'ITBS': 27492176.67, 'ISS': 212988813.5},
        {'ano': 2021, 'IPTU': 183670102.4, 'ITBS': 43443378.64, 'ISS': 235992768.9},
        {'ano': 2022, 'IPTU': 210852549.8, 'ITBS': 33544293.04, 'ISS': 252080301.1}
    ],
    'diadema': [
        {'ano': 2013, 'IPTU': 92786572.18, 'ITBS': 10096935.57, 'ISS': 69038980.35},
        {'ano': 2014, 'IPTU': 104956733.1, 'ITBS': 18057223.14, 'ISS': 73939973.5},
        {'ano': 2015, 'IPTU': 116812911.8, 'ITBS': 14015548, 'ISS': 73328818.02},
        {'ano': 2016, 'IPTU': 132877311.4, 'ITBS': 16959816.48, 'ISS': 74735450.23},
        {'ano': 2017, 'IPTU': 145893704.3, 'ITBS': 19740541.4, 'ISS': 77990064.85},
        {'ano': 2018, 'IPTU': 181159084.3, 'ITBS': 20279236.4, 'ISS': 90353187.18},
        {'ano': 2019, 'IPTU': 186594341.4, 'ITBS': 20213198.71, 'ISS': 100269947.1},
        {'ano': 2020, 'IPTU': 175022928.4, 'ITBS': 15526341.51, 'ISS': 95647874.86},
        {'ano': 2021, 'IPTU': 197585301.5, 'ITBS': 26706288.76, 'ISS': 109336653.9},
        {'ano': 2022, 'IPTU': 212333539.8, 'ITBS': 25088837.28, 'ISS': 131286798.5}
    ],
    'maua': [
        {'ano': 2013, 'IPTU': 60724650.33, 'ITBS': 5835725.62, 'ISS': 56401977.48},
        {'ano': 2014, 'IPTU': 65092534.1, 'ITBS': 6362944.9, 'ISS': 59599221.68},
        {'ano': 2015, 'IPTU': 67685757.34, 'ITBS': 10756361.44, 'ISS': 69374953.13},
        {'ano': 2016, 'IPTU': 77789966.97, 'ITBS': 10628629.23, 'ISS': 77634321.57},
        {'ano': 2017, 'IPTU': 77593540.91, 'ITBS': 9192373.56, 'ISS': 67876213.85},
        {'ano': 2018, 'IPTU': 102771196.3, 'ITBS': 11394718.95, 'ISS': 85935328.71},
        {'ano': 2019, 'IPTU': 104655032.1, 'ITBS': 20312925.68, 'ISS': 99784593.39},
        {'ano': 2020, 'IPTU': 105753368.2, 'ITBS': 17940079.84, 'ISS': 102557718.1},
        {'ano': 2021, 'IPTU': 109818115.2, 'ITBS': 21298704.23, 'ISS': 120876188.6},
        {'ano': 2022, 'IPTU': 140107404.4, 'ITBS': 17987708.27, 'ISS': 130973007.7}
    ],
    'rp': [
        {'ano': 2013, 'IPTU': 19902540.7, 'ITBS': 2101291.64, 'ISS': 20928344.52},
        {'ano': 2014, 'IPTU': 22699775.94, 'ITBS': 2167522.54, 'ISS': 19980195.6},
        {'ano': 2015, 'IPTU': 24935536.87, 'ITBS': 2403622.98, 'ISS': 18959349.25},
        {'ano': 2016, 'IPTU': 27260889.51, 'ITBS': 1636444.91, 'ISS': 19161072.01},
        {'ano': 2017, 'IPTU': 29027386.97, 'ITBS': 2209940.6, 'ISS': 18380227.37},
        {'ano': 2018, 'IPTU': 42072787.6, 'ITBS': 2649006.78, 'ISS': 28609407.16},
        {'ano': 2019, 'IPTU': 51047607.71, 'ITBS': 4899316.74, 'ISS': 30458079.66},
        {'ano': 2020, 'IPTU': 51047607.71, 'ITBS': 4899316.74, 'ISS': 30458079.66},
        {'ano': 2021, 'IPTU': 51047607.71, 'ITBS': 4899316.74, 'ISS': 30458079.66},
        {'ano': 2022, 'IPTU': 57836055.07, 'ITBS': 5197201.28, 'ISS': 39664808.24}
    ],
    'rgs': [
        {'ano': 2013, 'IPTU': 1646452.93, 'ITBS': 180845.89, 'ISS': 2022979.04},
        {'ano': 2014, 'IPTU': 1758695.98, 'ITBS': 226520.78, 'ISS': 2092090.54},
        {'ano': 2015, 'IPTU': 1920582.76, 'ITBS': 242572.31, 'ISS': 3305958.92},
        {'ano': 2016, 'IPTU': 2024906.89, 'ITBS': 364207.84, 'ISS': 2691157.17},
        {'ano': 2017, 'IPTU': 2187139.25, 'ITBS': 256961.07, 'ISS': 2212830.26},
        {'ano': 2018, 'IPTU': 4341282.68, 'ITBS': 217712.46, 'ISS': 2850287.5},
        {'ano': 2019, 'IPTU': 5204470.91, 'ITBS': 199734.86, 'ISS': 3576792.65},
        {'ano': 2020, 'IPTU': 4989196.31, 'ITBS': 253291.22, 'ISS': 2574085.69},
        {'ano': 2021, 'IPTU': 6278329.34, 'ITBS': 277768.41, 'ISS': 3370320.23},
        {'ano': 2022, 'IPTU': 7187279.69, 'ITBS': 272800.3, 'ISS': 4540192.86}
    ]
}

@app.route('/')
def home():
    return render_template('index.html', abc=abc, sa=sa, sbc=sbc, scs=scs, diadema=diadema, maua=maua, rp=rp, rgs=rgs)

@app.route('/busca', methods=['GET', 'POST'])
def busca():
    if request.method == 'POST':
        municipio = request.form['nome']
        if municipio == "Santo André":
            return render_template('sa.html', sa_impostos_municipais=impostos_municipais['sa'])
        elif municipio == "São Bernardo do Campo":
            return render_template('sbc.html', sbc_impostos_municipais=impostos_municipais['sbc'])
        elif municipio == "São Caetano do Sul":
            return render_template('scs.html', scs_impostos_municipais=impostos_municipais['scs'])
        elif municipio == 'Diadema':
            return render_template('diadema.html', diadema_impostos_municipais=impostos_municipais['diadema'])
        elif municipio == 'Mauá':
            return render_template('maua.html', maua_impostos_municipais=impostos_municipais['maua'])
        elif municipio == "Ribeirão Pires":
            return render_template('rp.html', rp_impostos_municipais=impostos_municipais['rp'])
        elif municipio == "Rio Grande da Serra":
            return render_template('rgs.html', rgs_impostos_municipais=impostos_municipais['rgs'])
        else:
            return 'Município não encontrado.'
    else:
        # Se a solicitação for um GET, redirecione para a página inicial
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
