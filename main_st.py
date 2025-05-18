import streamlit as st
import re

def to_kalmyk(text):
    text = re.sub('ё', 'й', text)
    text = re.sub(r'гоо', 'ха', text)
    text = re.sub(r'үгүй', 'уга', text)
    text = re.sub(r'гүй ', 'го', text)
    text = re.sub(r'хуй |хүй ', 'лһн', text)
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

text3 = st.text_area("Enter text:", value="нар буцахад эхлэдэг хүйтний наян нэг хоногийг есөн ес гэнэ")

st.write(to_kalmyk(text3))
st.write('Нарн буцхд эклдг киитниг найн нег хонгиг йисн йис гинә')





