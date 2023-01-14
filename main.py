import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1512",
  database="agilim"
)

mycursor = mydb.cursor()

def init_dataBase(tableName):
    mycursor.execute(
        "CREATE TABLE " + tableName + " (id INT AUTO_INCREMENT PRIMARY KEY,"
        "date VARCHAR(255),"
        "team VARCHAR(255)," 
        "delivery INT,"
        "strength VARCHAR(255),"
        "improvment VARCHAR(255)," 
        "felling VARCHAR(255),"
        "evaluation VARCHAR(255))"
        )

def add(val, tableName):
    sql = "INSERT INTO " + tableName + " (date, team, delivery, strength, improvment, felling, evaluation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def agilimToDB(path, csvName, tableName):
    header = ['data', 'time', 'entrega', 'positivo', 'melhoria', 'humor', 'avaliacao']
    with open(csvName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        lines = [line for line in open(path)]

        for i in range(1, len(lines)):
            tupla = lines[i].strip().split(',')
            dados = tupla[0].strip().split('       ')
            writer.writerow(dados)
            add(dados, tableName)

def showInstances(tableName):
    mycursor.execute("SELECT * FROM " + tableName)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def interationsToMySQL(csvOrigin, csvToStore, tableName): # ("instances", files\Agilim_Outubro.csv", "AgOutToDB.csv")
    init_dataBase(tableName) 
    agilimToDB(csvOrigin, csvToStore, tableName)
    showInstances(tableName)

if __name__ == '__main__':
  showInstances("answers")