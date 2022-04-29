import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import numpy as np

#title
st.title('Tweet Sentiment Analysis')
#sidebar
st.sidebar.title('Sentiment analysis of twitter')
# sidebar markdown 
st.sidebar.markdown("We can analyse users review from this application.")

data=pd.read_csv('../sentiment_tweet_data.csv')
#checkbox to show data 
if st.checkbox("Show Data"):
    st.write(data.head(50))

st.sidebar.subheader('Tweets Analyser')
#radio buttons
tweets=st.sidebar.radio('Sentiment Type',('positive','negative'))
st.write(data.query('score==@tweets')[['original_text']].sample(1).iat[0,0])

select=st.sidebar.selectbox('Visualisation Of Tweets',['Histogram','Pie Chart'],key=1)
sentiment=data['score'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})
st.markdown("###  Sentiment count")
if select == "Histogram":
        fig = px.bar(sentiment, x='Sentiment', y='Tweets', color = 'Tweets', height= 500)
        st.plotly_chart(fig)
else:
        fig = px.pie(sentiment, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)