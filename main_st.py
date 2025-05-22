import streamlit as st
import re

def to_kalmyk(text):
    text_was_upper = False
    if text == text.upper():
        text = text.lower()
        text_was_upper = True
    text = ' '+text + ' '
    text = re.sub('\.', ' . ', text)
    text = re.sub('\,', ' , ', text)
    text = re.sub('\!', ' ! ', text)
    text = re.sub('\?', ' ? ', text)
    text = re.sub(r'\bтэ', ' те', text)
    text = re.sub(r'\bяв', 'йов', text)
    text = re.sub(r'\bес', 'йис', text)
    text = re.sub(r'\bдэлхий', ' делкәә', text)
    text = re.sub(r'\bхөвөө', ' көвәә', text)
    text = re.sub(r'\bнэг\b', ' нег', text)
    text = re.sub(r'гэнэ', 'гинәә', text)
    text = re.sub(r'\bхүйт', ' киит', text)
    text = re.sub(r'\bхөрс', ' көрс', text)
    text = re.sub(r'\bдээ', ' дее', text)
    text = re.sub(r'\bдээ', ' дее', text)
    text = re.sub(r'\Bдээ\B', 'дә', text)
    text = re.sub(r'\Bдэ\B', 'д', text)
    text = re.sub(r'\bгээ', ' гее', text)
    text = re.sub(r'\bгээ', ' гее', text)
    text = re.sub(r'\Bгээ\B', 'гә', text)
    text = re.sub(r'\Bгэ\B', 'г', text)
    text = re.sub(r'\bсээ', ' сее', text)
    text = re.sub(r'\bсээ', ' сее', text)
    text = re.sub(r'\Bсээ\B', 'сәә', text)
    text = re.sub(r'\Bсэ\B', 'с', text)
    text = re.sub(r'\bмээ', ' мее', text)
    text = re.sub(r'\bмээ', ' мее', text)
    text = re.sub(r'\Bмээ\B', 'мәә', text)
    text = re.sub(r'\Bмэ\B', 'м', text)
    text = re.sub(r'\bбээ', ' бее', text)
    text = re.sub(r'\bбя', ' би', text)
    text = re.sub(r'\bбээ', ' бее', text)
    text = re.sub(r'\Bбээ\B', 'бәә', text)
    text = re.sub(r'\Bбэ\B', 'б', text)
    # text = re.sub('ийн ', 'ин ', text)
    # text = re.sub('ийг ', 'иг ', text)
    text = re.sub(r'\Bой', 'а', text)
    text = re.sub(r'\Bэй', 'ә', text)
    text = re.sub(r'\Bая\B', 'ай', text)
    text = re.sub(r'\Bлга\B|\Bлго\B|\Bлгө\B|\Bлгэ\B', 'лһ', text)
    text = re.sub(r'\Bб', 'в', text)
    text = re.sub(r'\Bцгаа\B|\Bцгоо\B', 'цхаа', text)
    text = re.sub(r'\Bцгөө\B|\Bцгээ\B', 'цхәә', text)
    text = re.sub(r'\Bнгуу\B', 'ңһуу', text)
    text = re.sub(r'\Bнгүү\B', 'ңгүү', text)
    text = re.sub(r'\Bнгөө\B', 'ңһәә', text)
    text = re.sub(r'\Bнгээ\B', 'ңгәә', text)
    text = re.sub(r'\Bгай', 'хаа', text)
    text = re.sub(r'\Bгэй\B', 'хәә', text)

    text = re.sub(r'\Bхул\B', 'хлаа', text)
    text = re.sub(r'\Bхүл\B', 'хләә', text)
    text = re.sub(r'\Bаарай|\Bоорой', 'аараа', text)
    text = re.sub(r'\Bөөрэй|\Bээрэй', 'әәрәә', text)
    text = re.sub(r'гтун |гтүн ', 'тн ', text)
    text = re.sub(r'уузай ', 'вза ', text)
    text = re.sub(r'үүзэй ', 'взә ', text)
    text = re.sub(r'тугай ', 'тха ', text)
    text = re.sub(r'түгэй ', 'тхә ', text)
    text = re.sub(r'гсад |гсөд |гсөд |гсэд ', 'сд ', text)

    text = re.sub(r'\Bвч', 'вчн', text)
    text = re.sub(r'\Bчих\B', 'чк', text)
    text = re.sub(r'\Bсхий\B', 'ск', text)
    text = re.sub(r'\Bхуй|\Bхүй|\Bахүй|\Bахүй', 'лһн', text)
    # text = re.sub('[\w]ээ', 'ее', text)
    text = re.sub('ё', 'й', text)
    text = re.sub(r'гоо', 'хаа', text)
    text = re.sub(r'үгүй ', 'угаа ', text)
    text = re.sub(r'гүй ', 'гоо ', text)
    # text = re.sub(r'нг', 'ң', text)
    text = re.sub(r'га|го|гө', 'х', text)
    text = re.sub('ж', 'җ', text)
    text = re.sub(r'\Bээс', 'әәс', text)
    text = re.sub(r'багатур', 'баатр', text)
    text =text.strip()
    # st.markdown(text)
    text = ' '.join([reduce_symbols(word) for word in text.split(' ')])

    if text_was_upper:
        text = text.upper()
    return text

def to_kalmyk_text(text):
    words = text.split(' ')
    for i in range(len(words)):
        words[i] = to_kalmyk(words[i])
    return ' '.join(words)

gset = set('аояиэуюәүөе')
# kgset = set('ә')

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
                elif i > 0 and word[i] ==word[i-1]:
                    new_word +=word[i]
                # elif (word[i] in kgset):
                #     new_word +=word[i]
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

st.write(to_kalmyk_text(text1))
st.write('теңгрин бошгар')

text2 = st.text_area("Enter text:", value="хийсвээс тэнггэрийн доор, хэлвээс ноёдын доор")

st.write(to_kalmyk_text(text2))
st.write('киисвәс теңгрин дор, келвәс нойдын дор')

text3 = st.text_area("Enter text:", value="тэнггэрийн заяа цагийн улирал дагаж")

st.write(to_kalmyk_text(text3))
st.write('теңгрин заян цагин ульрл дахҗ')

text3 = st.text_area("Enter text:", value="нар буцахад эхлэдэг хүйтний наян нэг хоногийг есөн ес гэнэ")

st.write(to_kalmyk_text(text3))
st.write('Нарн буцхд эклдг киитниг найн нег хонгиг йисн йис гинә')
#хоёр есийн хүйтэнд хорз архи хөлдөнө 

text3 = st.text_area("Enter text:", value="хоёр есийн хүйтэнд хорз архи хөлдөнө э")

st.write(to_kalmyk_text(text3))
st.write('хойр йисин киитнд хорз әрк көлднә')





