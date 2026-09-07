import io

import pandas as pd
import streamlit as st

from database import (
    init_db,
    get_authors,
    add_author,
    delete_author,
    get_books,
    add_book,
    delete_book,
    add_sale,
    get_sales,
    delete_sale
)


# ============================================================
# INISIALISASI DATABASE
# ============================================================

init_db()


# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="Pelaporan Penjualan Kitab",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background-color: #06291d;
    min-width: 280px;
    max-width: 280px;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1rem;
}


/* ============================================================
   JUDUL SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] h2 {
    color: white;
    font-size: 21px;
    margin-bottom: 0;
}

section[data-testid="stSidebar"] hr {
    border-color: #174737;
}


/* ============================================================
   TEKS SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] p {
    color: #dceae5;
}


/* ============================================================
   MENU RADIO
   ============================================================ */

section[data-testid="stSidebar"]
div[data-testid="stRadio"] > div {
    gap: 5px;
}

section[data-testid="stSidebar"]
div[data-testid="stRadio"] label {
    background-color: transparent;
    border-radius: 12px;
    padding: 10px 14px;
    margin: 2px 5px;
    transition: 0.2s;
}

section[data-testid="stSidebar"]
div[data-testid="stRadio"] label:hover {
    background-color: #0b3d2c;
}

section[data-testid="stSidebar"]
div[data-testid="stRadio"] label p {
    color: #dceae5;
    font-size: 16px;
    font-weight: 500;
}


/* ============================================================
   RADIO BUTTON DISEMBUNYIKAN
   ============================================================ */

section[data-testid="stSidebar"]
div[data-testid="stRadio"] label > div:first-child {
    display: none;
}


/* ============================================================
   TOMBOL
   ============================================================ */

.stButton > button {
    border-radius: 9px;
    font-weight: 600;
}


/* ============================================================
   INPUT
   ============================================================ */

.stTextInput input,
.stNumberInput input,
.stDateInput input {
    border-radius: 8px;
}


/* ============================================================
   METRIC
   ============================================================ */

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 18px 20px;
}


/* ============================================================
   ALERT
   ============================================================ */

div[data-testid="stAlert"] {
    border-radius: 10px;
}


/* ============================================================
   EXPANDER
   ============================================================ */

div[data-testid="stExpander"] {
    border-radius: 12px;
}


/* ============================================================
   DATAFRAME
   ============================================================ */

div[data-testid="stDataFrame"] {
    border-radius: 10px;
}
/* ============================================================
   DASHBOARD
   ============================================================ */

.dashboard-title {
    font-size: 38px;
    font-weight: 750;
    color: #071b3a;
    margin-bottom: 0;
}

.dashboard-subtitle {
    font-size: 18px;
    color: #60708a;
    margin-top: 4px;
    margin-bottom: 30px;
}


/* FILTER */

.filter-box {
    background: white;
    border: 1px solid #dfe5ec;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 28px;
}


/* CARD */

.dashboard-card {
    background: white;
    border: 1px solid #dfe5ec;
    border-radius: 16px;
    padding: 25px;
    min-height: 150px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
}

.dashboard-card-title {
    color: #60708a;
    font-size: 15px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.dashboard-card-value {
    color: #071b3a;
    font-size: 30px;
    font-weight: 700;
    margin-top: 15px;
}


/* PANEL */

.dashboard-panel {
    background: white;
    border: 1px solid #dfe5ec;
    border-radius: 16px;
    padding: 25px;
    height: 100%;
}

.dashboard-panel-title {
    color: #071b3a;
    font-size: 23px;
    font-weight: 700;
    margin-bottom: 20px;
}


/* PROFIT ROW */

.profit-row {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 18px 0;

    border-bottom: 1px solid #edf0f4;
}

.profit-label {
    color: #60708a;
    font-size: 16px;
}

.profit-value {
    color: #071b3a;
    font-size: 19px;
    font-weight: 700;
}


/* BUTTON FILTER */

div[data-testid="stHorizontalBlock"] .stButton button {
    border-radius: 10px;
    min-height: 45px;
}


/* BACKGROUND */

.stApp {
    background-color: #f7f9fc;
}
/* ============================================================
   DASHBOARD
   ============================================================ */

.dashboard-title {
    font-size: 38px;
    font-weight: 750;
    color: #071b3a;
    margin-bottom: 5px;
}

.dashboard-subtitle {
    font-size: 18px;
    color: #60708a;
    margin-bottom: 25px;
}


/* METRIC */

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #dfe5ec;
    border-radius: 16px;
    padding: 22px;
    min-height: 145px;
}

div[data-testid="stMetricLabel"] {
    font-weight: 600;
}


/* BUTTON */

.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    min-height: 42px;
}


/* APP BACKGROUND */

.stApp {
    background-color: #f7f9fc;
}

/* ============================================================
   LAPORAN PENJUALAN
   ============================================================ */

.report-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5px;
}

.report-title {
    font-size: 38px;
    font-weight: 750;
    color: #071b3a;
}

.report-subtitle {
    color: #60708a;
    font-size: 17px;
    margin-bottom: 28px;
}

.report-profit {
    color: #087f5b;
    font-weight: 700;
}

.report-modal {
    color: #6b7c96;
}

.report-info {
    color: #60708a;
    font-size: 14px;
    margin-top: 12px;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #dfe5ec;
    border-radius: 14px;
    overflow: hidden;
}

div[data-testid="stDataFrame"] iframe {
    border-radius: 14px;
}

.report-filter-title {
    font-size: 18px;
    font-weight: 700;
    color: #071b3a;
    margin-bottom: 10px;
}


/* ============================================================
   BRAND / HEADER
   ============================================================ */
