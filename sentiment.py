import pickle
import streamlit as st

model = pickle.load(open('sentiment_analysis_model.p', 'rb'))

st.title('Sentiment Analysis Model')

st.write('Enter Text for sentiment analysis')
message = st.text_area("", "Type Here....")
if st.button('PREDICT'):
    disp = " "
    a = model.predict([message])[0]
    if(a==1):
        disp = "Positive Sentiment"
    else:
        disp = "Negative Sentiment"
    st.write('The sentiment of given text is :', disp)