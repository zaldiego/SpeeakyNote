import streamlit as st
import algoritmo
import os
import tempfile
import base64

def app():
    st.header('Transformar IMAGEN en AUDIO')

    lang_voice = st.radio("Selecciona el idioma del texto (Español, Inglés, Francés y Portugués):", ("es", "en", "fr", "pt"))

    # Widget para seleccionar los archivos de imagen
    uploaded_files = st.file_uploader("Selecciona archivos de imagen", accept_multiple_files=True)

    # Variable de estado para almacenar la carpeta temporal
    if 'temp_folder' not in st.session_state:
        st.session_state.temp_folder = None

    if uploaded_files:
        # Crear una carpeta temporal para almacenar los archivos
        temp_folder = tempfile.TemporaryDirectory()
        st.session_state.temp_folder = temp_folder.name

        # Guardar los archivos en la carpeta temporal
        for file in uploaded_files:
            with open(os.path.join(temp_folder.name, file.name), "wb") as f:
                f.write(file.read())

    # Variable de estado para controlar si la generación del audio fue exitosa
    if 'audio_generation_successful' not in st.session_state:
        st.session_state.audio_generation_successful = False

    # Variable de estado para almacenar los datos del audio generado
    if 'audio_data' not in st.session_state:
        st.session_state.audio_data = None

    # Variable de estado para almacenar el nombre del archivo de audio
    if 'audio_filename' not in st.session_state:
        st.session_state.audio_filename = "output.mp3"

    # Orden de ejecución del programa
    if st.button('Inicio') and st.session_state.temp_folder:
        with st.spinner("Estamos generando su audio..."):
            # Listar archivos en la carpeta temporal
            files_in_temp_folder = [os.path.join(st.session_state.temp_folder, filename) for filename in os.listdir(st.session_state.temp_folder)]
            list_ocr = algoritmo.ocr_transform(files_in_temp_folder, lang_voice)

            # Generar audio basado en el texto extraído de las imágenes
            audio_data = algoritmo.generate_audio(list_ocr, lang_voice)

            # Almacena los datos del audio en el estado de la sesión
            st.session_state.audio_data = audio_data

    if st.session_state.audio_data is not None:
        audio_filename = st.text_input("Nombre del archivo de audio:", st.session_state.audio_filename)

        if st.button("Reproducir y Descargar Audio") and audio_filename:
            # Almacena el nombre del archivo proporcionado por el usuario
            st.session_state.audio_filename = audio_filename

            # Marcar la generación de audio como exitosa
            st.session_state.audio_generation_successful = True

            if st.session_state.audio_generation_successful:
                st.success('El audio se ha generado correctamente')
            # Mostrar el audio en línea
                st.audio(st.session_state.audio_data, format="audio/mp3", start_time=0)

                # Agregar un botón de descarga
                b64 = base64.b64encode(st.session_state.audio_data).decode('utf-8')
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="{audio_filename}">Descargar Audio</a>'
                st.markdown(href, unsafe_allow_html=True)

                st.balloons()

            else:
                st.warning("La generación del archivo de audio ha fallado. Asegúrate de haber generado el audio correctamente.")
