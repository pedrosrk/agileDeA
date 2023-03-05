import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from mainDB import dataBase as db

class dataAnalisis:
  def __init__(self, text = "I love the computer sicence", model = "Default"):
    self.aglDB = db() # Agilim's database
    self.text = text
    self.model = model

  def getText(self):
    return self.text
  
  def setText(self, message):
    self.model = message

  def getModel(self):
    return self.model
  
  def setModel(self, model):
    self.text = model

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
  dados = dataAnalisis()
  dados.corrDeliveryAndFelling()
  