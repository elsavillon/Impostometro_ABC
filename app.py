from flask import Flask, render_template, request, redirect, url_for

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
        try:
            municipio = request.form['nome']
            if municipio == "Santo André":
                return render_template('sa.html')
            elif municipio == "São Bernardo do Campo":
                return render_template('sbc.html')
            elif municipio == "São Caetano do Sul":
                return render_template('scs.html')
            elif municipio == 'Diadema':
                return render_template('diadema.html')
            elif municipio == 'Mauá':
                return render_template('maua.html')
            elif municipio == "Ribeirão Pires":
                return render_template('rp.html')
            elif municipio == "Rio Grande da Serra":
                return render_template('rgs.html')
            else:
                return 'Município não encontrado.'
        except Exception as e:
            print(f"Erro ao processar a solicitação: {e}")
            return f"Ocorreu um erro: {e}", 500
    else:
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
