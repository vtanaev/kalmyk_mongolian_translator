import streamlit as st
import re

def to_kalmyk(text):
    text = re.sub('ё', 'й', text)
    text = re.sub(r'га|го|гө', 'х', text)
    text = re.sub('ж', 'җ', text)
    text = re.sub('ээс', 'әс', text)
    text = re.sub(r'багатур', 'баатр', text)
    return text 

text1 = st.text_area("Enter text:", value="тэнгэрийн бошгоор")

st.write(to_kalmyk(text1))
st.write('теңгрин бошгар')

text2 = st.text_area("Enter text:", value="хийсвээс тэнгэрийн доор, хэлвээс ноёдын доор")

st.write(to_kalmyk(text2))
st.write('киисвәс теңгрин дор, келвәс нойдын дор')

text3 = st.text_area("Enter text:", value="тэнгэрийн заяа цагийн улирал дагаж")

st.write(to_kalmyk(text3))
st.write('теңгрин заян цагин ульрл дахҗ')





