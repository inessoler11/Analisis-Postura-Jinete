import streamlit as st

# Configuración de la aplicación
st.set_page_config(page_title="Análisis de Postura del Jinete", layout="wide")

# Título y descripción
st.title("📊 Análisis de Postura del Jinete con IA")
st.write("Sube un video de tu entrenamiento y la IA analizará tu postura, alineación y posición en la montura.")

# Subida de videos
video_file = st.file_uploader("📤 Sube tu video aquí", type=["mp4", "mov", "avi"])

if video_file:
    st.video(video_file)  # Reproducir el video subido
    st.write("📡 **Procesando análisis...**")

    # Simulación de feedback (hasta que integremos IA)
    st.subheader("📊 Resultados del Análisis")
    st.write("🔹 **Alineación vertical:** Se detectó una ligera inclinación hacia adelante en el galope.")
    st.write("🔹 **Ángulo de la espalda:** 145° (Ideal: 160° - 180°) → *Podrías estar encorvado*")
    st.write("🔹 **Posición de manos:** Tus manos parecen estar un poco altas, lo que puede afectar el contacto con la boca del caballo.")
    st.write("🔹 **Posición de piernas:** Los talones están subiendo demasiado en el trote, lo que puede afectar la estabilidad.")

    st.subheader("✅ Recomendaciones")
    st.write("✔️ Mantén una alineación hombros-caderas-talones para mejorar la estabilidad.")
    st.write("✔️ Relaja las manos y mantén un contacto suave y constante.")
    st.write("✔️ Intenta bajar los talones para mejorar el equilibrio.")
    st.write("✔️ Mantén la espalda erguida para evitar tensión en las transiciones.")

st.write("📌 **Próximamente:** Análisis automático con IA en tiempo real.")

# Mensaje final
st.write("Prueba subiendo un video de entrenamiento y obtén tu primer análisis.")

