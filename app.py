# Aplicación Streamlit de Rendiciones Nomade
import streamlit as st
import pandas as pd
import pytesseract
from PIL import Image
import io

st.set_page_config(page_title='Rendiciones Nomade')
st.title('Rendiciones Nomade')
st.write('Subí tu boleta o factura para extraer los datos y exportarlos a Excel.')
