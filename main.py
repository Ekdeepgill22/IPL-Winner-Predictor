from model import train_model, predict_winner

# Train the model and get encoders
model, encoders, target_encoder = train_model()

# Sample input for prediction
test_input = {
    'team1': "Mumbai Indians",
    'team2': "Chennai Super Kings",
    'toss_winner': "Mumbai Indians",
    'toss_decision': "bat",
    'venue': "Wankhede Stadium",
}

# Predict winner
winner = predict_winner(
    model,
    encoders,
    target_encoder,
    test_input['team1'],
    test_input['team2'],
    test_input['toss_winner'],
    test_input['toss_decision'],
    test_input['venue'],
)

print(f"Predicted Winner: {winner}")
