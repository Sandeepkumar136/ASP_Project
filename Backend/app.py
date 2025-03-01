from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Social Media Poster API is running!"

if __name__ == "__main__":
    print("Starting Flask server...")  # Explicitly print this
    app.run(debug=True)
