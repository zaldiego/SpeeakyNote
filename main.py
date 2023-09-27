import streamlit as st
from streamlit_option_menu import option_menu


import img_audio, txt_audio



#Arreglar el set_page_config
st.set_page_config(
    page_title='Speaky Note',
    page_icon = '/home/zaldiego/Imágenes/neuralbatch_icono.png',
    initial_sidebar_state='expanded'
)


class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            'title':title,
            'function':function
        })
    
    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='Speaky Note',
                options=['Imagen -> Audio', 'Texto -> Audio'],
                icons=['code', 'code'],
                menu_icon='star',
                default_index=1,
                orientation='vertical',
                styles={

                        "container": {"padding": "5!important","background-color":'#FFFFFF'},
                        "icon": {"color": "#39067B", "font-size": "18px"}, 
                        "nav-link": {"color":"#39067B","font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#6B00F7"},
                        "nav-link-selected": {"background-color": "#6B00F7", 'color':'#FFFFFF', 'font-size':'18px'},}
                        )
            

        
        if app == "Imagen -> Audio":
            img_audio.app()
        if app == "Texto -> Audio":
            txt_audio.app()
             
          
             
    run()            
        

#POR HACER:

# Producto inicial MVP y testeo
# 5) Agregar función inversa, de texto a audio
# 6) Ajustar CSS y probar el programa
# 7) Despliegue del programa Version 0.1


# Mejora en el desarrollo del producto y testeo avanzado 
# 8) Agregar una función para que detecte la cálidad de la imagen y si estas pueden ser procesadas adecuadamente por el programa
# 9) Mejorar el codigo para reducir los tiempos de procesamiento del programa en general
# 10) Agregar un optimizador de imagen para usar con el programa de imagen -> audio
# 11) Agregar voicebox o un algun algoritmo similar para clonar la voz
# 12) Desarrollar API de Speaky Note
# 13) Desplegar y publicar tanto en streamlit como API en la página de Neural Batch como Version 0.2


# Orientar monetización del producto para comerciarlizarlo
# 14) Agregar función de block de notas
# 15) Agregar base de datos de usuario
# 16) Agregar un filtro que detecte y elimine el texto en imágenes
# 17) Agregar el ajuste de parametros para que el usuario escoja la voz, el idioma, y la velocidad de lectura sobre el generador de audio
# 18) Agregar metodo de monetización
# 19) Construir página e identidad de marca propia
# 20) Desplegar y publicar la Version 0.3
