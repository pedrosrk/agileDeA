import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from mainDB import dataBase as db

class dataAnalisis:
  def __init__(self):
    self.aglDB = db()

  def correlationFellingDeliveryScatter(self):
    x_axis = self.aglDB.extractFellingList()
    y_axis = self.aglDB.extractDeliveryList()
    x = np.array(x_axis)
    y = np.array(y_axis)
    plt.scatter(x, y)
    plt.show()

  def correlationFellingDeliveryBar(self):
    x_axis = self.aglDB.extractFellingList()
    y_axis = self.aglDB.extractDeliveryList()
    x = np.array(x_axis)
    y = np.array(y_axis)
    plt.bar(x,y)
    plt.show()

  def corrDeliveryAndFelling(self):
    x = self.aglDB.extractDeliveryList()
    y = self.aglDB.extractFellingListInt()
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    def myfunc(x):
      return slope * x + intercept

    mymodel = list(map(myfunc, x))
    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()
    return r

if __name__ == '__main__':
  dados = db()
  print(dados.extractDeliveryList('instances'))
  