from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I asked the librarian if she had any books on paranoia. She whispered, 'They're right behind you!'",
    "Why don't eggs tell jokes? Because they might crack up!",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
    "Why did the tomato turn red? Because it saw the salad dressing!"
]

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')

@app.route('/jokes', methods=['GET'])
def get_jokes():
    num_jokes = int(request.args.get('num', 1))
    random_jokes = random.sample(jokes, num_jokes)

    formatted_jokes = []
    for i, joke in enumerate(random_jokes, start=1):
        formatted_jokes.append(f"Joke {i}: {joke}")

    jokes_text = '\n'.join(formatted_jokes)
    return f"<h2>Jokes</h2><pre>{jokes_text}</pre>"



if __name__ == '__main__':
    app.run()