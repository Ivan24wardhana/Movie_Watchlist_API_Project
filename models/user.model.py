from extensions import get_db

def find_user(google_id):
    """Cari user berdasarkan google_id"""
    db = get_db()
    return db["users"].find_one({"google_id": google_id})

def create_user(google_id, name, email, picture):
    """Simpan user baru ke MongoDB"""
    db = get_db()
    db["users"].insert_one({
        "google_id" : google_id,
        "name"      : name,
        "email"     : email,
        "picture"   : picture,
    })