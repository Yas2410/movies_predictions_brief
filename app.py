from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        #TODO: gestion des saisies dans le formulaire, load du modèle, prédiction, affichage résultat
        return render_template('prediction_result.html')
    return render_template('formulaire.html')

if __name__ == "__main__":
    app.run(debug=True)
