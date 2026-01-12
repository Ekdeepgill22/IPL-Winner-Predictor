import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from preprocess import load_data

def train_model():
    df = load_data()

    # Select features and target
    features = df[['team1', 'team2', 'toss_winner', 'toss_decision', 'venue']].copy()
    target = df['winner']

    # Encode categorical features
    encoders = {}
    for col in features.columns:
        if features[col].dtype == 'object':
            enc = LabelEncoder()
            features[col] = enc.fit_transform(features[col])
            encoders[col] = enc

    # Encode target
    target_encoder = LabelEncoder()
    target = target_encoder.fit_transform(target)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc:.2f}")

    return model, encoders, target_encoder


def predict_winner(model, encoders, target_encoder, team1, team2, toss_winner, toss_decision, venue):
    input_data = {
        'team1': [team1],
        'team2': [team2],
        'toss_winner': [toss_winner],
        'toss_decision': [toss_decision],
        'venue': [venue],
    }

    input_df = pd.DataFrame(input_data)

    # Validate and encode using fitted encoders
    for col in input_df.columns:
        if col in encoders:
            encoder = encoders[col]
            if input_df[col][0] not in encoder.classes_:
                raise ValueError(f"Value '{input_df[col][0]}' for column '{col}' was not seen during training.")
            input_df[col] = encoder.transform(input_df[col])

    # Predict and decode
    pred = model.predict(input_df)[0]
    winner = target_encoder.inverse_transform([pred])[0]
    return winner

