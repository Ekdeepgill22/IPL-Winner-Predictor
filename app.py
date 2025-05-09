from flask import Flask, render_template, request, jsonify
from model import train_model, predict_winner
from venues import get_team_venues

app = Flask(__name__)
model, encoders, target_encoder = train_model()
team_venue_map = get_team_venues()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    winner = predict_winner(
        model, encoders, target_encoder,
        data["team1"], data["team2"],
        data["toss_winner"], data["toss_decision"], data["venue"]
    )
    return jsonify({"winner": winner})

@app.route("/get_team_venues")
def get_team_venues_route():
    from venues import get_team_venues
    return jsonify(get_team_venues())


@app.route("/get_neutral_venues")
def get_neutral_venues_route():
    from venues import get_neutral_venues
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    return jsonify(get_neutral_venues(team1, team2))


if __name__ == "__main__":
    app.run(debug=True)
