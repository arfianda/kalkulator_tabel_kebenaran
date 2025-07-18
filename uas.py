# Nama          : Arfianda Firsta Satritama
# NIM           : 312410377
# Mata Kuliah   : Logika Informatika
# Dosen         : Muhammad Najamuddin Dwi Miharja, S.Kom, M.Kom.

import streamlit as st
import pandas as pd
import itertools
import re

# --- FUNGSI LOGIKA ---

def generate_truth_table(propositions, expression):
    """
    Menghasilkan dan menganalisis tabel kebenaran untuk ekspresi logika.

    Fungsi ini mengambil daftar proposisi atomik dan sebuah string ekspresi logika,
    kemudian menghitung semua kemungkinan hasil kebenaran.

    Args:
        propositions (list): Daftar string proposisi atomik (misal: ['p', 'q']).
        expression (str): Ekspresi logika dalam bentuk string (misal: 'p ∧ q').

    Returns:
        pd.DataFrame: Tabel kebenaran dalam bentuk pandas DataFrame.
        str: Hasil analisis ('Tautologi', 'Kontradiksi', atau 'Kontingensi').
    """
    # Menghasilkan semua kombinasi nilai kebenaran (True/False) untuk proposisi
    truth_values = list(itertools.product([True, False], repeat=len(propositions)))
    
    # Menyiapkan header untuk tabel DataFrame
    table_headers = propositions + [expression]
    table_data = []

    # Iterasi melalui setiap kombinasi nilai kebenaran untuk dievaluasi
    for values in truth_values:
        # Membuat scope lokal untuk fungsi eval(), memetakan nama proposisi ke nilai kebenarannya
        local_scope = {prop: val for prop, val in zip(propositions, values)}
        
        # Mengonversi simbol logika yang user-friendly menjadi operator Python yang dapat dievaluasi
        eval_expression = expression.lower().replace('∧', 'and').replace('∨', 'or').replace('¬', 'not ').replace('↔', '==')
        
        # Penanganan khusus untuk implikasi (→)
        if '→' in expression:
            eval_expression = eval_expression.replace('→', ' implies ')
            parts = eval_expression.split(' implies ')
            antecedent = eval(parts[0], {}, local_scope)
            consequent = eval(parts[1], {}, local_scope)
            result = (not antecedent) or consequent
        else:
            # Mengevaluasi ekspresi logika lain menggunakan fungsi eval()
            result = eval(eval_expression, {"__builtins__": {}}, local_scope)
        
        # Menambahkan baris hasil ke data tabel
        row = list(values) + [result]
        table_data.append(row)

    # Membuat DataFrame dari data yang telah dikumpulkan
    df = pd.DataFrame(table_data, columns=table_headers)

    # --- Analisis Hasil Kolom Terakhir ---
    result_column = df[expression]
    if all(result_column):
        analysis = "Tautologi"
    elif not any(result_column):
        analysis = "Kontradiksi"
    else:
        analysis = "Kontingensi"
        
    return df, analysis

# --- ANTARMUKA PENGGUNA (UI) STREAMLIT ---

# Konfigurasi dasar halaman Streamlit
st.set_page_config(page_title="Kalkulator Logika Proposisi", layout="wide", initial_sidebar_state="expanded")

# Judul utama dan informasi mahasiswa
st.title("👨‍💻 Implementasi Program Logika Proposisi")
st.markdown("---")

