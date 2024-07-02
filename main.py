from flask import Flask,render_template
import random as rand
import pandas as pd

app=Flask(__name__)

dataset = pd.read_csv('dataset/AnimeQuotes.csv', encoding='utf-8')


def generate_quote():
  random_quote = dataset.sample(n=1).iloc[0]
  return {
    'quote':random_quote['Quote'],
    'character':random_quote['Character'],
    'anime':random_quote['Anime']
  }

@app.route('/')
def show():
  quote=generate_quote()
  return render_template('index.html',quote=quote) #one is the variable in python file the other on the .html file

if __name__=='__main__':
  app.run(debug=True)