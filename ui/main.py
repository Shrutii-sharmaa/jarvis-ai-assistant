from flask import Flask, render_template , jsonify
import os

app = Flask(__name__)

# Route for your AI assistant's interface
@app.route("/")
def index():
    # Pass any context data to your template (e.g., initial prompts)
    return render_template("main.html")

@app.route('/api/get_log')
def get_log_data():
    with open(fr'{os.getcwd()}\templates\log.txt', 'r') as f:
        log_content = f.read()
    return jsonify({'log': log_content})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=4444)  # Set debug=False for production
