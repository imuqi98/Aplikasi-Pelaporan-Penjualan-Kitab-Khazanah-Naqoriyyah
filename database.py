import sqlite3
from pathlib import Path


# ==========================================
# LOKASI DATABASE
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "penjualan_kitab.db"


# ==========================================
# KONEKSI DATABASE
# ==========================================

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Mengaktifkan foreign key
    conn.execute("PRAGMA foreign_keys = ON")

    return conn


# ==========================================
# MEMBUAT TABEL DATABASE
# ==========================================

def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    # --------------------------------------
    # TABEL PENGARANG
    # --------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_pengarang TEXT NOT NULL,
            singkatan TEXT
        )
    """)

    # --------------------------------------
    # TABEL KITAB
    # --------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kode_kitab TEXT UNIQUE,
            nama_kitab TEXT NOT NULL,
            author_id INTEGER,

            harga_modal REAL NOT NULL DEFAULT 0,

            persen_mahar REAL NOT NULL DEFAULT 0,
            harga_mahar REAL NOT NULL DEFAULT 0,

            persen_store REAL NOT NULL DEFAULT 0,
            persen_pemimpin REAL NOT NULL DEFAULT 0,
            persen_penulis REAL NOT NULL DEFAULT 0,

            FOREIGN KEY (author_id)
                REFERENCES authors(id)
        )
    """)

    # --------------------------------------
    # TABEL PENJUALAN
    # --------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            tanggal TEXT NOT NULL,
            kode_kitab TEXT,
            pembeli TEXT NOT NULL,
            jumlah INTEGER NOT NULL DEFAULT 1,

            harga_modal REAL NOT NULL DEFAULT 0,
            harga_mahar REAL NOT NULL DEFAULT 0,

            total_modal REAL NOT NULL DEFAULT 0,
            total_mahar REAL NOT NULL DEFAULT 0,

            keuntungan REAL NOT NULL DEFAULT 0,

            keuntungan_store REAL NOT NULL DEFAULT 0,
            keuntungan_pemimpin REAL NOT NULL DEFAULT 0,

            nama_penulis TEXT,
            keuntungan_penulis REAL NOT NULL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# DATA PENGARANG
# ==========================================

def get_authors():

    conn = get_connection()

    data = conn.execute("""
        SELECT *
        FROM authors
        ORDER BY nama_pengarang
    """).fetchall()

    conn.close()

    return data


def add_author(nama_pengarang, singkatan):

    conn = get_connection()

    conn.execute("""
        INSERT INTO authors
        (nama_pengarang, singkatan)
        VALUES (?, ?)
    """, (
        nama_pengarang,
        singkatan
    ))

    conn.commit()
    conn.close()


def delete_author(author_id):

    conn = get_connection()

    # Cek apakah pengarang masih digunakan oleh kitab
    book = conn.execute("""
        SELECT id
        FROM books
        WHERE author_id = ?
    """, (author_id,)).fetchone()

    if book:
        conn.close()
        return False

    conn.execute("""
        DELETE FROM authors
        WHERE id = ?
    """, (author_id,))

    conn.commit()
    conn.close()

    return True


# ==========================================
# DATA KITAB
# ==========================================

def get_books():

    conn = get_connection()

    data = conn.execute("""
        SELECT
            books.id,
            books.kode_kitab,
            books.nama_kitab,
            books.author_id,
            authors.nama_pengarang,
            authors.singkatan,
            books.harga_modal,
            books.persen_mahar,
            books.harga_mahar,
            books.persen_store,
            books.persen_pemimpin,
            books.persen_penulis
        FROM books
        LEFT JOIN authors
            ON books.author_id = authors.id
        ORDER BY books.nama_kitab
    """).fetchall()

    conn.close()

    return data


def add_book(
    kode_kitab,
    nama_kitab,
    author_id,
    harga_modal,
    persen_mahar,
    harga_mahar,
    persen_store,
    persen_pemimpin,
    persen_penulis
):

    conn = get_connection()

    conn.execute("""
        INSERT INTO books (
            kode_kitab,
            nama_kitab,
            author_id,
            harga_modal,
            persen_mahar,
            harga_mahar,
            persen_store,
            persen_pemimpin,
            persen_penulis
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        kode_kitab,
        nama_kitab,
        author_id,
        harga_modal,
        persen_mahar,
        harga_mahar,
        persen_store,
        persen_pemimpin,
        persen_penulis
    ))

    conn.commit()
    conn.close()


def delete_book(book_id):

    conn = get_connection()

    # Cek apakah kitab sudah pernah digunakan dalam transaksi
    book = conn.execute("""
        SELECT kode_kitab
        FROM books
        WHERE id = ?
    """, (book_id,)).fetchone()

    if not book:
        conn.close()
        return False

    sales = conn.execute("""
        SELECT id
        FROM sales
        WHERE kode_kitab = ?
        LIMIT 1
    """, (book["kode_kitab"],)).fetchone()

    if sales:
        conn.close()
        return False

    conn.execute("""
        DELETE FROM books
        WHERE id = ?
    """, (book_id,))

    conn.commit()
    conn.close()

    return True

# ==========================================
# DATA PENJUALAN
# ==========================================

def add_sale(
    tanggal,
    kode_kitab,
    pembeli,
    jumlah,
    harga_modal,
    harga_mahar,
    total_modal,
    total_mahar,
    keuntungan,
    keuntungan_store,
    keuntungan_pemimpin,
    nama_penulis,
    keuntungan_penulis
):

    conn = get_connection()

    conn.execute("""
        INSERT INTO sales (
            tanggal,
            kode_kitab,
            pembeli,
            jumlah,
            harga_modal,
            harga_mahar,
            total_modal,
            total_mahar,
            keuntungan,
            keuntungan_store,
            keuntungan_pemimpin,
            nama_penulis,
            keuntungan_penulis
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        tanggal,
        kode_kitab,
        pembeli,
        jumlah,
        harga_modal,
        harga_mahar,
        total_modal,
        total_mahar,
        keuntungan,
        keuntungan_store,
        keuntungan_pemimpin,
        nama_penulis,
        keuntungan_penulis
    ))

    conn.commit()
    conn.close()


def get_sales():

    conn = get_connection()

    rows = conn.execute("""
        SELECT
            sales.id,
            sales.tanggal,
            sales.kode_kitab,
            sales.pembeli,
            sales.jumlah,
            sales.harga_modal,
            sales.harga_mahar,
            sales.total_modal,
            sales.total_mahar,
            sales.keuntungan,
            sales.keuntungan_store,
            sales.keuntungan_pemimpin,
            sales.nama_penulis,
            sales.keuntungan_penulis,

            books.nama_kitab,
            authors.nama_pengarang

        FROM sales

        LEFT JOIN books
            ON sales.kode_kitab = books.kode_kitab

        LEFT JOIN authors
            ON books.author_id = authors.id

        ORDER BY
            sales.tanggal DESC,
            sales.id DESC

    """).fetchall()

    conn.close()

    # UBAH sqlite3.Row MENJADI DICTIONARY
    return [dict(row) for row in rows]


def delete_sale(sale_id):

    conn = get_connection()

    conn.execute("""
        DELETE FROM sales
        WHERE id = ?
    """, (sale_id,))

    conn.commit()
    conn.close()