import streamlit as st

st.set_page_config(layout="centered")
st.title("📊 Model Antrian M/M/1")
st.markdown("### Sistem Antrian dalam Dunia Industri")

st.write(
    """
    Model M/M/1 digunakan untuk menganalisis sistem pelayanan satu jalur:
    - Pabrik jalur perakitan
    - Loket pelayanan
    - Helpdesk / customer service
    """
)

st.subheader("📥 Masukkan Parameter:")
λ = st.number_input("λ = Rata-rata kedatangan per jam", value=10.0)
μ = st.number_input("μ = Rata-rata pelayanan per jam", value=12.0)

if st.button("Hitung Model Antrian"):
    if λ >= μ:
        st.error("❌ λ harus lebih kecil dari μ agar sistem stabil.")
    else:
        ρ = λ / μ
        W = 1 / (μ - λ)
        Wq = λ / (μ * (μ - λ))
        L = λ * W
        Lq = λ * Wq

        st.success("✅ Hasil Perhitungan:")
        st.write(f"**Tingkat Utilisasi (ρ):** {ρ:.2f} atau {ρ*100:.1f}%")
        st.write(f"**Rata-rata waktu di sistem (W):** {W:.2f} jam")
        st.write(f"**Rata-rata waktu tunggu dalam antrean (Wq):** {Wq:.2f} jam")
        st.write(f"**Jumlah pelanggan di sistem (L):** {L:.2f}")
        st.write(f"**Jumlah pelanggan dalam antrean (Lq):** {Lq:.2f}")
