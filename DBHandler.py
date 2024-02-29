import mysql.connector

db = mysql.connector.connect(host='prodmysql03.fc.ul.pt',
                     user='vaprevention',
                     password='Qp4AyAw4mbUn3QRV',
                     database='db_vaprevention')
mysql = db.cursor()

def insertAvaliacao(insertStatement):
    try:
        sql = "INSERT INTO answers (azeite, horticolas, fruta, carne, gorduras, refrigerantes, alcool, leguminosas, peixe, pastelaria, oleaginosas, user_id, answer_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mysql.execute(sql, insertStatement)
        db.commit()
        return "Data inserted."
    except Exception as error:
        return error

    return "teste"

def selectHabitosN(userN):
    try:
        #sql = f"SELECT COLUMN_NAME INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'db_vaprevention' AND TABLE_NAME = 'answers';"
        sql = f"SELECT * FROM answers WHERE user_id = '{userN}' ORDER BY answer_date DESC LIMIT 1"
        mysql.execute(sql)
        result = mysql.fetchall()
        #for row in result:
            #print(row)

    except Exception as error:
        return error

    return result
