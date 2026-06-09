from flask import Flask
from config import Config
from extensions import init_db

# Import semua Blueprint (Controller)
from controllers.auth_controller      import auth_bp
from controllers.movie_controller     import movie_bp
from controllers.watchlist_controller import watchlist_bp

# INIT APP
app = Flask(__name__)
app.config.from_object(Config)

# INIT DATABASE
init_db(app.config["MONGO_URI"], app.config["MONGO_DB_NAME"])

# REGISTER BLUEPRINTS
app.register_blueprint(auth_bp)
app.register_blueprint(movie_bp)
app.register_blueprint(watchlist_bp)

# RUN
if __name__ == "__main__":
    app.run(debug=True, port=5000)