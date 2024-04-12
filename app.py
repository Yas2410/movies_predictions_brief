from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Chargement du modèle (Ici, XGBoost est le meilleur mais conflit
# le test est donc effectué avec le modèle Random Forest)
prediction_model = joblib.load("models/prediction_model_RF.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            duration = request.form.get("duration", type=int)
            director_fb_likes = request.form.get("director_fb_likes", type=int)
            actor_1_fb_likes = request.form.get("actor_1_fb_likes", type=int)
            gross = request.form.get("gross", type=float)
            num_voted_users = request.form.get("num_voted_users", type=int)
            facenumber_in_poster = request.form.get("facenumber_in_poster", type=int)  # noqa: E501
            budget = request.form.get("budget", type=int)
            title_year = request.form.get("title_year", type=int)
            aspect_ratio = request.form.get("aspect_ratio", type=int)
            movie_fb_likes = request.form.get("movie_fb_likes", type=int)
            country = request.form.get("country")
            country_UK = (country == "UK")
            country_USA = (country == "USA")
            other_actors_fb_likes = request.form.get("other_actors_fb_likes", type=int)  # noqa: E501
            critic_reviews_ratio = request.form.get("critic_reviews_ratio", type=float)  # noqa: E501

            # Avec linter Flake8, limites du nbr caractères : "# noqa: E501" pour ignorer cela

            # L'ensemble des variables collectées est assemblé dans un tableau (features)  # noqa : E501
            # qui va ensuite être utilisé lors de la prédiction plus bas
            features = np.array([[
                duration,
                director_fb_likes,
                actor_1_fb_likes,
                gross,
                num_voted_users,
                facenumber_in_poster,
                budget,
                title_year,
                aspect_ratio,
                movie_fb_likes,
                country_UK,
                country_USA,
                other_actors_fb_likes,
                critic_reviews_ratio
            ]])
            #print(features)

            # On effectue la prédiction avec le modèle
            prediction = prediction_model.predict(features)

            # On retourne la page de résultats
            return render_template("prediction_results.html", prediction=prediction[0])  # noqa: E501
        except Exception as e:
            return str(e)
    else:
        # Si méthode GET, on affiche le formulaire
        return render_template("formulaire.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
