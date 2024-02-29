from flask import jsonify
import json
from datetime import datetime
#import DBHandler

# ---------------------------------   MOTOR DE DIÁLOGO   ---------------------------------

def get_next_phase(current_phase):
    # Your logic to determine the next phase based on the current phase
    phases = ['opening', 'reviewTasks', 'assess', 'assignTasks', 'counselling', 'closing']
    if current_phase in phases:
        current_index = phases.index(current_phase)
        if current_index < len(phases) - 1:
            return phases[current_index + 1]
    return None

def get_dialogue(phase):
    if phase == 'opening':
        return getOpening()
    elif phase == 'reviewTasks':
        return getReviewTasks()
    elif phase == 'assess':
        return getAssess()
    elif phase == 'assignTasks':
        return getAssignTasks()
    elif phase == 'counselling':
        return getCounselling()
    elif phase == 'closing':
        return getClosing()
    else:
        return None


def motorDeDialogo(fase="opening"):
    """
    Seleciona o dia atual
    Base de dados: o dia inicial do dia de referência, o hábito a ser trabalhado neste momento, número de sessões (Para saber se é motivacinal ou não.
    """
    dataAtual = datetime.datetime.now()
    diaAtual = dataAtual.day

    #diaInicial = Chamar à base de dados
    #habito = Habito a ser trabalhado da base de dados
    #if habito == "AtFisica":
        #motorDeDialogoAtFisica():
    #else:
        #motorDeDialogoAlimentacao(diaAtual, diaInicial, habito, fase):
        

def motorDeDialogoAlimentacao():
    """
    Chamado pelo motorDeDialogo(), desenhado para a fase de acompanhamento da alimentação
    """

def motorDeDialogoAtFisica():
    """
    Chamado pelo motorDeDialogo(), desenhado para a fase de acompanhamento da alimentação
    """
    
# ---------------------------------   ACOMPANHAMENTO   ---------------------------------
def getCounselling():
    """
    Lê as perguntas do counselling e envia-as para a API
    """
    try:
        with open("counselling.json", "r", encoding='utf-8') as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})
            
            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return

def getSolutions(data, category, barrier):
    """
    Seleciona as soluções e diálogos de uma determinada barreira de categoria
    """
    if category in data and barrier in data[category]:
        solutions = data[category][barrier]
        response = {
            'category': category,
            'barrier': barrier,
            'solutions': solutions
        }
        return jsonify(response)
    else:
        return jsonify({'error': 'Category or barrier not found'}), 404

def getOpening():
    """
    Lê os diálogos do opening.json e envia-as para o motor
    """
    print("QUANDO LIGA")
    try:
        with open("opening.json", "r", encoding='utf-8') as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})
            
            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return

def getReviewTasks():
    """
    Lê os diálogos do reviewTasks.json e envia-as para o motor
    """
    try:
        with open("reviewTasks.json", "r", encoding='utf-8') as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})
            
            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return

def getAssess():
    """
    Lê os diálogos do assess.json e envia-as para o motor
    """
    try:
        with open("assess.json", "r", encoding='utf-8') as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})
            
            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")

def getAssignTasks():
    """
    Lê os diálogos do assignTasks.json e envia-as para o motor
    """
    try:
        with open("assignTasks.json", "r", encoding='utf-8') as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})
            
            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")

def getClosing():
    """
    Lê os diálogos do closing.json e envia-as para o motor
    """
    try:
        with open("closing.json", "r", encoding='utf-8') as json_file:
            questions = json.load(json_file)

            jsonify({'result': questions})
            
            return questions
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