.brand-title {
    font-size: 34px;
    font-weight: 800;
    color: #126b45;
    line-height: 1.05;
    margin: 4px 0 2px 0;
}
.brand-title span { color: #c79616; }
.brand-subtitle {
    font-size: 19px;
    font-weight: 700;
    color: #172033;
    margin-bottom: 8px;
}
.brand-description {
    color: #667085;
    font-size: 14px;
    line-height: 1.5;
}
.quote-box {
    padding: 12px 8px;
    text-align: center;
    color: #17633f;
    font-style: italic;
    font-size: 16px;
    line-height: 1.5;
}
.logo-card {
    background: white;
    border: 1px solid #e6ebe8;
    border-radius: 18px;
    padding: 8px;
}
.shortcut-title {
    font-size: 17px;
    font-weight: 750;
    color: #172033;
    margin-top: 5px;
}
.shortcut-text {
    color: #667085;
    font-size: 13px;
}
.section-title {
    font-size: 22px;
    font-weight: 750;
    color: #172033;
}
.footer-note {
    text-align: center;
    color: #667085;
    font-size: 13px;
    padding: 18px 0 4px 0;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    if __import__("os").path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)

    st.markdown(
        "<div style='text-align:center;color:white;font-size:19px;font-weight:800;'>LP2K KHAZANAH<br>NAQORIYYAH</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<div style='text-align:center;color:#b8d6c8;font-size:13px;margin-top:6px;'>Sistem Pelaporan<br>Penjualan Kitab</div>",
        unsafe_allow_html=True
    )

    st.divider()
    st.markdown(
        "<span style='color:#789b8d;font-size:11px;font-weight:700;letter-spacing:1.2px;'>MENU UTAMA</span>",
        unsafe_allow_html=True
    )

    menu = st.radio(
        "Menu",
        [
            "🏠  Dashboard",
            "📖  Master Kitab",
            "👤  Master Pengarang",
            "🛒  Penjualan",
            "📄  Laporan Penjualan",
            "📊  Rekap Keuntungan"
        ],
        label_visibility="collapsed"
    )

    st.markdown(
        "<div style='position:relative;margin-top:55px;padding:18px 12px;background:#0b3d2c;border-radius:16px;text-align:center;color:#dceae5;font-size:12px;font-style:italic;line-height:1.5;'>\"Ilmu adalah warisan para nabi, dan kitab adalah jalannya.\"</div>",
        unsafe_allow_html=True
    )

# ============================================================
# DASHBOARD
# ============================================================

if menu == "🏠  Dashboard":

    from datetime import date, timedelta

    # ========================================================
    # AMBIL DATA
    # ========================================================
    sales = get_sales()
    df = pd.DataFrame(sales) if sales else pd.DataFrame()

    if not df.empty:
        df["tanggal_data"] = pd.to_datetime(
            df.get("tanggal"), errors="coerce"
        )

    # ========================================================
    # HEADER BRAND
    # ========================================================
    h1, h2, h3 = st.columns([1.25, 4.5, 2.0])

    with h1:
        if __import__("os").path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        else:
            st.markdown("### 📚")

    with h2:
        st.markdown(
            '<div class="brand-title">APLIKASI PELAPORAN <span>PENJUALAN KITAB</span></div>'
            '<div class="brand-subtitle">LP2K KHAZANAH NAQORIYYAH</div>'
            '<div class="brand-description">Sistem Informasi Pelaporan Penjualan Kitab untuk mendukung pengelolaan yang transparan dan amanah.</div>',
            unsafe_allow_html=True
        )

    with h3:
        st.markdown(
            '<div class="quote-box">"Bersama Kitab<br>Menuju Generasi<br>Berilmu dan Berakhlak"<br><br>━━━━</div>',
            unsafe_allow_html=True
        )

    st.write("")

    # ========================================================
    # FILTER PERIODE
    # ========================================================
    today = date.today()

    if not df.empty and df["tanggal_data"].notna().any():
        tanggal_valid = df["tanggal_data"].dropna()
        mulai_default = tanggal_valid.min().date()
        akhir_default = tanggal_valid.max().date()
    else:
        mulai_default = today
        akhir_default = today

    f1, f2, f3, f4, f5 = st.columns(5)
    with f1:
        btn_hari = st.button("Hari Ini", use_container_width=True, key="btn_hari")
    with f2:
        btn_minggu = st.button("Minggu Ini", use_container_width=True, key="btn_minggu")
    with f3:
        btn_bulan = st.button("Bulan Ini", use_container_width=True, key="btn_bulan")
    with f4:
        btn_tahun = st.button("Tahun Ini", use_container_width=True, key="btn_tahun")
    with f5:
        btn_semua = st.button("Semua Data", use_container_width=True, key="btn_semua")

    if btn_hari:
        mulai_default, akhir_default = today, today
    elif btn_minggu:
        mulai_default = today - timedelta(days=today.weekday())
        akhir_default = today
    elif btn_bulan:
        mulai_default = today.replace(day=1)
        akhir_default = today
    elif btn_tahun:
        mulai_default = today.replace(month=1, day=1)
        akhir_default = today
    elif btn_semua:
        if not df.empty and df["tanggal_data"].notna().any():
            tanggal_valid = df["tanggal_data"].dropna()
            mulai_default = tanggal_valid.min().date()
            akhir_default = tanggal_valid.max().date()

    d1, d2 = st.columns(2)
    with d1:
        tanggal_mulai = st.date_input("Dari", value=mulai_default, key="dashboard_tanggal_mulai")
    with d2:
        tanggal_akhir = st.date_input("Sampai", value=akhir_default, key="dashboard_tanggal_akhir")

    # ========================================================
    # FILTER DATA
    # ========================================================
    if not df.empty:
        df_filter = df.copy()
        df_filter = df_filter[df_filter["tanggal_data"] >= pd.Timestamp(tanggal_mulai)]
        df_filter = df_filter[df_filter["tanggal_data"] < pd.Timestamp(tanggal_akhir) + pd.Timedelta(days=1)]
    else:
        df_filter = pd.DataFrame()

    def nilai_kolom(dataframe, nama_kolom):
        if nama_kolom in dataframe.columns:
            return pd.to_numeric(dataframe[nama_kolom], errors="coerce").fillna(0)
        return pd.Series(0.0, index=dataframe.index)

    total_transaksi = len(df_filter)
    total_jp = nilai_kolom(df_filter, "jumlah").sum()
    total_mahar = nilai_kolom(df_filter, "total_mahar").sum()
    total_modal = nilai_kolom(df_filter, "total_modal").sum()
    total_keuntungan = total_mahar - total_modal

    # ========================================================
    # STATISTIK
    # ========================================================
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("🛒 Total Transaksi", f"{total_transaksi:,}")
    with c2:
        st.metric("📖 Total Kitab Terjual", f"{total_jp:,.0f}")
    with c3:
        st.metric("💰 Total Mahar", f"Rp {total_mahar:,.0f}")
    with c4:
        st.metric("📈 Total Keuntungan", f"Rp {total_keuntungan:,.0f}")

    st.write("")

    # ========================================================
    # SHORTCUT MENU
    # ========================================================
    st.markdown('<div class="section-title">Menu Cepat</div>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    shortcuts = [
        (s1, "👤", "Data Pengarang", "Kelola data pengarang kitab."),
        (s2, "📖", "Data Kitab", "Kelola data kitab dan harga."),
        (s3, "🛒", "Transaksi Penjualan", "Catat transaksi penjualan."),
        (s4, "📊", "Laporan", "Lihat rekap dan laporan."),
    ]
    for col, icon, title, desc in shortcuts:
        with col:
            with st.container(border=True):
                st.markdown(f"<div style='font-size:30px'>{icon}</div><div class='shortcut-title'>{title}</div><div class='shortcut-text'>{desc}</div>", unsafe_allow_html=True)

    st.write("")

    # ========================================================
    # TRANSAKSI TERBARU
    # ========================================================
    left, right = st.columns([2.1, 1])

    with left:
        with st.container(border=True):
            st.markdown('<div class="section-title">🕘 Transaksi Terbaru</div>', unsafe_allow_html=True)
            if not df_filter.empty:
                terbaru = df_filter.sort_values("tanggal_data", ascending=False).head(5).copy()
                tabel = pd.DataFrame({
                    "Tanggal": terbaru["tanggal_data"].dt.strftime("%Y-%m-%d"),
                    "Nama Kitab": terbaru.get("nama_kitab", "-"),
                    "Pengarang": terbaru.get("nama_pengarang", "-"),
                    "Pemahar": terbaru.get("pembeli", "-"),
                    "Jumlah": nilai_kolom(terbaru, "jumlah").astype(int),
                    "Mahar": nilai_kolom(terbaru, "total_mahar").map(lambda x: f"Rp {x:,.0f}"),
                    "Keuntungan": nilai_kolom(terbaru, "keuntungan").map(lambda x: f"Rp {x:,.0f}"),
                })
                st.dataframe(tabel, use_container_width=True, hide_index=True)
            else:
                st.info("Belum ada transaksi pada periode yang dipilih.")

    with right:
        with st.container(border=True):
            st.markdown('<div class="section-title">💼 Pembagian Keuntungan</div>', unsafe_allow_html=True)
            total_store = nilai_kolom(df_filter, "keuntungan_store").sum()
            total_pemimpin = nilai_kolom(df_filter, "keuntungan_pemimpin").sum()
            total_penulis = nilai_kolom(df_filter, "keuntungan_penulis").sum()
            st.metric("🏪 Store", f"Rp {total_store:,.0f}")
            st.metric("👑 Pemimpin", f"Rp {total_pemimpin:,.0f}")
            st.metric("✍️ Penulis", f"Rp {total_penulis:,.0f}")

    st.write("")

    # ========================================================
    # GRAFIK
    # ========================================================
    with st.container(border=True):
        st.markdown('<div class="section-title">📈 Grafik Penjualan & Keuntungan</div>', unsafe_allow_html=True)
        if not df_filter.empty:
            grafik = df_filter.copy()
            grafik["Tanggal"] = grafik["tanggal_data"].dt.strftime("%d-%m")
            grafik_tampil = pd.DataFrame({
                "Penjualan": nilai_kolom(grafik, "total_mahar").values,
                "Keuntungan": nilai_kolom(grafik, "keuntungan").values,
            }, index=grafik["Tanggal"])
            st.line_chart(grafik_tampil, use_container_width=True)
        else:
            st.info("Belum ada data untuk ditampilkan.")

    st.markdown(
        '<div class="footer-note">© 2026 LP2K Khazanah Naqoriyyah &nbsp; | &nbsp; Aplikasi Pelaporan Penjualan Kitab</div>',
        unsafe_allow_html=True
    )

# ============================================================
# MASTER KITAB
# ============================================================

elif menu == "📖  Master Kitab":

    st.title("📖 Master Kitab")

    st.write(
        "Kelola data kitab, harga modal, harga mahar, "
        "dan pembagian keuntungan."
    )

    st.divider()

    authors = get_authors()

    if len(authors) == 0:

        st.warning(
            "Belum ada data pengarang."
        )

        st.info(
            "Silakan tambahkan pengarang terlebih dahulu "
            "di menu Master Pengarang."
        )

    else:

        st.subheader("➕ Tambah Kitab")

        author_options = {}

        for author in authors:

            label = (
                f"{author['nama_pengarang']} "
                f"({author['singkatan'] or '-'})"
            )

            author_options[label] = author["id"]

        with st.form("form_tambah_kitab"):

            st.markdown("### 📖 Data Kitab")

            col1, col2 = st.columns(2)

            with col1:

                kode_kitab = st.text_input(
                    "Kode Kitab",
                    placeholder="Contoh: TBM001"
                )

                nama_kitab = st.text_input(
                    "Nama Kitab",
                    placeholder="Contoh: Tanbihul Masyi"
                )

                pilihan_pengarang = st.selectbox(
                    "Pengarang",
                    list(author_options.keys())
                )

            with col2:

                harga_modal = st.number_input(
                    "Harga Modal / Kitab",
                    min_value=0.0,
                    value=0.0,
                    step=1000.0,
                    format="%.0f"
                )

                persen_mahar = st.number_input(
                    "% Kenaikan Mahar",
                    min_value=0.0,
                    max_value=1000.0,
                    value=100.0,
                    step=5.0
                )

            st.markdown(
                "### 💰 Pembagian Keuntungan"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                persen_store = st.number_input(
                    "% Store",
                    min_value=0.0,
                    max_value=100.0,
                    value=30.0,
                    step=5.0
                )

            with col2:

                persen_pemimpin = st.number_input(
                    "% Pemimpin",
                    min_value=0.0,
                    max_value=100.0,
                    value=20.0,
                    step=5.0
                )

            with col3:

                persen_penulis = st.number_input(
                    "% Penulis",
                    min_value=0.0,
                    max_value=100.0,
                    value=50.0,
                    step=5.0
                )

            harga_mahar = (
                harga_modal
                * (1 + persen_mahar / 100)
            )

            total_persen = (
                persen_store
                + persen_pemimpin
                + persen_penulis
            )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"Harga Mahar / Kitab: "
                    f"Rp {harga_mahar:,.0f}"
                )

            with col2:

                if total_persen == 100:

                    st.success(
                        f"Pembagian {total_persen:.0f}% ✓"
                    )

                else:

                    st.error(
                        f"Pembagian {total_persen:.0f}% "
                        f"(harus 100%)"
                    )

            simpan = st.form_submit_button(
                "💾 Simpan Kitab",
                use_container_width=True
            )

            if simpan:

                if not kode_kitab.strip():

                    st.error(
                        "Kode kitab wajib diisi."
                    )

                elif not nama_kitab.strip():

                    st.error(
                        "Nama kitab wajib diisi."
                    )

                elif harga_modal <= 0:

                    st.error(
                        "Harga modal harus lebih dari 0."
                    )

                elif total_persen != 100:

                    st.error(
                        "Persentase Store + Pemimpin + "
                        "Penulis harus tepat 100%."
                    )

                else:

                    author_id = author_options[
                        pilihan_pengarang
                    ]

                    try:

                        add_book(
                            kode_kitab.strip(),
                            nama_kitab.strip(),
                            author_id,
                            harga_modal,
                            persen_mahar,
                            harga_mahar,
                            persen_store,
                            persen_pemimpin,
                            persen_penulis
                        )

                        st.success(
                            "Kitab berhasil ditambahkan."
                        )

                        st.rerun()

                    except Exception as e:

                        st.error(
                            f"Gagal menyimpan kitab: {e}"
                        )

    st.divider()

    st.subheader("📋 Daftar Kitab")

    books = get_books()

    if len(books) == 0:

        st.info(
            "Belum ada data kitab."
        )

    else:

        for book in books:

            with st.expander(
                f"📖 {book['nama_kitab']} "
                f"— {book['kode_kitab']}"
            ):

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Kode Kitab:** "
                        f"{book['kode_kitab']}"
                    )

                    st.write(
                        f"**Nama Kitab:** "
                        f"{book['nama_kitab']}"
                    )

                    st.write(
                        f"**Pengarang:** "
                        f"{book['nama_pengarang'] or '-'}"
                    )

                    st.write(
                        f"**Singkatan:** "
                        f"{book['singkatan'] or '-'}"
                    )

                    st.write(
                        f"**Harga Modal:** "
                        f"Rp {book['harga_modal']:,.0f}"
                    )

                with col2:

                    st.write(
                        f"**Kenaikan Mahar:** "
                        f"{book['persen_mahar']:.0f}%"
                    )

                    st.write(
                        f"**Harga Mahar:** "
                        f"Rp {book['harga_mahar']:,.0f}"
                    )

                    st.write(
                        f"**Store:** "
                        f"{book['persen_store']:.0f}%"
                    )

                    st.write(
                        f"**Pemimpin:** "
                        f"{book['persen_pemimpin']:.0f}%"
                    )

                    st.write(
                        f"**Penulis:** "
                        f"{book['persen_penulis']:.0f}%"
                    )

                if st.button(
                    "🗑️ Hapus Kitab",
                    key=f"hapus_kitab_{book['id']}"
                ):

                    berhasil = delete_book(
                        book["id"]
                    )

                    if berhasil:

                        st.success(
                            "Kitab berhasil dihapus."
                        )

                    else:

                        st.error(
                            "Kitab tidak dapat dihapus "
                            "karena sudah digunakan dalam transaksi."
                        )

                    st.rerun()


