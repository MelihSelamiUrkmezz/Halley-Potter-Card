from flask import Flask, jsonify, request
import mysql.connector
import redis
r = redis.Redis(
    host='34.170.163.125',
    port=6379, 
    password='kouyazlab',
)

r.flushdb()
r.flushall()
# DB
def getCardsFromDb():
    cnx = mysql.connector.connect(user="root", password="yazlab123", host="34.71.163.17", database="memorygame")
    print(cnx)
    myCursor = cnx.cursor()
    response = []

    query = "SELECT c.id, c.name, c.score, h.Name, h.Score, c.image FROM Cards as c, Home as h WHERE c.home_id = h.id"
    try:
        myCursor.execute(query)

        result = myCursor.fetchall()
        
        for i in result:
            myDict = {}
            myDict["cardId"]=i[0]
            myDict["cardName"]=i[1]
            myDict["cardScore"]=i[2]
            myDict["homeName"]=i[3]
            myDict["homeScore"]=i[4]
            
            
            response.append(myDict)

    except Exception as e:
        print("hata")
    
    return response

    
# API  
app = Flask(__name__)

@app.route("/getCards", methods = ["GET"])
def getCard():
    if request.method == 'GET':     
        return jsonify(getCardsFromDb())
    return "Hata" 
    
    
app.run("0.0.0.0",debug=True,port=5001)
