import mysql.connector

class dataBase ():
  def __init__(self):
    self.mydb = mysql.connector.connect(host="localhost", user="root", password="1512", database="agilim")
    self.mycursor = self.mydb.cursor()

  def init_dataBase(self, tableName):
      self.mycursor.execute(
          "CREATE TABLE " + tableName + " (id INT AUTO_INCREMENT PRIMARY KEY,"
          "date VARCHAR(1255),"
          "team VARCHAR(1255)," 
          "delivery INT,"
          "strength VARCHAR(1255),"
          "improvement VARCHAR(1255)," 
          "felling VARCHAR(1255),"
          "evaluation VARCHAR(1255))"
          )

  def add(self, val, tableName):
      sql = "INSERT INTO " + tableName + " (date, team, delivery, strength, improvement, felling, evaluation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      self.mycursor.execute(sql, val)
      self.mydb.commit() # (?)

  def showInstances(self, tableName):
      self.mycursor.execute("SELECT * FROM " + tableName)
      myresult = self.mycursor.fetchall()
      for x in myresult:
          print(x)

  def verifyIni(answer):
      return ((answer[4] == "-") & (answer[7] == "-") & (answer[10] == "T") & (answer[13] == ":") &        
              (answer[16] == ":") & (answer[19] == "Z"))

  def verifyEnd(answer):
      return (((answer[len(answer)-1] == "1") & (answer[len(answer)-2] == ",") & 
              (answer[len(answer)-3] == "%")))

  def deleteTableDB(self, tableName):
      self.mycursor.execute("DROP TABLE " + tableName)
      self.mydb.commit()

  # Call examples: updateMySQL("./files/Agilim_Outubro.csv", "instances") // updateMySQL("./files/Agilim_Janeiro23_Quinzena01.csv", "instances")
  def updateMySQL(self, fileCSV, tableName):
      fileTest = open(fileCSV, encoding='utf-8', mode='r')
      head = fileTest.readline()
      content = fileTest.read()
      answers = content.splitlines()
      for ind in range(0, len(answers)-1):
          if (self.verifyIni(answers[ind])): 
              if (self.verifyEnd(answers[ind])):
                  dados = answers[ind].split('       ')
                  dados[6] = dados[6][:len(dados[6])-8]
                  self.add(dados, tableName)
              else:
                  answers[ind+1] = answers[ind] + answers[ind + 1]
                  ind = ind + 1

if __name__ == '__main__':
    db = dataBase()
    db.showInstances('instances')
