# Movie Watchlist Application

Aplikasi web berbasis Flask untuk mengelola daftar tontonan film (*Movie Watchlist*). Proyek ini dibangun menggunakan pendekatan **MVC (Model-View-Controller)** untuk memisahkan logika bisnis, pengelolaan database, dan tampilan antarmuka (*user interface*) secara rapi dan modular.

## 🚀 Fitur Utama

- **Autentikasi & Manajemen Pengguna:** Fitur pendaftaran akun baru (*Register*), masuk (*Login*), keluar (*Logout*), serta halaman profil pengguna.
- **Eksplorasi Film:** Menampilkan daftar katalog film pada halaman utama serta halaman detail informasi untuk setiap film.
- **Daftar Tontonan (Watchlist):** Fitur interaktif bagi pengguna yang telah login untuk menambahkan film ke daftar tontonan pribadi atau menghapusnya jika sudah selesai ditonton.

## 🛠️ Tech Stack

- **Backend Framework:** Python (Flask)
- **Database:** MongoDB (diintegrasikan melalui `models/`)
- **Frontend / Templating:** Jinja2 Templates, HTML5, CSS3 (dioptimalkan dengan Tailwind CSS)
- **Environment Management:** Python Virtual Environment (`venv`) & `python-dotenv`

## 📁 Struktur Folder

Proyek ini disusun dengan struktur direktori yang bersih dan terorganisir sebagai berikut:

```text
├── controllers/
│   ├── auth_controller.py        # Mengatur logika registrasi, login, & session
│   ├── movie_controller.py       # Mengatur logika penampilan katalog & detail film
│   ├── watchlist_controller.py   # Mengatur logika tambah/hapus film di watchlist
│   └── __init__.py
├── models/
│   ├── user_model.py             # Cetak biru data & interaksi database untuk User
│   ├── watchlist_model.py        # Cetak biru data & interaksi database untuk Watchlist
│   └── __init__.py
├── static/
│   └── img/                      # Tempat penyimpanan aset gambar statis
├── templates/
│   ├── base.html                 # Struktur dasar HTML (Navbar & Footer induk)
│   ├── home.html                 # Halaman utama (Dashboard katalog film)
│   ├── login.html                # Antarmuka halaman masuk
│   ├── movie_detail.html         # Antarmuka detail informasi film
│   ├── profile.html              # Antarmuka halaman profil user
│   └── ...                       # Halaman template pendukung lainnya
├── .env                          # File konfigurasi rahasia (Environment Variables) - diabaikan oleh Git
├── app.py                        # Entry point utama untuk menjalankan aplikasi Flask
├── config.py                     # Konfigurasi sistem dan pengaturan environment
├── extensions.py                 # Inisialisasi instansiasi library pihak ketiga
└── requirements.txt              # Daftar dependensi library Python yang dibutuhkan

⚙️ Prasyarat & Konfigurasi
Prasyarat Sistem
Sebelum menjalankan proyek ini, pastikan perangkat Anda sudah terpasang:

Python 3.10 atau versi di atasnya

MongoDB Server (Bisa menggunakan MongoDB Lokal/Community Server atau MongoDB Atlas di Cloud)

Konfigurasi .env
Karena file .env asli diabaikan demi keamanan, buatlah sebuah berkas baru bernama .env tepat di direktori utama (root) proyek Anda saat melakukan instalasi mandiri, kemudian sesuaikan variabel lingkungan berikut:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=masukkan_string_acak_dan_rahasia_di_sini

# Konfigurasi Koneksi Database MongoDB
MONGO_URI=mongodb://localhost:27017/movie_watchlist_db

# Konfigurasi Google OAuth (Jika digunakan)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

🛠️ Panduan Instalasi & Cara Menjalankan
Ikuti langkah-langkah di bawah ini untuk memasang dan menjalankan aplikasi di lingkungan lokal Anda:

1. Clone Repositori

git clone [https://github.com/Ivan24wardhana/Movie_Watchlist_API_Project.git](https://github.com/Ivan24wardhana/Movie_Watchlist_API_Project.git)
cd Movie_Watchlist_API_Project

2. Buat & Aktifkan Virtual Environment

Pengguna Windows:
python -m venv venv
venv\Scripts\activate

Pengguna macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3. Instal Seluruh Dependensi
Pastikan virtual environment Anda sudah aktif (ditandai dengan teks (venv) di terminal), lalu jalankan:
pip install -r requirements.txt

4. Jalankan Aplikasi
python app.py

Buka peramban (browser) Anda lalu akses alamat: http://127.0.0.1:5000/

📑 Dokumentasi Route & Endpoint
Aplikasi ini menggunakan perpaduan antara web views dan endpoint penanganan data:

1. Rute Autentikasi (controllers/auth_controller.py)

| Route | Method | Deskripsi | Hak Akses |
| :--- | :---: | :--- | :---: |
| `/register` | `GET, POST` | Halaman pendaftaran & proses pembuatan akun baru | Publik |
| `/login` | `GET, POST` | Halaman masuk & validasi akun pengguna | Publik |
| `/logout` | `GET` | Menghapus sesi aktif dan keluar dari aplikasi | User (Login) |
| `/profile` | `GET` | Menampilkan informasi akun pengguna | User (Login) |

2. Tabel Rute Film & Watchlist

| Route | Method | Deskripsi | Hak Akses |
| :--- | :---: | :--- | :---: |
| `/` | `GET` | Menampilkan halaman katalog film utama | Publik |
| `/movie/<id>` | `GET` | Menampilkan halaman detail spesifik dari suatu film | Publik |
| `/watchlist/add/<movie_id>` | `POST` | Menambahkan film ke dalam daftar tontonan | User (Login) |
| `/watchlist/delete/<movie_id>` | `POST / DELETE` | Menghapus film dari daftar tontonan | User (Login) |

📝 Lisensi
Proyek ini didistribusikan di bawah lisensi MIT License. Anda diperbolehkan memodifikasi, mendistribusikan, dan menggunakan kode ini untuk keperluan personal maupun komersial.

---

### Langkah 3: Push README ke GitHub
Kembali ke terminal PowerShell Anda, jalankan 3 perintah ringkas ini secara berurutan untuk mengirim file README tersebut ke repositori:

