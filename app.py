import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from mainDB import dataBase as db
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class dataAnalysis:
  def __init__(self, text = "I love the computer sicence", model = "Default"):
    self.aglDB = db() # Agilim's database
    self.text = text
    self.model = model

  def getText(self):
    return self.text
  
  def setText(self, message):
    self.text = message

  def getModel(self):
    return self.model
  
  def setModel(self, model):
    self.text = model
  
  def englishSentiment(self): #tests Defaut message = Positive; dados.setText('I need study to the next test') = Neutral; dados.setText('I hate this job') = Negative;
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(self.text)
    if (scores['compound'] > 0.3333):
     result = 'Positive'
    elif (scores['compound'] > -0.3333):
      result = 'Neutral'
    else:
      result = 'Negative'
    return result
  
  def sentimentMultinomialNBModel(self):
    dataset = pd.read_csv('files/Tweets_Mg.csv',encoding='utf-8') #production
    #dataset = pd.read_csv('Tweets_Mg.csv',encoding='utf-8') #test
    tweets = dataset["Text"].values
    classes = dataset["Classificacao"].values
    vectorizer = CountVectorizer(analyzer = "word")
    freq_tweets = vectorizer.fit_transform(tweets)
    modelo = MultinomialNB()
    modelo.fit(freq_tweets, classes)
    if self.getText() == 'I love the computer sicence':
      self.setText('Eu amo a ciência da computação')
    example = [self.text]
    freq_teste = vectorizer.transform(example)
    result = modelo.predict(freq_teste)[0]
    if (result == 'Positivo'):
     result = 'Positive'
    elif (result == 'Neutro'):
      result = 'Neutral'
    else:
      result = 'Negative'
    return result

  def correlationFellingDeliveryScatter(self):
    x_axis = self.aglDB.extractFellingList('instances')
    y_axis = self.aglDB.extractDeliveryList('instances')
    x = np.array(x_axis)
    y = np.array(y_axis)
    plt.scatter(x, y)
    plt.show()

  def correlationFellingDeliveryBar(self):
    x_axis = self.aglDB.extractFellingList('instances')
    y_axis = self.aglDB.extractDeliveryList('instances')
    x = np.array(x_axis)
    y = np.array(y_axis)
    plt.bar(x,y)
    plt.show()

  def corrDeliveryAndFelling(self):
    x = self.aglDB.extractDeliveryList('instances')
    y = self.aglDB.extractFellingListInt('instances')
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    def myfunc(x):
      return slope * x + intercept

    mymodel = list(map(myfunc, x))
    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()
    return r

if __name__ == '__main__':
  dados = dataAnalysis()
  print(dados.getText())
  print(dados.sentimentMultinomialNBModel())
  print(dados.getText())
  
  
  