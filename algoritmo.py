from paddleocr import PaddleOCR
from gtts import gTTS
import tempfile

#===================================================== ALGORITMO OCR


# Función para la transformación OCR
def ocr_transform(files, lang_voice):
    # Set OCR model with PaddleOCR
    reader = PaddleOCR(use_angle_cls=True, lang=lang_voice)

    # List to store the extracted text
    list_ocr = []

    # Sort the image files based on their names
    #files.sort(key=lambda x: int(x.split('_')[1])) Este sort se debe mejorar, da error en el programa a la hora de iterar el orden de los archivos

    # Iterate over all selected files
    for image_path in files:
        result = reader.ocr(image_path)
        for index in range(len(result)):
            res = result[index]
            for line in res:
                list_ocr.append(line[1][0])

    return list_ocr

#===================================================== TRANSFORMACIÓN DEL TEXTO EN AUDIO

def generate_audio(list_ocr, lang_voice):
    str_ocr = ", ".join(map(str, list_ocr))
    myobj = gTTS(text=str_ocr, lang=lang_voice, slow=False)

    # Crear un archivo temporal para el audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        audio_filename = temp_audio.name
        myobj.save(audio_filename)
    
    # Leer los datos del archivo temporal y devolverlos
    audio_data = open(audio_filename, "rb").read()
    
    return audio_data

