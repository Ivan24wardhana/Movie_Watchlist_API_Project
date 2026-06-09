from extensions import get_db
from datetime import datetime

def get_watchlist(user_id):
    """Ambil semua watchlist milik user, urutkan terbaru"""
    db    = get_db()
    items = list(db["watchlist"].find({"user_id": user_id}).sort("added_at", -1))
    for item in items:
        item["_id"] = str(item["_id"])
    return items

def find_in_watchlist(user_id, movie_id):
    """Cek apakah film sudah ada di watchlist user"""
    db   = get_db()
    item = db["watchlist"].find_one({
        "user_id"  : user_id,
        "movie_id" : str(movie_id)
    })
    if item:
        item["_id"] = str(item["_id"])
    return item

def add_to_watchlist(user_id, movie_id, title, poster_path, genres):
    """Tambah film baru ke watchlist"""
    db = get_db()
    db["watchlist"].insert_one({
        "user_id"    : user_id,
        "movie_id"   : str(movie_id),
        "title"      : title,
        "poster_path": poster_path,
        "genres"     : genres,
        "status"     : "Akan Di Tonton",
        "added_at"   : datetime.utcnow()
    })

def update_status(user_id, movie_id, new_status):
    """Update status tonton film di watchlist"""
    db = get_db()
    db["watchlist"].update_one(
        {"user_id": user_id, "movie_id": movie_id},
        {"$set": {"status": new_status}}
    )

def delete_from_watchlist(user_id, movie_id):
    """Hapus film dari watchlist"""
    db = get_db()
    db["watchlist"].delete_one({"user_id": user_id, "movie_id": movie_id})

def count_watchlist(user_id, status=None):
    """Hitung jumlah film, bisa filter by status"""
    db    = get_db()
    query = {"user_id": user_id}
    if status:
        query["status"] = status
    return db["watchlist"].count_documents(query)