import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# This function simulates an AI generating personalized lyrics.
# In a real application, this would involve a complex AI model
# that processes user input and potentially existing lyric data.
def generate_personalized_lyrics(title: str, artist: str, user_mood: str) -> str:
    """
    Simulates an AI generating personalized lyrics based on input.
    The 'personalization' aspect is demonstrated by adapting the output
    based on the 'user_mood'.
    """
    base_lyrics = f"Oh, {title} by {artist},\n"
    if "happy" in user_mood.lower():
        base_lyrics += "Your melody brings joy, a sunny day's delight.\n"
        base_lyrics += "Every note a smile, shining ever so bright."
    elif "sad" in user_mood.lower():
        base_lyrics += "Your melody echoes a quiet, rainy night.\n"
        base_lyrics += "A gentle solace found in fading light."
    elif "energetic" in user_mood.lower():
        base_lyrics += "Your rhythm pulses strong, a vibrant, burning fire.\n"
        base_lyrics += "Igniting passion, taking spirits higher."
    else:
        base_lyrics += "Your melody whispers secrets, soft and low.\n"
        base_lyrics += "A unique story only you would know."
    
    base_lyrics += f"\n-- Generated for your current mood: '{user_mood}'"
    return base_lyrics

@app.route('/generate-lyrics', methods=['POST'])
def lyrics_generator():
    """
    API endpoint to generate personalized lyrics.
    Expects a JSON payload with 'title', 'artist', and 'user_mood'.
    This endpoint represents the core 'Song Lingo' AI service described in the article.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    title = data.get('title')
    artist = data.get('artist')
    user_mood = data.get('user_mood')

    if not all([title, artist, user_mood]):
        return jsonify({"error": "Missing 'title', 'artist', or 'user_mood' in request"}), 400

    # Call the simulated AI function to get personalized lyrics
    personalized_lyrics = generate_personalized_lyrics(title, artist, user_mood)
    
    return jsonify({
        "song_title": title,
        "artist": artist,
        "user_mood": user_mood,
        "personalized_lyrics": personalized_lyrics
    })

@app.route('/')
def health_check():
    """
    Basic health check endpoint for Cloud Run deployment.
    """
    return "Song Lingo AI service is running!"

if __name__ == '__main__':
    # Cloud Run expects the application to listen on the port specified by the PORT environment variable.
    # If running locally, it defaults to 8080.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
