import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load product data
with open('supply_chain_data.json') as f:
    supply_chain_data = json.load(f)

@app.route('/start-game', methods=['POST'])
def start_game():
    user_choice = request.json['product']
    user_country = request.json['country']
    
    # Initialize game state
    game_state = {
        "product": user_choice,
        "country": user_country,
        "profit": 1000,  # Starting profit
        "sustainability": 100,
        "carbon_footprint": 0,
        "current_supply_chain": supply_chain_data['products'][user_choice]['supply_chain'],
        "events": supply_chain_data['products'][user_choice]['events']
    }
    
    return jsonify(game_state)

@app.route('/simulate-event', methods=['POST'])
def simulate_event():
    event = random.choice(game_state["events"])
    impact = event["impact"]
    
    # Update game state based on event impact
    game_state["profit"] += impact["profit"]
    game_state["sustainability"] += impact["sustainability"]
    game_state["carbon_footprint"] += impact["carbon_footprint"]
    
    return jsonify({"event": event, "new_state": game_state})