# ============================================================
# MASTER PENGARANG
# ============================================================

elif menu == "👤  Master Pengarang":

    st.title("👤 Master Pengarang")

    st.write(
        "Kelola nama pengarang dan singkatan."
    )

    st.divider()

    st.subheader("➕ Tambah Pengarang")

    with st.form("form_tambah_pengarang"):

        col1, col2 = st.columns(2)

        with col1:

            nama_pengarang = st.text_input(
                "Nama Pengarang",
                placeholder="Masukkan nama pengarang"
            )

        with col2:

            singkatan = st.text_input(
                "Singkatan",
                placeholder="Contoh: AHM"
            )

        simpan = st.form_submit_button(
            "💾 Simpan Pengarang",
            use_container_width=True
        )

        if simpan:

            if not nama_pengarang.strip():

                st.error(
                    "Nama pengarang wajib diisi."
                )

            else:

                try:

                    add_author(
                        nama_pengarang.strip(),
                        singkatan.strip()
                    )

                    st.success(
                        "Pengarang berhasil ditambahkan."
                    )

                    st.rerun()

                except Exception as e:

                    st.error(
                        f"Gagal menyimpan pengarang: {e}"
                    )

    st.divider()

    st.subheader("📋 Daftar Pengarang")

    authors = get_authors()

    if len(authors) == 0:

        st.info(
            "Belum ada data pengarang."
        )

    else:

        for author in authors:

            col1, col2, col3 = st.columns(
                [1, 5, 2]
            )

            with col1:

                st.write(
                    f"**{author['id']}**"
                )

            with col2:

                st.write(
                    f"**{author['nama_pengarang']}**"
                )

                st.caption(
                    f"Singkatan: "
                    f"{author['singkatan'] or '-'}"
                )

            with col3:

                if st.button(
                    "🗑️ Hapus",
                    key=f"hapus_pengarang_{author['id']}"
                ):

                    berhasil = delete_author(
                        author["id"]
                    )

                    if berhasil:

                        st.success(
                            "Pengarang berhasil dihapus."
                        )

                    else:

                        st.error(
                            "Pengarang tidak dapat dihapus "
                            "karena masih digunakan."
                        )

                    st.rerun()


