from flask import Blueprint, redirect, url_for, session, request, render_template
from urllib.parse import urlencode
from config import Config
from models.user_model import find_user, create_user
import requests as req
import secrets

auth_bp = Blueprint("auth", __name__)

GOOGLE_AUTH_URL     = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL    = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"


@auth_bp.route("/login")
def login():
    if "user" in session:
        return redirect(url_for("movie.home"))
    return render_template("login.html")


@auth_bp.route("/auth/google")
def auth_google():
    state                  = secrets.token_urlsafe(32)
    session["oauth_state"] = state
    session.modified       = True

    params = {
        "client_id"     : Config.GOOGLE_CLIENT_ID,
        "redirect_uri"  : Config.GOOGLE_REDIRECT_URI,
        "response_type" : "code",
        "scope"         : "openid email profile",
        "state"         : state,
        "access_type"   : "online",
        "prompt"        : "select_account"
    }
    return redirect(f"{GOOGLE_AUTH_URL}?{urlencode(params)}")


@auth_bp.route("/auth/callback")
def auth_callback():
    # Verifikasi state
    state_session = session.pop("oauth_state", None)
    state_request = request.args.get("state")
    if not state_session or state_session != state_request:
        return redirect(url_for("auth.login"))

    code = request.args.get("code")
    if not code:
        return redirect(url_for("auth.login"))

    # Tukar code → access token
    token_data   = req.post(GOOGLE_TOKEN_URL, data={
        "code"          : code,
        "client_id"     : Config.GOOGLE_CLIENT_ID,
        "client_secret" : Config.GOOGLE_CLIENT_SECRET,
        "redirect_uri"  : Config.GOOGLE_REDIRECT_URI,
        "grant_type"    : "authorization_code"
    }).json()

    access_token = token_data.get("access_token")
    if not access_token:
        return redirect(url_for("auth.login"))

    # Ambil data user dari Google
    user_info = req.get(
        GOOGLE_USERINFO_URL,
        headers={"Authorization": f"Bearer {access_token}"}
    ).json()

    google_id = user_info.get("sub")
    if not google_id:
        return redirect(url_for("auth.login"))

    # Simpan user ke MongoDB jika belum ada
    if not find_user(google_id):
        create_user(
            google_id,
            user_info.get("name"),
            user_info.get("email"),
            user_info.get("picture")
        )

    session["user"] = {
        "google_id" : google_id,
        "name"      : user_info.get("name"),
        "email"     : user_info.get("email"),
        "picture"   : user_info.get("picture"),
    }
    return redirect(url_for("movie.home"))


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))