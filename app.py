import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class dataAnalisis:
  def __init__(self):
    mydb = mysql.connector.connect(host="localhost", user="root", password="1512", database="agilim")
    mycursor = mydb.cursor()
    self.mydb = mydb
    self.mycursor = mycursor

  def extractFellingList(self, tablename):
    self.mycursor.execute("SELECT felling FROM " + tablename)
    myresult = self.mycursor.fetchall()
    axis = []
    for x in myresult:
      axis.append(x[0])
    return axis

  def extractDeliveryList(self):
    self.mycursor.execute("SELECT delivery FROM tablename")
    myresult = self.mycursor.fetchall()
    axis = []
    for x in myresult:
      axis.append(int(x[0]))
    return axis

  def correlationFellingDeliveryScatter(self):
    x_axis = self.extractFellingList()
    y_axis = self.extractDeliveryList()
    x = np.array(x_axis)
    y = np.array(y_axis)
    plt.scatter(x, y)
    plt.show()

  def correlationFellingDeliveryBar(self):
    x_axis = self.extractFellingList()
    y_axis = self.extractDeliveryList()
    x = np.array(x_axis)
    y = np.array(y_axis)
    plt.bar(x,y)
    plt.show()

  def extractFellingListInt(self):
    self.mycursor.execute("SELECT felling FROM tablename")
    myresult = self.mycursor.fetchall()
    classes = []
    for aux in myresult:
      c1 = aux[0]
      add = True
      for i in classes:
        if i == c1:
          add = False
      if (add):
        classes.append(c1)
    axis = []
    for x in myresult:
      axis.append(classes.index(x[0]))
    return axis

  def corrDeliveryAndFelling(self):
    x = self.extractDeliveryList()
    y = self.extractFellingListInt()
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
  print(dados.extractFellingList('instances'))
  