# ============================================================
# PENJUALAN
# ============================================================

elif menu == "🛒  Penjualan":

    st.title("🛒 Penjualan Kitab")

    st.write(
        "Input transaksi penjualan kitab."
    )

    st.divider()

    books = get_books()

    if len(books) == 0:

        st.warning(
            "Belum ada data kitab."
        )

        st.info(
            "Silakan tambahkan kitab terlebih dahulu "
            "di menu Master Kitab."
        )

    else:

        book_options = {}

        for book in books:

            label = (
                f"{book['nama_kitab']} "
                f"({book['kode_kitab']})"
            )

            book_options[label] = book

        st.subheader("➕ Input Penjualan")

        with st.form("form_penjualan"):

            col1, col2 = st.columns(2)

            with col1:

                tanggal = st.date_input(
                    "Tanggal Penjualan"
                )

                pembeli = st.text_input(
                    "Nama Pemahar",
                    placeholder="Masukkan nama pemahar"
                )

            with col2:

                pilihan_kitab = st.selectbox(
                    "Pilih Kitab",
                    list(book_options.keys())
                )

                jumlah = st.number_input(
                    "Jumlah / JP",
                    min_value=1,
                    value=1,
                    step=1
                )

            selected_book = book_options[
                pilihan_kitab
            ]

            kode_kitab = selected_book[
                "kode_kitab"
            ]

            nama_kitab = selected_book[
                "nama_kitab"
            ]

            nama_penulis = (
                selected_book["nama_pengarang"]
                or "-"
            )

            harga_modal = float(
                selected_book["harga_modal"]
            )

            harga_mahar = float(
                selected_book["harga_mahar"]
            )

            persen_store = float(
                selected_book["persen_store"]
            )

            persen_pemimpin = float(
                selected_book["persen_pemimpin"]
            )

            persen_penulis = float(
                selected_book["persen_penulis"]
            )

            # ------------------------------------------------
            # PERHITUNGAN
            # ------------------------------------------------

            total_modal = (
                harga_modal * jumlah
            )

            total_mahar = (
                harga_mahar * jumlah
            )

            keuntungan = (
                total_mahar - total_modal
            )

            keuntungan_store = (
                keuntungan
                * persen_store
                / 100
            )

            keuntungan_pemimpin = (
                keuntungan
                * persen_pemimpin
                / 100
            )

            keuntungan_penulis = (
                keuntungan
                * persen_penulis
                / 100
            )

            # ------------------------------------------------
            # INFORMASI
            # ------------------------------------------------

            st.divider()

            st.subheader(
                "📖 Informasi Kitab"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"**Kode:** {kode_kitab}"
                )

                st.write(
                    f"**Kitab:** {nama_kitab}"
                )

            with col2:

                st.write(
                    f"**Penulis:** {nama_penulis}"
                )

                st.write(
                    f"**Modal / Kitab:** "
                    f"Rp {harga_modal:,.0f}"
                )

            with col3:

                st.write(
                    f"**Mahar / Kitab:** "
                    f"Rp {harga_mahar:,.0f}"
                )

                st.write(
                    f"**JP:** {jumlah}"
                )

            st.subheader(
                "💰 Ringkasan Transaksi"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "Total Modal",
                    f"Rp {total_modal:,.0f}"
                )

            with col2:

                st.metric(
                    "Total Mahar",
                    f"Rp {total_mahar:,.0f}"
                )

            with col3:

                st.metric(
                    "Keuntungan",
                    f"Rp {keuntungan:,.0f}"
                )

            with col4:

                st.metric(
                    "JP",
                    f"{jumlah}"
                )

            st.subheader(
                "📊 Pembagian Keuntungan"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"**Store ({persen_store:.0f}%)**"
                )

                st.success(
                    f"Rp {keuntungan_store:,.0f}"
                )

            with col2:

                st.write(
                    f"**Pemimpin "
                    f"({persen_pemimpin:.0f}%)**"
                )

                st.info(
                    f"Rp {keuntungan_pemimpin:,.0f}"
                )

            with col3:

                st.write(
                    f"**Penulis "
                    f"({persen_penulis:.0f}%)**"
                )

                st.warning(
                    f"Rp {keuntungan_penulis:,.0f}"
                )

            st.divider()

            simpan = st.form_submit_button(
                "💾 Simpan Transaksi",
                use_container_width=True
            )

            if simpan:

                if not pembeli.strip():

                    st.error(
                        "Nama pemahar wajib diisi."
                    )

                else:

                    try:

                        add_sale(
                            tanggal=str(tanggal),
                            kode_kitab=kode_kitab,
                            pembeli=pembeli.strip(),
                            jumlah=jumlah,
                            harga_modal=harga_modal,
                            harga_mahar=harga_mahar,
                            total_modal=total_modal,
                            total_mahar=total_mahar,
                            keuntungan=keuntungan,
                            keuntungan_store=keuntungan_store,
                            keuntungan_pemimpin=keuntungan_pemimpin,
                            nama_penulis=nama_penulis,
                            keuntungan_penulis=keuntungan_penulis
                        )

                        st.success(
                            "Transaksi berhasil disimpan."
                        )

                        st.rerun()

                    except Exception as e:

                        st.error(
                            f"Gagal menyimpan transaksi: {e}"
                        )

    # --------------------------------------------------------
    # RIWAYAT PENJUALAN
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "📋 Riwayat Penjualan"
    )

    sales = get_sales()

    if len(sales) == 0:

        st.info(
            "Belum ada transaksi penjualan."
        )

    else:

        for sale in sales:

            with st.expander(
                f"📅 {sale['tanggal']} | "
                f"{sale['nama_kitab'] or sale['kode_kitab']} | "
                f"{sale['pembeli']}"
            ):

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Tanggal:** {sale['tanggal']}"
                    )

                    st.write(
                        f"**Pemahar:** {sale['pembeli']}"
                    )

                    st.write(
                        f"**Kitab:** "
                        f"{sale['nama_kitab'] or '-'}"
                    )

                    st.write(
                        f"**Kode:** "
                        f"{sale['kode_kitab'] or '-'}"
                    )

                    st.write(
                        f"**JP:** {sale['jumlah']}"
                    )

                    st.write(
                        f"**Penulis:** "
                        f"{sale['nama_penulis'] or '-'}"
                    )

                with col2:

                    st.write(
                        f"**Modal / Kitab:** "
                        f"Rp {sale['harga_modal']:,.0f}"
                    )

                    st.write(
                        f"**Mahar / Kitab:** "
                        f"Rp {sale['harga_mahar']:,.0f}"
                    )

                    st.write(
                        f"**Total Modal:** "
                        f"Rp {sale['total_modal']:,.0f}"
                    )

                    st.write(
                        f"**Total Mahar:** "
                        f"Rp {sale['total_mahar']:,.0f}"
                    )

                    st.write(
                        f"**Keuntungan:** "
                        f"Rp {sale['keuntungan']:,.0f}"
                    )

                st.divider()

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.write("**Store**")

                    st.write(
                        f"Rp {sale['keuntungan_store']:,.0f}"
                    )

                with col2:

                    st.write("**Pemimpin**")

                    st.write(
                        f"Rp {sale['keuntungan_pemimpin']:,.0f}"
                    )

                with col3:

                    st.write("**Penulis**")

                    st.write(
                        f"Rp {sale['keuntungan_penulis']:,.0f}"
                    )

                if st.button(
                    "🗑️ Hapus Transaksi",
                    key=f"hapus_transaksi_{sale['id']}"
                ):

                    delete_sale(
                        sale["id"]
                    )

                    st.success(
                        "Transaksi berhasil dihapus."
                    )

                    st.rerun()


