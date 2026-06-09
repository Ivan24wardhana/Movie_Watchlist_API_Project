from flask import Blueprint, redirect, url_for, session, render_template, request
from models.watchlist_model import get_watchlist, find_in_watchlist, count_watchlist
from config import Config
import requests as req

movie_bp = Blueprint("movie", __name__)


def _tmdb_get(endpoint, params=None):
    """Helper internal untuk panggil TMDB API"""
    if params is None:
        params = {}
    params["api_key"]  = Config.TMDB_API_KEY
    params["language"] = "id-ID"
    return req.get(f"{Config.TMDB_BASE_URL}{endpoint}", params=params).json()

def _login_required():
    """Return redirect jika belum login, None jika sudah"""
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return None


@movie_bp.route("/")
def index():
    if "user" in session:
        return redirect(url_for("movie.home"))
    return redirect(url_for("auth.login"))


@movie_bp.route("/home")
def home():
    guard = _login_required()
    if guard:
        return guard

    watchlist = get_watchlist(session["user"]["google_id"])
    data      = _tmdb_get("/movie/popular", {"page": 1})
    popular   = [r for r in data.get("results", []) if r.get("poster_path")]

    return render_template(
        "home.html",
        user      = session["user"],
        watchlist = watchlist,
        results   = popular,
        query     = ""
    )

@movie_bp.route("/watchlist")
def watchlist_page():
    guard = _login_required()
    if guard:
        return guard

    watchlist = get_watchlist(session["user"]["google_id"])

    return render_template(
        "watchlist.html",
        user      = session["user"],
        watchlist = watchlist,
    )

@movie_bp.route("/search")
def search():
    guard = _login_required()
    if guard:
        return guard

    query   = request.args.get("q", "").strip()
    results = []

    if query:
        data    = _tmdb_get("/search/movie", {"query": query})
        results = [r for r in data.get("results", []) if r.get("poster_path")]

    watchlist = get_watchlist(session["user"]["google_id"])

    return render_template(
        "home.html",
        user      = session["user"],
        watchlist = watchlist,
        results   = results,
        query     = query
    )


@movie_bp.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    guard = _login_required()
    if guard:
        return guard

    movie        = _tmdb_get(f"/movie/{movie_id}", {"append_to_response": "credits"})
    in_watchlist = find_in_watchlist(session["user"]["google_id"], str(movie_id))

    return render_template(
        "movie_detail.html",
        user         = session["user"],
        movie        = movie,
        in_watchlist = in_watchlist,
        img_base     = Config.TMDB_IMAGE_BASE_URL
    )


@movie_bp.route("/profile")
def profile():
    guard = _login_required()
    if guard:
        return guard

    google_id = session["user"]["google_id"]
    stats = {
        "total"  : count_watchlist(google_id),
        "akan"   : count_watchlist(google_id, "Akan Di Tonton"),
        "sedang" : count_watchlist(google_id, "Sedang Di Tonton"),
        "sudah"  : count_watchlist(google_id, "Sudah Di Tonton"),
    }
    return render_template("profile.html", user=session["user"], stats=stats)