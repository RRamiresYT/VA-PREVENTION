import json
import DialogueMotor
from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
import AvaliationHandler
import AcompanhamentoHandler
#import DBHandler

app = Flask(__name__)
CORS(app)

# ---------------------------------   AVALIAÇÃO DA ALIMENTAÇÂO   ---------------------------------
@app.route('/getAvaliation', methods=['GET'])
def get_avaliation():
    """
    Envia as perguntas do Medas para o FrontEnd
    """
    try:
        result = AvaliationHandler.getAvaliation()
        if result is not None:
            #result.headers.add('Content-Type', 'application/json; charset=utf-8')
            return result
        else:
            return jsonify({'error': 'Failed to retrieve medas data'}), 500

    except Exception as error:
        print(error)
        return jsonify({'error': 'Failed to retrieve medas data'}), 500
    
@app.route('/postAvaliation', methods=["POST"])
def post_avaliation():
    """
    Recebe as respostas da avaliação e envia-as para o BackEnd
    """
    print("ENTREI")
    dados = request.get_json()
    print(dados)

    result = AvaliationHandler.postAvaliation(dados)
    
    # AvaliationHandler.postAvaliation(dados)
    return jsonify({'message': 'Data added successfully'}), 201

@app.route('/getHabitsN', methods=["GET"])
def get_habitsN():
    userN = 3 #Mudar para request.get_json()

    result = AvaliationHandler.getHabitosN(userN)

    if result is not None:
        return result
    else:
        return jsonify({'error': 'Failed to retrieve habits data'}), 500

    return result
    

# ---------------------------------   AVALIAÇÃO DA ATIVIDADE FÍSICA   ---------------------------------
@app.route('/getAvaliationT', methods=['GET'])
def get_avaliationt():
    """
    Envia as perguntas da avaliação física para o FrontEnd
    """
    try:
        result = AvaliationHandler.getAvaliationT()
        if result is not None:
            return result
        else:
            return jsonify({'error': 'Failed to retrieve physical questions data'}), 500

    except Exception as error:
        print(error)
        return jsonify({'error': 'Failed to retrieve physical questions data'}), 500

@app.route('/getBarriersT', methods=['GET'])
def get_barrierst():
    """
    Envia as barreiras da avaliação física para o FrontEnd
    """
    try:
        result = AvaliationHandler.getBarriersT()
        if result is not None:
            return result
        else:
            return jsonify({'error': 'Failed to retrieve physical barriers data'}), 500

    except Exception as error:
        print(error)
        return jsonify({'error': 'Failed to retrieve physical barriers data'}), 500

@app.route('/postAvaliationAF', methods=["POST"])
def post_avaliationAF():
    """
    Recebe as respostas da avaliação e envia-as para o BackEnd
    """
    print("ENTREI")
    dados = request.get_json()
    print(dados)

    result = AvaliationHandler.postAvaliationAF(dados)
    
    # AvaliationHandler.postAvaliation(dados)
    return jsonify({'message': 'Data added successfully'}), 201

# ---------------------------------   TESTE HELLO WORLD!   ---------------------------------
@app.route('/testeHello', methods=["GET"])
def testeHello():
    """
    testeHelloWorld
    """
    try:
        result = "Hello World!"
        if result is not None:
            return jsonify({'message': result})
        else:
            return jsonify({'error': 'Failed to retrieve medas data'}), 500

    except Exception as error:
        print(error)
        return jsonify({'error': 'Failed to retrieve medas data'}), 500

# ---------------------------------   ACOMPANHAMENTO   ---------------------------------
@app.route('/getOpeningPhaseDialogue', methods=['GET'])
def get_opening():
    dialogue = AcompanhamentoHandler.get_dialogue("opening")
    print(dialogue)
    next_phase = "opening"
    if dialogue is not None:
        dialogue['nextPhase'] = next_phase
        return jsonify(dialogue)
    else:
        return jsonify({'error': 'Falha a obter o dialogo'}), 500

@app.route('/getNextPhaseDialogue', methods=['GET'])
def get_next_phase_dialogue():
    current_phase = request.args.get('currentPhase')
    print(current_phase)
    next_phase = AcompanhamentoHandler.get_next_phase(current_phase)
    print(next_phase)
    dialogue = AcompanhamentoHandler.get_dialogue(next_phase)
    print(dialogue)
    if dialogue is not None:
        dialogue['nextPhase'] = next_phase
        return jsonify(dialogue)
    else:
        return jsonify({'error': 'Falha a obter o dialogo'}), 500

@app.route('/getDialogosBarreiras', methods=['GET'])
def get_dialogosBarreiras():
    """
    Vai buscar os dialogos das barreiras selecionando as solucoes especificas da barreira e devidos dialogos
    """
    try:
        result = AcompanhamentoHandler.getCounselling()
        result = AcompanhamentoHandler.getSolutions(result, "1.Azeite", "Não sei como usar o azeite para cozinhar e temperar no meu dia-a-dia")
        print(result)
        if result is not None:
            return result
        else:
            return jsonify({'error': 'Falha a devolver as barreiras'}), 500

    except Exception as error:
        print(error)
        return jsonify({'error': 'Falha a devolver as barreiras'}), 500



if __name__ == "__main__":
    app.run(debug=True)
