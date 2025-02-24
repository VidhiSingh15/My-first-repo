from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'guessing_game_secret'  # Secret key for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        # Initialize session variables
        if 'number' not in session:
            session['number'] = random.randint(1, 100)
            session['attempts'] = 0

        message = ""

        if request.method == 'POST':
            user_guess = request.form.get('guess')

            if user_guess and user_guess.isdigit():
                user_guess = int(user_guess)
                session['attempts'] += 1

                if user_guess < session['number']:
                    message = "🔽 Too low! Try again."
                elif user_guess > session['number']:
                    message = "🔼 Too high! Try again."
                else:
                    message = f"🎉 Correct! You guessed it in {session['attempts']} attempts!"
                    session.pop('number')  # Reset game
                    session.pop('attempts')

            else:
                message = "⚠️ Please enter a valid number!"

        return render_template('index.html', message=message)

    except Exception as e:
        return f"⚠️ Error: {str(e)}", 500  # Display error message if something fails

if __name__ == '__main__':
    app.run(debug=True)
