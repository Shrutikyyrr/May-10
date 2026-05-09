from flask import Flask, jsonify

from database import init_db

from routes.book_routes import book_bp
from routes.member_routes import member_bp
from routes.borrow_routes import borrow_bp
from routes.analytics_routes import analytics_bp
from routes.upload_routes import upload_bp

from routes.log_routes import log_bp

app = Flask(__name__)

# Initialize Database
init_db()

# Register Blueprints
app.register_blueprint(book_bp)
app.register_blueprint(member_bp)
app.register_blueprint(borrow_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(log_bp)

@app.route("/")
def home():
    return jsonify({
        "message": "LibTrack API Running"
    })

if __name__ == "__main__":
    app.run(debug=True)