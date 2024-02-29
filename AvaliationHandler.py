from flask import jsonify
import json
from datetime import datetime
import DBHandler


# ---------------------------------   AVALIAÇÃO DA ALIMENTAÇÂO   ---------------------------------
def getAvaliation():
    """
    Lê as perguntas do Medas e envia-as para a API
    """
    try:
        with open("medas.json", "r", encoding='utf-8') as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})
            
            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return

def postAvaliation(dados):
    """
    Recebe as respostas da API e dá INSERT na DB
    """
    for key in dados:
        if dados[key] == 'Nao':
            dados[key] = 'N'
        elif dados[key] == 'Sim':
            dados[key] = 'Y'
        elif dados[key] == 'Nao aplicavel':
            dados[key] = 'NA'
    try:
        azeite=dados["azeite"]
        horticolas=dados["horticolas"]
        fruta=dados["fruta"]
        carne=dados["carne"]
        gorduras=dados["gorduras"]
        refrigerantes=dados["refrigerantes"]
        alcool=dados["alcool"]
        leguminosas=dados["leguminosas"]
        peixe=dados["peixe"]
        pastelaria=dados["pastelaria"]
        oleaginosas=dados["oleaginosas"]
        user_id=3
        
        insertStatement=(azeite, horticolas, fruta, carne, gorduras, refrigerantes, alcool, leguminosas, peixe, pastelaria, oleaginosas, user_id, datetime.now())
        result = DBHandler.insertAvaliacao(insertStatement)

    except Exception as error:
        print(error)
        return

def getHabitosN(userN):
    results = DBHandler.selectHabitosN(userN)
    print(results)
    print("A")


    #TESTE

    azeite=results[0][1]
    horticolas=results[0][2]
    fruta=results[0][3]
    carne=results[0][4]
    gorduras=results[0][5]
    refrigerantes=results[0][6]
    alcool=results[0][7]
    leguminosas=results[0][8]
    peixe=results[0][9]
    pastelaria=results[0][10]
    oleaginosas=results[0][11]

    variables_with_N = []

    if azeite == "N":
        variables_with_N.append("azeite")
    if horticolas == "N":
        variables_with_N.append("horticolas")
    if fruta == "N":
        variables_with_N.append("fruta")
    if carne == "N":
        variables_with_N.append("carne")
    if gorduras == "N":
        variables_with_N.append("gorduras")
    if refrigerantes == "N":
        variables_with_N.append("refrigerantes")
    if alcool == "N":
        variables_with_N.append("alcool")
    if leguminosas == "N":
        variables_with_N.append("leguminosas")
    if peixe == "N":
        variables_with_N.append("peixe")
    if pastelaria == "N":
        variables_with_N.append("pastelaria")
    if oleaginosas == "N":
        variables_with_N.append("oleaginosas")

    print("Variables with value 'N':", variables_with_N)

    with open("medas.json", "r") as json_file:
        questions = json.load(json_file)
    
    filtered_questions = {key: questions[key] for key in variables_with_N if key in questions}

    print(filtered_questions)
    return filtered_questions
    

    #return results
    
# ---------------------------------   AVALIAÇÃO DA ATIVIDADE FÍSICA   ---------------------------------
def getAvaliationT():
    """
    Lê as perguntas da Atividade Física e envia-as para a API
    """
    try:
        with open("perguntasAF.json", "r") as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})

            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return

def getBarriersT():
    """
    Lê as perguntas da Atividade Física e envia-as para a API
    """
    try:
        with open("barreirasAF.json", "r") as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})

            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return

def postAvaliationAF(data):
    """
    Recebe os resultados das perguntas da atividade física
    """

    #Atividade Física Moderada
    # 6*7
    Q06 = int(data.get('Q06', 0))
    Q07 = int(data.get('Q07', 0))
    Q07_numbers = int(data.get('Q07_numbers', 0))
    afm1 = Q06 * (Q07 * 60 + Q07_numbers)

    # 9*10
    Q09 = int(data.get('Q09', 0))
    Q10 = int(data.get('Q10', 0))
    Q10_numbers = int(data.get('Q10_numbers', 0))
    afm2 = Q09 * (Q10 * 60 + Q10_numbers)

    # 15*16
    Q15 = int(data.get('Q15', 0))
    Q16 = int(data.get('Q16', 0))
    Q16_numbers = int(data.get('Q16_numbers', 0))
    afm3 = Q15 * (Q16 * 60 + Q16_numbers)

    #Atividade Física Rigorosa
    # 3*4
    Q03 = int(data.get('Q03', 0))
    Q04 = int(data.get('Q04', 0))
    Q04_numbers = int(data.get('Q04_numbers', 0))
    afr1 = Q03 * (Q04 * 60 + Q04_numbers)

    # 12*13
    Q12 = int(data.get('Q12', 0))
    Q13 = int(data.get('Q13', 0))
    Q13_numbers = int(data.get('Q13_numbers', 0))
    afr2 = Q12 * (Q13 * 60 + Q13_numbers)

    afm = afm1 + afm2 + afm2
    afr = afr1 + afr2
    afTotal = afm + (2*afr)

    print(afm)
    print(afr)
    print(afTotal)

