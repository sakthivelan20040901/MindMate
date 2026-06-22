from flask import Flask, render_template

from routes.chat import chat
from routes.newsletter import newsletter
from routes.youtube import youtube_bp
from routes.dashboard import dashboard_bp

app = Flask(__name__)

app.register_blueprint(chat)
app.register_blueprint(newsletter)
app.register_blueprint(youtube_bp)
app.register_blueprint(dashboard_bp)

@app.route("/")
def home():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
