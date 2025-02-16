import streamlit as st
st.set_page_config(layout="wide")
# Custom CSS dengan animasi dan efek modern
st.markdown(
    """
    <style>
    /* Background animasi gradient yang lebih halus */
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stApp {
        background: linear-gradient(-45deg, #1e1e2f, #2a2a40, #3a3a5a, #4a4a75);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }

    /* Judul dengan efek teks gradient yang lebih halus */
    .title {
        font-size: 4rem;
        text-align: center;
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    /* Card dengan glassmorphism effect yang lebih minimalis */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.1);
    }

    /* Ikon modern dengan animasi */
    .icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: inline-block;
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        transition: transform 0.3s ease;
    }

    .icon:hover {
        transform: scale(1.1);
    }

    /* Tombol dengan efek neon yang lebih halus */
    .stButton > button {
        background: rgba(255,255,255,0.05);
        border: 2px solid #2575fc;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 25px;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
    }

    .stButton > button:hover {
        background: rgba(37, 117, 252, 0.1);
        border-color: #6a11cb;
        box-shadow: 0 0 15px rgba(106, 17, 203, 0.2);
    }

    /* Feature showcase grid */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        padding: 2rem 0;
    }

    /* Footer dengan efek lebih halus */
    .footer {
        text-align: center;
        margin-top: 4rem;
        color: rgba(255,255,255,0.6);
        padding: 1.5rem;
    }

    .footer a {
        color: rgba(255,255,255,0.6);
        margin: 0 1rem;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .footer a:hover {
        color: #2575fc;
    }
    </style>
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    h1.anchor, h2 .anchor, h3 .anchor, h4 .anchor, h5 .anchor, h6 .anchor {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Font Awesome Icons
st.markdown(
    """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">""",
    unsafe_allow_html=True
)

# Konten utama
st.markdown('<h1 class="title">HERA</h1>', unsafe_allow_html=True) 
st.markdown('<div style="text-align: center; margin-bottom: 3rem;"><h3 style="color: rgba(255,255,255,0.9); font-weight: 300;">High-efficiency Entities Recognition Application</h3></div>', unsafe_allow_html=True)

# Feature Grid
st.markdown("""
<div class="feature-grid">
    <!-- PII Masking Card -->
    <div class="card">
        <i class="fas fa-mask icon"></i>
        <h3 style="color: white; margin-bottom: 1rem;">PII Masking</h3>
        <p style="color: rgba(255,255,255,0.8); line-height: 1.6;">
            Proteksi otomatis untuk informasi sensitif seperti nomor KTP, rekening bank, dan data pribadi lainnya dengan teknologi masking canggih.
        </p>
    </div>

<!-- NER Card -->
<div class="card">
    <i class="fas fa-search-location icon"></i>
    <h3 style="color: white; margin-bottom: 1rem;">Entity Detection</h3>
    <p style="color: rgba(255,255,255,0.8); line-height: 1.6;">
        Identifikasi 20+ jenis entitas termasuk lokasi geografis, organisasi, dan entitas temporal dengan model NLP terlatih.
    </p>
</div>

<!-- POS Tagging Card -->
<div class="card">
    <i class="fas fa-tags icon"></i>
    <h3 style="color: white; margin-bottom: 1rem;">POS Tagging</h3>
    <p style="color: rgba(255,255,255,0.8); line-height: 1.6;">
        Analisis struktur kalimat mendalam dengan akurasi 98.7% untuk deteksi subjek, predikat, dan objek.
    </p>
</div>
</div>
""", unsafe_allow_html=True)

# CTA Section
if st.button("🚀 Launch HERA Now"):
    st.balloons()
    st.success("Redirecting to application...")
    
# Demo Section
st.markdown("""
<div style="margin-top: 4rem; padding: 2rem; background: rgba(255,255,255,0.05); border-radius: 15px;">
    <h2 style="color: white; text-align: center; margin-bottom: 2rem;">✨ Feature Showcase</h2>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
        <div style="padding: 1.5rem; background: rgba(0,0,0,0.1); border-radius: 10px;">
            <h4 style="color: #6a11cb; margin-bottom: 1rem;">Before PII Masking</h4>
            <p style="color: rgba(255,255,255,0.7);">"John Doe (123-45-6789) tinggal di 123 Main St, New York."</p>
        </div>
        <div style="padding: 1.5rem; background: rgba(0,0,0,0.1); border-radius: 10px;">
            <h4 style="color: #2575fc; margin-bottom: 1rem;">After PII Masking</h4>
            <p style="color: rgba(255,255,255,0.7);">"████ ███ (███-██-████) tinggal di ███ █████ St, ███████."</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Powered by AI Magic ✨ • v2.0.1</p>
    <div style="margin-top: 1rem;">
        <a href="#"><i class="fab fa-github"></i></a>
        <a href="#"><i class="fab fa-twitter"></i></a>
        <a href="#"><i class="fab fa-linkedin"></i></a>
    </div>
</div>
""", unsafe_allow_html=True)