# Menggunakan kolom untuk menata informasi mahasiswa
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Nama:** Arfianda Firsta Satritama
    **NIM:** 312410377
    """)
with col2:
    st.markdown("""
    **Mata Kuliah:** Logika Informatika
    **Dosen:** Muhammad Najamuddin Dwi Miharja, S.Kom, M.Kom.
    """)

st.markdown("---")

# Deskripsi singkat tentang aplikasi
st.header("Kalkulator Tabel Kebenaran Otomatis")
st.markdown(
    "Aplikasi ini dibuat untuk memenuhi UAS Logika Informatika. "
    "Program ini secara otomatis menghasilkan tabel kebenaran dan menganalisis "
    "hasil dari sebuah ekspresi logika untuk menentukan apakah ia Tautologi, Kontradiksi, atau Kontingensi."
)

# Panel input di sidebar kiri
st.sidebar.header("⚙️ Panel Input")

# Contoh kasus dari dokumen untuk kemudahan penggunaan
st.sidebar.subheader("Contoh Analisis Berita (Kontradiksi)")
st.sidebar.info(
    "Berdasarkan analisis dokumen:\n"
    "- **Proposisi (p):** Kebijakan IPR bertujuan untuk menyejahterakan rakyat.\n"
    "- **Ekspresi:** `p ∧ ¬p`\n"
    "- **Analisis:** Pernyataan ini adalah sebuah **Kontradiksi**."
)
if st.sidebar.button("Gunakan Contoh Kasus `p ∧ ¬p`"):
    st.session_state.expression_input = 'p ∧ ¬p'

# Input kustom dari pengguna
st.sidebar.subheader("Input Kustom Anda")
expression_input = st.sidebar.text_input(
    "Masukkan Ekspresi Logika Anda:",
    key="expression_input",
    placeholder="Contoh: (p ∧ q) → r",
    help="Gunakan simbol: ∧ (DAN), ∨ (ATAU), ¬ (TIDAK), → (IMPLIKASI), ↔ (BIIMPLIKASI). Gunakan kurung untuk prioritas."
).strip()

# Tombol untuk memicu kalkulasi
if st.sidebar.button("🚀 Buat Tabel Kebenaran", type="primary", use_container_width=True):
    
    # --- Penanganan Input dan Validasi (Error Handling) ---
    if not expression_input:
        st.error("⚠️ **Input Error:** Ekspresi logika tidak boleh kosong. Silakan masukkan ekspresi di sidebar.")
    else:
        # Menggunakan regex untuk mendeteksi semua huruf (sebagai proposisi) dalam ekspresi
        propositions = sorted(list(set(re.findall(r'[a-z]', expression_input.lower()))))
        
        if not propositions:
            st.error("⚠️ **Input Error:** Tidak ada proposisi yang valid (contoh: p, q, r) terdeteksi dalam ekspresi Anda.")
        else:
            try:
                st.success(f"Proposisi yang terdeteksi: **{', '.join(propositions)}**")
                
                # Panggil Fungsi Logika dan Tampilkan Hasil
                truth_table_df, analysis_result = generate_truth_table(propositions, expression_input)
                
                st.header("📊 Hasil Analisis")
                
                # Menampilkan kesimpulan analisis dengan visual yang sesuai
                if analysis_result == "Tautologi":
                    st.success(f"Ekspresi `{expression_input}` adalah sebuah **{analysis_result}**.")
                    st.markdown("Ini berarti ekspresi tersebut **selalu bernilai Benar (True)**.")
                elif analysis_result == "Kontradiksi":
                    st.error(f"Ekspresi `{expression_input}` adalah sebuah **{analysis_result}**.")
                    st.markdown("Ini berarti ekspresi tersebut **selalu bernilai Salah (False)**.")
                else:
                    st.info(f"Ekspresi `{expression_input}` adalah sebuah **{analysis_result}**.")
                    st.markdown("Ini berarti nilai kebenaran ekspresi ini **bergantung** pada nilai kebenaran proposisinya.")

                # Visualisasi Hasil (Tabel Kebenaran)
                st.subheader("Tabel Kebenaran")
                truth_table_df_display = truth_table_df.copy()
                for col in truth_table_df_display.columns:
                    truth_table_df_display[col] = truth_table_df_display[col].apply(lambda x: 'T (Benar)' if x else 'F (Salah)')
                
                st.dataframe(truth_table_df_display, use_container_width=True)

            except Exception as e:
                st.error(f"🔥 **Syntax Error:** Terjadi kesalahan saat memproses ekspresi Anda: `{e}`")
                st.warning("Pastikan format ekspresi Anda benar. Contoh: `p ∧ q`, `¬p`, `(p ∨ q) → r`.")

# --- Bagian Source Code yang Dapat Diperluas ---
st.markdown("---")
with st.expander("Lihat Source Code Lengkap Program Ini"):
    st.code((lambda: open(__file__, encoding='utf-8').read())(), language='python')