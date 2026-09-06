import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Absensi KPU Jambi", layout="wide")

st.title("📋 SISTEM ABSENSI MAGANG - KPU PROVINSI JAMBI")

# Baca file html
with open("absensi.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Tampilkan di streamlit
components.html(html_code, height=1200, scrolling=True)
