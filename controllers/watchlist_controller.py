from flask import Blueprint, redirect, url_for, session, request, flash
from models.watchlist_model import (
    find_in_watchlist,
    add_to_watchlist,
    update_status,
    delete_from_watchlist
)

watchlist_bp = Blueprint("watchlist", __name__)


def _login_required():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return None


@watchlist_bp.route("/watchlist/add", methods=["POST"])
def watchlist_add():
    guard = _login_required()
    if guard:
        return guard

    movie_id    = request.form.get("movie_id")
    title       = request.form.get("title")
    poster_path = request.form.get("poster_path")
    genres      = request.form.get("genres", "")
    user_id     = session["user"]["google_id"]

    if not find_in_watchlist(user_id, movie_id):
        add_to_watchlist(user_id, movie_id, title, poster_path, genres)
        flash(f"✅ '{title}' berhasil ditambahkan ke watchlist!", "success")

    return redirect(url_for("movie.movie_detail", movie_id=movie_id))


@watchlist_bp.route("/watchlist/status/<movie_id>", methods=["POST"])
def watchlist_status(movie_id):
    guard = _login_required()
    if guard:
        return guard

    user_id    = session["user"]["google_id"]
    new_status = request.form.get("status")
    item       = find_in_watchlist(user_id, movie_id)

    update_status(user_id, movie_id, new_status)

    title = item["title"] if item else "Film"
    flash(f"✅ Status '{title}' diubah ke '{new_status}'", "success")

    return redirect(request.referrer or url_for("movie.home"))


@watchlist_bp.route("/watchlist/delete/<movie_id>", methods=["POST"])
def watchlist_delete(movie_id):
    guard = _login_required()
    if guard:
        return guard

    delete_from_watchlist(session["user"]["google_id"], movie_id)
    flash("🗑️ Film berhasil dihapus dari watchlist.", "success")
    return redirect(url_for("movie.home"))