document.getElementById('start-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const product = document.getElementById('product').value;
    const country = document.getElementById('country').value;

    // Start game
    fetch('/start-game', {
        method: 'POST',
        body: JSON.stringify({ product: product, country: country }),
        headers: { 'Content-Type': 'application/json' }
    }).then(response => response.json())
      .then(gameState => updateGameDisplay(gameState));

    // Function to simulate an event after a turn
    function simulateEvent() {
        fetch('/simulate-event', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        }).then(response => response.json())
          .then(eventData => {
              updateGameDisplay(eventData.new_state);
              logEvent(eventData.event);
          });
    }
});
