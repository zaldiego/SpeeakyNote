import streamlit as st
import algoritmo
import os
import tempfile
from io import BytesIO
import base64

def app():
    st.header('Transformar TEXTO en AUDIO')

    lang_voice = st.radio("Selecciona el idioma del texto (Español, Inglés, Francés y Portugués):", ("es", "en", "fr", "pt"))


    # Widget para ingresar texto
    input_text = st.text_area("Ingresa el texto (máximo 10,000 palabras):")

    if input_text:
        # Verificar que el texto ingresado no supere las 10,000 palabras
        word_count = len(input_text.split())
        if word_count > 10000:
            st.warning("El texto ingresado supera el límite de 10,000 palabras.")
        else:
            # Campo de entrada para el nombre del archivo de audio
            audio_filename = st.text_input("Nombre del archivo de audio:", "output.mp3")

            # Variable de estado para controlar si la generación del audio fue exitosa
            if 'audio_generation_successful' not in st.session_state:
                st.session_state.audio_generation_successful = False

            if st.button("Generar Audio") and audio_filename:
                with st.spinner("Estamos generando su audio..."):
                    # Generar audio basado en el texto ingresado
                    list_ocr = [input_text]

                    # Llama a la función generate_audio, que devolverá los datos del audio
                    audio_data = algoritmo.generate_audio(list_ocr, lang_voice)
                    
                    # Almacena el nombre del archivo proporcionado por el usuario
                    st.session_state.audio_filename = audio_filename
                    st.session_state.audio_data = audio_data
                    
                    # Marcar la generación de audio como exitosa
                    st.session_state.audio_generation_successful = True

                # Verificar si la generación de audio fue exitosa antes de mostrar y descargar
                if st.session_state.audio_generation_successful:
                    # Mostrar el audio en línea
                    st.audio(st.session_state.audio_data, format="audio/mp3", start_time=0)

                    st.success('El audio se ha generado correctamente')

                    # Agregar un botón de descarga
                    b64 = base64.b64encode(st.session_state.audio_data).decode('utf-8')
                    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{audio_filename}">Descargar Audio</a>'
                    st.markdown(href, unsafe_allow_html=True)

                    st.balloons()
                else:
                    st.warning("La generación del archivo de audio ha fallado. Asegúrate de haber generado el audio correctamente.")
