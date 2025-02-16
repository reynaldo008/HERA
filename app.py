import streamlit as st

st.set_page_config(page_title="HERA", layout="wide")

# Custom CSS dengan desain modern dan UX yang menarik
custom_css = """
<style>
/* Animasi gradient background */
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Global styling */
body {
    margin: 0;
    padding: 0;
    font-family: 'Roboto', sans-serif;
}
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
    background-size: 400% 400%;
    animation: gradient 30s ease infinite;
    color: #f0f0f0;
}

/* Header */
.header-title {
    font-size: 7rem;  /* Ukuran judul di layar besar */
    font-weight: bold;
    text-align: center;
    background: linear-gradient(45deg, #FF6FD8, #3813C2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 2rem 0 0.5rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
.header-subtitle {
    text-align: center;
    font-size: 4rem;  /* Ukuran subjudul di layar besar */
    color: #d0d0d0;
    margin-bottom: 3rem;
}

/* Feature Grid */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 2rem 0;
}

/* Card style dengan efek glassmorphism */
.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(8px);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
    margin-bottom: 1rem; 
}
.card p {
    font-size: 1.2rem; 
    line-height: 1.6;
    color: #e0e0e0;
}
.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.3);
}
.card-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    color: #ff6fd8;
    transition: transform 0.3s ease;
}
.card:hover .card-icon {
    transform: scale(1.2);
}
.card h3 {
    margin: 0;
    margin-bottom: 1rem;
    font-size: 1.75rem;
    color: #fff;
}

/* Tooltip */
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted #ccc;
    cursor: help;
}
.tooltip .tooltiptext {
    visibility: hidden;
    width: 180px;
    background-color: rgba(0, 0, 0, 0.9);
    color: #fff;
    text-align: center;
    border-radius: 8px;
    padding: 8px;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -90px;
    opacity: 0;
    transition: opacity 0.4s ease;
}
.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}

/* CTA Button */
.cta-button {
    display: block;
    width: 250px;
    margin: 2rem auto;
    padding: 15px 20px;
    text-align: center;
    font-size: 1.2rem;
    background: linear-gradient(45deg, #ff6fd8, #3813C2);
    border: none;
    border-radius: 50px;
    color: #fff;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.3s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
.cta-button:hover {
    transform: scale(1.05);
    background: linear-gradient(45deg, #3813C2, #ff6fd8);
}

/* Demo Section */
.demo-section {
    margin-top: 4rem;
    padding: 2rem;
    background: rgba(255,255,255,0.05);
    border-radius: 20px;
}
.demo-section h2 {
    text-align: center;
    color: #fff;
    margin-bottom: 2rem;
}
.demo-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}
.demo-card {
    background: rgba(0,0,0,0.1);
    padding: 1.5rem;
    border-radius: 15px;
}
.demo-card h4 {
    margin-top: 0;
    margin-bottom: 1rem;
    color: #ff6fd8;
}
.demo-card p {
    color: #e0e0e0;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 3rem;
    padding: 1.5rem;
    color: #bbb;
}
.footer a {
    color: #bbb;
    margin: 0 1rem;
    text-decoration: none;
    transition: color 0.3s ease;
}
.footer a:hover {
    color: #ff6fd8;
}

/* Responsive: Atur ulang font-size agar lebih kecil di layar sempit */
@media (max-width: 768px) {
    .header-title {
        font-size: 4rem;  /* Lebih kecil di layar sempit */
    }
    .header-subtitle {
        font-size: 2.5rem; /* Lebih kecil di layar sempit */
    }
    .card h3 {
        font-size: 1.5rem;
    }
}
</style>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Header
st.markdown('<h1 class="header-title">HERA</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; margin-bottom: 0.25rem;"><h3 style="color:#d0d0d0; font-weight: 200;">High-efficiency Entities Recognition Application</h3></div>', unsafe_allow_html=True)


# Feature Cards
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

# Card: PII Masking
st.markdown('''
<div class="card">
    <i class="fas fa-user-secret card-icon"></i>
    <h3>PII Masking</h3>
    <p>
        Proteksi otomatis untuk informasi sensitif seperti nomor KTP, rekening bank, dan data pribadi lainnya dengan teknologi masking canggih.
    </p>
    <div class="tooltip">Hover untuk info lebih lanjut
        <span class="tooltiptext">Menggunakan algoritma enkripsi dan masking untuk mengamankan data Anda.</span>
    </div>
</div>
''', unsafe_allow_html=True)
if st.button("Go to PII Masking"):
    st.page_link("pages/PII_Masking.py", label="")

# Card: Entity Detection
st.markdown('''
<div class="card">
    <i class="fas fa-search-location card-icon"></i>
    <h3>Entity Detection</h3>
    <p>
        Identifikasi 20+ jenis entitas termasuk lokasi geografis, organisasi, dan entitas temporal dengan model NLP terlatih.
    </p>
    <div class="tooltip">Hover untuk info lebih lanjut
        <span class="tooltiptext">Model NLP kami mengidentifikasi entitas dengan akurasi tinggi dan cepat.</span>
    </div>
</div>
''', unsafe_allow_html=True)
if st.button("Go to Entity Detection"):
    st.page_link("pages/Entity_Detection.py", label="")

# Card: Subject Detection
st.markdown('''
<div class="card">
    <i class="fas fa-tags card-icon"></i>
    <h3>Subject Detection</h3>
    <p>
        Analisis struktur kalimat mendalam dengan akurasi 98.7% untuk deteksi subjek, predikat, dan objek.
    </p>
    <div class="tooltip">Hover untuk info lebih lanjut
        <span class="tooltiptext">Analisis cepat dan akurat untuk memetakan struktur kalimat Anda.</span>
    </div>
</div>
''', unsafe_allow_html=True)
if st.button("Go to Subject Detection"):
    st.page_link("pages/Subject_Detection.py", label="")

st.markdown('</div>', unsafe_allow_html=True)

# CTA Button
if st.button("🚀 Launch HERA Now", key="cta"):
    st.success("Redirecting to application...")

# Demo Section
st.markdown('''
<div class="demo-section">
    <h2>✨ Feature Showcase</h2>
    <div class="demo-grid">
        <div class="demo-card">
            <h4>Before PII Masking</h4>
            <p>"John Doe (123-45-6789) tinggal di 123 Main St, New York."</p>
        </div>
        <div class="demo-card">
            <h4>After PII Masking</h4>
            <p>"[Nama] (No. HP) tinggal di [Alamat]."</p>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# Footer
st.markdown('''
<div class="footer">
    <p>Powered by Streamlit ✨ • v2.0.1</p>
    <div>
        <a href="#"><i class="fab fa-github"></i></a>
        <a href="#"><i class="fab fa-twitter"></i></a>
        <a href="#"><i class="fab fa-linkedin"></i></a>
    </div>
</div>
''', unsafe_allow_html=True)
