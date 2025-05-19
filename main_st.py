import streamlit as st
import re

def to_kalmyk(text):
    text = ' '+text + ' '
    text = re.sub('\.', ' . ', text)
    text = re.sub('\,', ' , ', text)
    text = re.sub('\!', ' ! ', text)
    text = re.sub('\?', ' ? ', text)
    text = re.sub(' тэ', ' те', text)
    text = re.sub(' яв', ' йов', text)
    text = re.sub(r' ес', ' йис', text)
    text = re.sub(r' нэг ', ' нег ', text)
    text = re.sub(r'гэнэ', 'гинә', text)
    # text = re.sub('ийн ', 'ин ', text)
    # text = re.sub('ийг ', 'иг ', text)
    text = re.sub('ой ', 'а ', text)
    text = re.sub('эй ', 'ә ', text)
    text = re.sub('ая', 'ай', text)
    text = re.sub(r'хуй |хүй |ахүй |ахүй ', 'лһн ', text)
    text = re.sub('[\w]ээ', 'е', text)
    text = re.sub('ё', 'й', text)
    text = re.sub(r'гоо', 'ха', text)
    text = re.sub(r'үгүй ', 'уга ', text)
    text = re.sub(r'гүй ', 'го', text)
    text = re.sub(r'нг', 'ң', text)
    text = re.sub(r'га|го|гө', 'х', text)
    text = re.sub('ж', 'җ', text)
    text = re.sub('ээс', 'әс', text)
    text = re.sub(r'багатур', 'баатр', text)
    text =text.strip()
    text = ' '.join([reduce_symbols(word) for word in text.split(' ')])
    text = re.sub(' хүйтн', ' киитн', text)
    return text

gset = set('аояиэуюәүөе')
kgset = set('ә')

def reduce_symbols(word):
    i = 0
    j = 0
    new_word = ''
    first_slog = 1
    if len(word)> 3:
        while i < len(word):
            if (word[i] in gset):
                if first_slog:
                    new_word +=word[i]
                    first_slog = 0
                elif (word[i] in kgset):
                    new_word +=word[i]
                elif i+1 < len(word):
                    if (word[i+1] == word[i]) or (word[i+1]) == 'й':
                        new_word +=word[i]
                        i+=2
                        continue
            else:
                new_word +=word[i]
            i+=1
    else:
        new_word = word
    return new_word

text1 = st.text_area("Enter text:", value="тэнггэрийн бошгоор")

st.write(to_kalmyk(text1))
st.write('теңгрин бошгар')

text2 = st.text_area("Enter text:", value="хийсвээс тэнггэрийн доор, хэлвээс ноёдын доор")

st.write(to_kalmyk(text2))
st.write('киисвәс теңгрин дор, келвәс нойдын дор')

text3 = st.text_area("Enter text:", value="тэнггэрийн заяа цагийн улирал дагаж")

st.write(to_kalmyk(text3))
st.write('теңгрин заян цагин ульрл дахҗ')

text3 = st.text_area("Enter text:", value="нар буцахад эхлэдэг хүйтний наян нэг хоногийг есөн ес гэнэ")

st.write(to_kalmyk(text3))
st.write('Нарн буцхд эклдг киитниг найн нег хонгиг йисн йис гинә')
#хоёр есийн хүйтэнд хорз архи хөлдөнө 

text3 = st.text_area("Enter text:", value="хоёр есийн хүйтэнд хорз архи хөлдөнө э")

st.write(to_kalmyk(text3))
st.write('хойр йисин киитнд хорз әрк көлднә')





