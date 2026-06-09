from pymongo import MongoClient

_client = None
_db     = None

def init_db(mongo_uri, db_name):
    """Inisialisasi koneksi MongoDB — dipanggil sekali di app.py"""
    global _client, _db
    _client = MongoClient(mongo_uri)
    _db     = _client[db_name]

def get_db():
    """Ambil instance database — dipanggil di models"""
    return _db