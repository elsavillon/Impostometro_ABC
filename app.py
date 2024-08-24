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