# ============================================================
# ============================================================
# LAPORAN PENJUALAN
# ============================================================

elif menu == "📄  Laporan Penjualan":

    from datetime import date
    from io import BytesIO

    st.markdown(
        '<div class="report-title">Laporan Penjualan</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="report-subtitle">'
        'Detail seluruh transaksi dengan filter, sortir, dan export.'
        '</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # AMBIL DATA
    # ========================================================

    sales = get_sales()
    books = get_books()

    # PENTING:
    # get_sales() mengembalikan sqlite3.Row.
    # sqlite3.Row harus diubah menjadi dictionary sebelum
    # dimasukkan ke DataFrame agar nama kolom terbaca benar.
    if sales:
        df = pd.DataFrame([dict(row) for row in sales])
    else:
        df = pd.DataFrame()

    # ========================================================
    # SIAPKAN MASTER KITAB
    # ========================================================

    book_map = {}

    for book in books:
        b = dict(book)
        kode = str(b.get("kode_kitab", "") or "").strip()

        if kode:
            book_map[kode] = b

    # ========================================================
    # SIAPKAN DATA
    # ========================================================

    if not df.empty:

        # -------------------------------
        # TANGGAL
        # -------------------------------

        if "tanggal" in df.columns:
            df["_tanggal"] = pd.to_datetime(
                df["tanggal"],
                errors="coerce"
            )
        else:
            df["_tanggal"] = pd.NaT

        # -------------------------------
        # KODE
        # -------------------------------

        if "kode_kitab" not in df.columns:
            df["kode_kitab"] = ""

        df["kode_kitab"] = (
            df["kode_kitab"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        # -------------------------------
        # NAMA KITAB
        # -------------------------------

        if "nama_kitab" not in df.columns:
            df["nama_kitab"] = ""

        # Jika nama kitab kosong, ambil dari Master Kitab
        df["nama_kitab"] = df.apply(
            lambda row: (
                row["nama_kitab"]
                if pd.notna(row["nama_kitab"])
                and str(row["nama_kitab"]).strip()
                else book_map.get(
                    row["kode_kitab"], {}
                ).get("nama_kitab", "")
            ),
            axis=1
        )

        # -------------------------------
        # PEMAHAR
        # -------------------------------

        if "pembeli" not in df.columns:
            if "pemahar" in df.columns:
                df["pembeli"] = df["pemahar"]
            else:
                df["pembeli"] = ""

        df["pembeli"] = (
            df["pembeli"]
            .fillna("")
            .astype(str)
        )

        # -------------------------------
        # JUMLAH / JP
        # -------------------------------

        if "jumlah" not in df.columns:
            df["jumlah"] = 0

        df["jumlah"] = pd.to_numeric(
            df["jumlah"],
            errors="coerce"
        ).fillna(0)

        # -------------------------------
        # TOTAL MAHAR
        # -------------------------------

        if "total_mahar" not in df.columns:
            df["total_mahar"] = 0

        df["total_mahar"] = pd.to_numeric(
            df["total_mahar"],
            errors="coerce"
        ).fillna(0)

        # -------------------------------
        # TOTAL MODAL / MODKIRP
        # -------------------------------

        if "total_modal" not in df.columns:
            if "MODKIRP" in df.columns:
                df["total_modal"] = df["MODKIRP"]
            else:
                df["total_modal"] = 0

        df["total_modal"] = pd.to_numeric(
            df["total_modal"],
            errors="coerce"
        ).fillna(0)

        # -------------------------------
        # KEUNTUNGAN
        # -------------------------------

        if "keuntungan" not in df.columns:
            df["keuntungan"] = (
                df["total_mahar"]
                - df["total_modal"]
            )

        df["keuntungan"] = pd.to_numeric(
            df["keuntungan"],
            errors="coerce"
        ).fillna(0)

        # -------------------------------
        # STORE
        # -------------------------------

        if "keuntungan_store" not in df.columns:
            if "STORE" in df.columns:
                df["keuntungan_store"] = df["STORE"]
            else:
                df["keuntungan_store"] = 0

        df["keuntungan_store"] = pd.to_numeric(
            df["keuntungan_store"],
            errors="coerce"
        ).fillna(0)

        # -------------------------------
        # PEMIMPIN
        # -------------------------------

        if "keuntungan_pemimpin" not in df.columns:
            if "PEMIMPIN" in df.columns:
                df["keuntungan_pemimpin"] = df["PEMIMPIN"]
            elif "pemimpin" in df.columns:
                df["keuntungan_pemimpin"] = df["pemimpin"]
            else:
                df["keuntungan_pemimpin"] = 0

        df["keuntungan_pemimpin"] = pd.to_numeric(
            df["keuntungan_pemimpin"],
            errors="coerce"
        ).fillna(0)

        # -------------------------------
        # PENULIS
        # -------------------------------

        if "nama_penulis" not in df.columns:
            df["nama_penulis"] = ""

        # Ambil singkatan penulis dari Master Kitab.
        # Ini membuat tabel sesuai tampilan contoh:
        # ULH, UAK, UMF, dst.
        df["singkatan_penulis"] = df.apply(
            lambda row: (
                book_map.get(
                    row["kode_kitab"], {}
                ).get("singkatan", "")
                or row.get("nama_penulis", "")
                or "-"
            ),
            axis=1
        )

        # -------------------------------
        # KEUNTUNGAN PENULIS
        # -------------------------------

        if "keuntungan_penulis" not in df.columns:
            df["keuntungan_penulis"] = 0

        df["keuntungan_penulis"] = pd.to_numeric(
            df["keuntungan_penulis"],
            errors="coerce"
        ).fillna(0)

        # -------------------------------
        # PENGARANG
        # -------------------------------

        df["nama_pengarang"] = df.apply(
            lambda row: book_map.get(
                row["kode_kitab"], {}
            ).get("nama_pengarang", ""),
            axis=1
        )

    # ========================================================
    # FILTER LAPORAN
    # ========================================================

    with st.container(border=True):

        st.markdown(
            '<div class="report-filter-title">'
            '🔎 Filter Laporan'
            '</div>',
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # TANGGAL
        # ----------------------------------------------------

        if not df.empty:

            tanggal_valid = df["_tanggal"].dropna()

            if len(tanggal_valid) > 0:
                tanggal_awal_default = (
                    tanggal_valid.min().date()
                )
                tanggal_akhir_default = (
                    tanggal_valid.max().date()
                )
            else:
                tanggal_awal_default = date.today()
                tanggal_akhir_default = date.today()

        else:
            tanggal_awal_default = date.today()
            tanggal_akhir_default = date.today()

        col1, col2 = st.columns(2)

        with col1:
            tanggal_mulai = st.date_input(
                "Dari Tanggal",
                value=tanggal_awal_default,
                key="laporan_tanggal_mulai"
            )

        with col2:
            tanggal_akhir = st.date_input(
                "Sampai Tanggal",
                value=tanggal_akhir_default,
                key="laporan_tanggal_akhir"
            )

        # ----------------------------------------------------
        # FILTER LAIN
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            if not df.empty:
                daftar_pemahar = sorted(
                    [
                        str(x)
                        for x in df["pembeli"]
                        .dropna()
                        .unique()
                        if str(x).strip()
                    ]
                )
            else:
                daftar_pemahar = []

            pemahar_filter = st.selectbox(
                "Pemahar",
                ["Semua Pemahar"] + daftar_pemahar,
                key="laporan_pemahar"
            )

        with col2:

            daftar_pengarang = [
                "Semua Pengarang"
            ]

            if not df.empty and "nama_pengarang" in df.columns:
                daftar_pengarang += sorted(
                    [
                        str(x)
                        for x in df["nama_pengarang"]
                        .dropna()
                        .unique()
                        if str(x).strip()
                    ]
                )

            pengarang_filter = st.selectbox(
                "Pengarang",
                daftar_pengarang,
                key="laporan_pengarang"
            )

        with col3:

            if not df.empty:
                daftar_kode = sorted(
                    [
                        str(x)
                        for x in df["kode_kitab"]
                        .dropna()
                        .unique()
                        if str(x).strip()
                    ]
                )
            else:
                daftar_kode = []

            kode_filter = st.selectbox(
                "Kode Kitab",
                ["Semua Kode"] + daftar_kode,
                key="laporan_kode"
            )

        # ----------------------------------------------------
        # TOMBOL
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:
            st.button(
                "🔍 Terapkan",
                use_container_width=True,
                type="primary",
                key="laporan_terapkan"
            )

        with col2:
            if st.button(
                "↻ Reset",
                use_container_width=True,
                key="laporan_reset"
            ):
                st.session_state["laporan_tanggal_mulai"] = tanggal_awal_default
                st.session_state["laporan_tanggal_akhir"] = tanggal_akhir_default
                st.session_state["laporan_pemahar"] = "Semua Pemahar"
                st.session_state["laporan_pengarang"] = "Semua Pengarang"
                st.session_state["laporan_kode"] = "Semua Kode"
                st.rerun()

    # ========================================================
    # VALIDASI TANGGAL
    # ========================================================

    if tanggal_mulai > tanggal_akhir:

        st.error(
            "Tanggal mulai tidak boleh lebih besar "
            "dari tanggal akhir."
        )

        st.stop()

    # ========================================================
    # FILTER DATA
    # ========================================================

    if not df.empty:

        laporan = df.copy()

        # Tanggal awal
        tanggal_mulai_ts = pd.Timestamp(
            tanggal_mulai
        )

        laporan = laporan[
            laporan["_tanggal"] >= tanggal_mulai_ts
        ].copy()

        # Tanggal akhir dibuat eksklusif
        # supaya transaksi pada tanggal akhir tetap masuk.
        tanggal_akhir_ts = (
            pd.Timestamp(tanggal_akhir)
            + pd.Timedelta(days=1)
        )

        laporan = laporan[
            laporan["_tanggal"] < tanggal_akhir_ts
        ].copy()

        # Pemahar
        if pemahar_filter != "Semua Pemahar":
            laporan = laporan[
                laporan["pembeli"].astype(str)
                == pemahar_filter
            ].copy()

        # Kode kitab
        if kode_filter != "Semua Kode":
            laporan = laporan[
                laporan["kode_kitab"].astype(str)
                == kode_filter
            ].copy()

        # Pengarang
        if pengarang_filter != "Semua Pengarang":
            laporan = laporan[
                laporan["nama_pengarang"].astype(str)
                == pengarang_filter
            ].copy()

    else:
        laporan = pd.DataFrame()

    # ========================================================
    # SORTING
    # ========================================================

    if not laporan.empty:
        laporan = laporan.sort_values(
            "_tanggal",
            ascending=False
        )

    # ========================================================
    # TABEL LAPORAN
    # ========================================================

    st.write("")

    with st.container(border=True):

        st.subheader("📋 Detail Penjualan")

        if laporan.empty:

            st.info(
                "Tidak ada data transaksi "
                "sesuai filter."
            )

        else:

            tabel = pd.DataFrame()

            # Tanggal
            tabel["Tanggal"] = (
                laporan["_tanggal"]
                .dt.strftime("%d %b\n%Y")
            )

            # Kode
            tabel["Kode"] = (
                laporan["kode_kitab"]
                .astype(str)
            )

            # Pemahar
            tabel["Pemahar"] = (
                laporan["pembeli"]
                .astype(str)
            )

            # Nama Kitab
            tabel["Nama Kitab"] = (
                laporan["nama_kitab"]
                .astype(str)
            )

            # JP
            tabel["JP"] = pd.to_numeric(
                laporan["jumlah"],
                errors="coerce"
            ).fillna(0).astype(int)

            # Mahar
            tabel["Mahar"] = pd.to_numeric(
                laporan["total_mahar"],
                errors="coerce"
            ).fillna(0)

            # MODKIRP = TOTAL MODAL
            tabel["MODKIRP"] = pd.to_numeric(
                laporan["total_modal"],
                errors="coerce"
            ).fillna(0)

            # Keuntungan
            tabel["Keuntungan"] = pd.to_numeric(
                laporan["keuntungan"],
                errors="coerce"
            ).fillna(0)

            # K. Store
            tabel["K. Store"] = pd.to_numeric(
                laporan["keuntungan_store"],
                errors="coerce"
            ).fillna(0)

            # K. Pemimpin
            tabel["K. Pemimpin"] = pd.to_numeric(
                laporan["keuntungan_pemimpin"],
                errors="coerce"
            ).fillna(0)

            # Penulis / Singkatan
            tabel["Penulis"] = (
                laporan["singkatan_penulis"]
                .astype(str)
            )

            # ------------------------------------------------
            # FORMAT RUPIAH
            # ------------------------------------------------

            kolom_uang = [
                "Mahar",
                "MODKIRP",
                "Keuntungan",
                "K. Store",
                "K. Pemimpin"
            ]

            for kolom in kolom_uang:
                tabel[kolom] = tabel[kolom].apply(
                    lambda x: f"Rp{float(x):,.0f}"
                )

            # ------------------------------------------------
            # TAMPILKAN
            # ------------------------------------------------

            st.dataframe(
                tabel,
                use_container_width=True,
                hide_index=True,
                height=500
            )

            st.caption(
                f"Menampilkan 1–{len(tabel)} "
                f"dari {len(tabel)} data"
            )

            # ------------------------------------------------
            # TOTAL
            # ------------------------------------------------

            total_jp = pd.to_numeric(
                laporan["jumlah"],
                errors="coerce"
            ).fillna(0).sum()

            total_mahar = pd.to_numeric(
                laporan["total_mahar"],
                errors="coerce"
            ).fillna(0).sum()

            total_modal = pd.to_numeric(
                laporan["total_modal"],
                errors="coerce"
            ).fillna(0).sum()

            total_keuntungan = (
                total_mahar - total_modal
            )

            st.divider()

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Total JP",
                    f"{total_jp:,.0f}"
                )

            with col2:
                st.metric(
                    "Total Mahar",
                    f"Rp{total_mahar:,.0f}"
                )

            with col3:
                st.metric(
                    "Total Modal",
                    f"Rp{total_modal:,.0f}"
                )

            with col4:
                st.metric(
                    "Total Keuntungan",
                    f"Rp{total_keuntungan:,.0f}"
                )

    # ========================================================
    # EXPORT
    # ========================================================

    if not laporan.empty:

        st.write("")
        st.subheader("📥 Export Laporan")

        col1, col2, col3 = st.columns(3)

        with col1:

            csv_data = tabel.to_csv(
                index=False
            ).encode("utf-8-sig")

            st.download_button(
                "⬇️ CSV",
                data=csv_data,
                file_name="laporan_penjualan.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col2:

            excel_buffer = BytesIO()

            with pd.ExcelWriter(
                excel_buffer,
                engine="openpyxl"
            ) as writer:

                tabel.to_excel(
                    writer,
                    index=False,
                    sheet_name="Laporan Penjualan"
                )

            excel_buffer.seek(0)

            st.download_button(
                "⬇️ Excel",
                data=excel_buffer,
                file_name="laporan_penjualan.xlsx",
                mime=(
                    "application/vnd.openxmlformats-"
                    "officedocument.spreadsheetml.sheet"
                ),
                use_container_width=True
            )

        with col3:

            st.info(
                "Untuk mencetak laporan, gunakan "
                "Ctrl + P pada browser."
            )

# REKAP KEUNTUNGAN
# ============================================================

elif menu == "📊  Rekap Keuntungan":

    st.title("📊 Rekap Keuntungan")

    st.write(
        "Ringkasan keuntungan dari seluruh transaksi penjualan."
    )

    st.divider()

    sales = get_sales()

    if len(sales) == 0:

        st.info(
            "Belum ada transaksi penjualan."
        )

    else:

        total_mahar = sum(
            sale["total_mahar"]
            for sale in sales
        )

        total_modal = sum(
            sale["total_modal"]
            for sale in sales
        )

        total_keuntungan = (
            total_mahar - total_modal
        )

        total_store = sum(
            sale["keuntungan_store"]
            for sale in sales
        )

        total_pemimpin = sum(
            sale["keuntungan_pemimpin"]
            for sale in sales
        )

        total_penulis = sum(
            sale["keuntungan_penulis"]
            for sale in sales
        )

        # ----------------------------------------------------
        # RINGKASAN
        # ----------------------------------------------------

        st.subheader(
            "💰 Ringkasan Keuangan"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Mahar",
                f"Rp {total_mahar:,.0f}"
            )

        with col2:

            st.metric(
                "Total Modal",
                f"Rp {total_modal:,.0f}"
            )

        with col3:

            st.metric(
                "Total Keuntungan",
                f"Rp {total_keuntungan:,.0f}"
            )

        st.divider()

        # ----------------------------------------------------
        # PEMBAGIAN
        # ----------------------------------------------------

        st.subheader(
            "📊 Pembagian Keuntungan"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "STORE",
                f"Rp {total_store:,.0f}"
            )

        with col2:

            st.metric(
                "PEMIMPIN",
                f"Rp {total_pemimpin:,.0f}"
            )

        with col3:

            st.metric(
                "PENULIS",
                f"Rp {total_penulis:,.0f}"
            )

        st.divider()

        # ----------------------------------------------------
        # VALIDASI
        # ----------------------------------------------------

        total_pembagian = (
            total_store
            + total_pemimpin
            + total_penulis
        )

        if round(
            total_pembagian,
            2
        ) == round(
            total_keuntungan,
            2
        ):

            st.success(
                f"✓ Pembagian keuntungan sesuai "
                f"dengan total keuntungan: "
                f"Rp {total_pembagian:,.0f}"
            )

        else:

            st.warning(
                "Perhatian: jumlah pembagian keuntungan "
                "belum sama dengan total keuntungan."
            )
