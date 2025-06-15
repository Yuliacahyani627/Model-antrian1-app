import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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

        # Tambahan grafik
        st.subheader("📈 Grafik Pengaruh λ terhadap Wq dan Lq")

        lambda_vals = np.linspace(0.1, μ - 0.01, 300)
        Wq_vals = lambda_vals / (μ * (μ - lambda_vals))
        Lq_vals = lambda_vals**2 / (μ * (μ - lambda_vals))

        fig, ax = plt.subplots(1, 2, figsize=(12, 4))

        ax[0].plot(lambda_vals, Wq_vals, label="Wq (jam)", color="blue")
        ax[0].axvline(λ, color='red', linestyle='--', label=f"λ saat ini = {λ}")
        ax[0].set_title("Waktu Tunggu (Wq) vs λ")
        ax[0].set_xlabel("λ (kedatangan per jam)")
        ax[0].set_ylabel("Wq (jam)")
        ax[0].legend()
        ax[0].grid(True)

        ax[1].plot(lambda_vals, Lq_vals, label="Lq (pelanggan)", color="orange")
        ax[1].axvline(λ, color='red', linestyle='--', label=f"λ saat ini = {λ}")
        ax[1].set_title("Jumlah Antrean (Lq) vs λ")
        ax[1].set_xlabel("λ (kedatangan per jam)")
        ax[1].set_ylabel("Lq (orang)")
        ax[1].legend()
        ax[1].grid(True)

        st.pyplot(fig)
