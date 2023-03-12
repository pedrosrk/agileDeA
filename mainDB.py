import mysql.connector
import bcrypt

class dataBase ():
  def __init__(self):
    self.mydb = mysql.connector.connect(host="localhost", user="root", password="1512", database="agilim")
    self.mycursor = self.mydb.cursor()
  
  # Get all users [Table: users]
  def get_users(self):
    query = "SELECT * FROM users"
    self.mycursor.execute(query)
    users = self.mycursor.fetchall()
    return users
  
  # Get a single user by user_id [Table: users]
  def get_user(self, user_id):
    query = "SELECT * FROM users WHERE id = %s"
    self.mycursor.execute(query, (user_id,))
    user = self.mycursor.fetchone()
    return user
  
  # Update a single user by user_id [Table: users]
  def update_user(self, user_id, newUser):
    user = self.get_user(user_id)
    if user:
      query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
      values = (newUser['name'], newUser['email'], user_id)
      self.mycursor.execute(query, values)
      self.mydb.commit()
      return values
    else:
       return 'User does not exist!'
    
  # Deleate a single user by user_id [Table: users]
  def delete_user(self, user_id):
    user = self.get_user(user_id)
    if user:
      query = "DELETE FROM users WHERE id = %s"
      self.mycursor.execute(query, (user_id,))
      self.mydb.commit()
      return user
    else:
       return 'User does not exist!'
    
  def create_user(self, data):
    query = "SELECT * FROM users WHERE name = %s"
    self.mycursor.execute(query, (data['name'],))
    user = self.mycursor.fetchone()
    if user:
       return {'message': 'Username already exist!'}
    else:
      query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
      password = data['password'].encode('utf-8')
      salt = bcrypt.gensalt(8)
      hash = bcrypt.hashpw(password, salt)
      values = (data['name'], data['email'], hash)
      self.mycursor.execute(query, values)
      self.mydb.commit()
      return {'message': 'New user created!'}

  # [Table: instances]
  def extractFellingList(self, tablename):
    self.mycursor.execute("SELECT felling FROM " + tablename)
    myresult = self.mycursor.fetchall()
    axis = []
    for x in myresult:
      axis.append(x[0])
    return axis
  
  def extractDeliveryList(self, tablename):
    self.mycursor.execute("SELECT delivery FROM " + tablename)
    myresult = self.mycursor.fetchall()
    axis = []
    for x in myresult:
      axis.append(x[0])
    return axis
  
  def extractFellingListInt(self, tablename):
    self.mycursor.execute("SELECT felling FROM " + tablename)
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
  
  def log_user(self, data):
    query = "SELECT * FROM users WHERE name = %s AND email = %s"
    self.mycursor.execute(query, (data['name'], data['email']))
    user = self.mycursor.fetchone()
    if user:
      userPassword = data['password']
      userBytes = userPassword.encode('utf-8')
      hash = user[3].encode('utf-8')
      result = bcrypt.checkpw(userBytes, hash) 
      if result:
        return {'message': 'User Logged'}
      else:
        return {'message': 'Password fail'}

    else:
      return {'message': 'Username does not exist!'}

  def unit_test_hashPass(self, user_id):
    user = db.get_user(user_id)
    hash = user[3].encode('utf-8')
    #print(hash)
    if user_id == 5:
      userPassword = 'test02'
    if user_id == 6:
       userPassword = 'testim'
    # encoding user password
    userBytes = userPassword.encode('utf-8')
    # checking password
    result = bcrypt.checkpw(userBytes, hash)
    return result
  
  def unit_test_logUser(self):
    db = dataBase()
    data = {
       "name": "testim",
       "email": "testim@znet.com.br",
       "password": "testim"
    }
    return db.log_user(data)['message'] == 'User Logged'
  
if __name__ == '__main__':
    db = dataBase()
    print(db.unit_test_logUser())


    