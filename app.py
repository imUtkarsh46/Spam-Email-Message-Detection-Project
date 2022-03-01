import streamlit as st
import pickle

import nltk
import string
from nltk.corpus import stopwords
stopwords.words('english')
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()





tf = pickle.load(open('Vectorizer.pkl', 'rb'))
model = pickle.load(open('Model.pkl', 'rb'))

def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

st.title("Email/SMS Spam Detection Tool")
input_msg = st.text_area('Enter The Message or Email...')
if st.button('Predict'):
    transform_msg = text_transform(input_msg)
    vector_input = tf.transform([transform_msg])
    result = model.predict(vector_input)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")







