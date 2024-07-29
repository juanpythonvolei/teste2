import streamlit as st

import face_recognition as fr
from PIL import Image

usuario_foto = st.camera_input(help='Faça o Login',label='Login',)
if usuario_foto:
    with open(f'captured_image.jpg', 'wb') as f:
                f.write(usuario_foto.getvalue())
    link = f"./captured_image.jpg"

    imagem_base = r'C:\Users\juanz\OneDrive\Área de Trabalho\minha foto.jpg'
    img_base = fr.load_image_file(imagem_base)
    encode_base = fr.face_encodings(img_base)[0]

    usuario = fr.load_image_file(link)
    encode_usuario = fr.face_encodings(usuario)[0]

    resultado = fr.compare_faces([encode_base], encode_usuario)
    if resultado[0]:
            print("Rosto reconhecido!")
            st.warning('Acesso Liberado')
    else:
            print("Rosto não reconhecido.")