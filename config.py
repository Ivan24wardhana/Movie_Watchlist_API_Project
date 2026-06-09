import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask — cookie session biasa, BUKAN filesystem
    SECRET_KEY             = os.getenv("SECRET_KEY")
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE   = False        # False karena pakai HTTP (localhost)

    # Google OAuth
    GOOGLE_CLIENT_ID     = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_REDIRECT_URI  = os.getenv("GOOGLE_REDIRECT_URI")

    # TMDB
    TMDB_API_KEY         = os.getenv("TMDB_API_KEY")
    TMDB_BASE_URL        = os.getenv("TMDB_BASE_URL")
    TMDB_IMAGE_BASE_URL  = os.getenv("TMDB_IMAGE_BASE_URL")

    # MongoDB
    MONGO_URI            = os.getenv("MONGO_URI")
    MONGO_DB_NAME        = os.getenv("MONGO_DB_NAME")
    
    