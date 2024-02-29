import json
import DialogueMotor
from flask import Flask, jsonify
from flask_cors import CORS

##app = Flask(__name__)
##CORS(app)

class PrimaryUser:
    def __init__(self, username, age, gender, weightKG, heightCM, medications = "Nada", glucoseLevelMgL = None, familyHistory = None, lvlPhysicalAct = None):
        '''
        Inicializa um utilizador primário utilizando como default o valor None para algumas das informações
        '''
        self.username = username
        self.age = age
        self.gender = gender
        self.weightKG = weightKG
        self.heightCM = heightCM
        self.glucoseLevelMgL = glucoseLevelMgL
        self.familyHistory = familyHistory
        self.lvlPhysicalAct = lvlPhysicalAct
        self.medications = [medications.replace(" ", "").split(",")]
        self.medasDict = {"azeite": None, "horticolas": None, "fruta": None, "carne": None, "m5": None, "m6": None, "m7": None, "m8": None, "m9": None, "m10": None, "m11": None}
        self.medasBad = []
        self.day = 0
        self.dialogueMotor = DialogueMotor.DialogueMotor("opening")
    
##    def returnMedas(self):
##        try:
##            with open("medas.json", "r") as json_file:
##                questions = json.load(json_file)
##                return questions
##        except FileNotFoundError:
##            print(f"File not found: {json_file_path}")
##            return
##
##        return questions

    def medas(self):
        if self.day == 0:
            print("É bastante importante que responda às perguntas seguintes de modo a ter o melhor acompanhamento possível!")

            try:
                with open("medas.json", "r") as json_file:
                    questions = json.load(json_file)
            except FileNotFoundError:
                print(f"File not found: {json_file_path}")
                return

            #Para verificar se é assim ###############
            """
            file_name = "outputForHtml.txt"

            with open(file_name, 'w') as file:
                for item in questions:
                    file.write("%s\n" % item)
            """
            ###########################################

            for i, question in enumerate(questions, start=1):
                response = input(f"{question} ")
                self.medasDict[f"m{i}"] = response

            print("As suas respostas ao Medas foram guardadas")
            self.day = 1

        else: # Questionar pergunta(s) a ser alterada(s), questionar e alterar valores pedidos
            numero = input("Qual o número da pergunta que pretende alterar a sua resposta?")
            data = []
            with open("medas.json", 'r') as json_file:
                data = json.load(json_file)
            mensagem = data[int(numero)-1]
            valor = input(mensagem)

            key = "m"+numero
            self.medasDict[key] = valor
            

            print("As suas respostas ao Medas foram alteradas")

    def getMedas(self):
        for key, value in self.medasDict.items():
            print(f"{key}: {value}")

    def avaliacao(self):
        if self.medasDict["m1"] == "N":
            self.medasBad.append("m1")
            
        if self.medasDict["m2"] == "N":
            self.medasBad.append("m2")
            
        if int(self.medasDict["m3"]) < 2 or int(self.medasDict["m3"]) > 4:
            self.medasBad.append("m3")
            
        if self.medasDict["m4"] == "N":
            self.medasBad.append("m4")
            
        if self.medasDict["m5"] == "N":
            self.medasBad.append("m5")
            
        if self.medasDict["m6"] == "N":
            self.medasBad.append("m6")

        #Verificar bebidas 
        if self.medasDict["m7"] == "N":
            self.medasBad.append("m7")
            
        if int(self.medasDict["m8"]) < 3 or int(self.medasDict["m8"]) > 5:
            self.medasBad.append("m8")
            
        if int(self.medasDict["m9"]) < 2:
            self.medasBad.append("m9")
            
        if self.medasDict["m10"] == "N":
            self.medasBad.append("m10")
            
        if int(self.medasDict["m11"]) < 3 or int(self.medasDict["m11"]) > 5:
            self.medasBad.append("m11")

        print("Resultado da avaliação dos hábitos a melhorar:")
        for i in self.medasBad:
            print(i)

    def initDialogueMotor(self):
        self.dialogueMotor.initDialogue()

    def initDialogue(self):
        '''
        Inicializa um diálogo básico perguntando sobre informação que existe em falta ou perguntando se deve alterar alguma informação caso já tenha a informação completa
        '''
        # Fazer algumas perguntas
        self.day += 1
        print("Olá, eu sou a Ema!")
        if self.glucoseLevelMgL == None:
            resposta = input("É importante saber o seu nível de glucose em mg/L? Sabe dizer-me o valor? (S/N)")
            if resposta == "N":
                print("Não há problema! Se possível tente informar-se para me facultar essa informação uma próxima vez :)")
            else:
                valor = input("Qual o valor?")
                print("Irei registar o valor! Obrigado")
                self.glucoseLevelMgL = float(valor)
        
        if self.familyHistory == None:
            resposta = input("Relativamente ao histórico da família, sabe dizer-me se tem algum parente com Diabetes? (S/N)")
            if resposta == "N":
                print("Não há problema! Se possível tente informar-se para me facultar essa informação uma próxima vez :)")
            else:
                historico = input("Existe historial na família? (S/N)")
                if historico == "S":
                    self.familyHistory = True
                else:
                    self.familyHistory = False
                print("Obrigado, irei registar a informação!")

        if self.lvlPhysicalAct == None:
            resposta = input("Se tivesse de avaliar de 1 a 5 o nível de exercício físico que pratica no dia a dia, qual seria o valor? (1 - Sedentário... 5 - Extremamente Ativo)")
            self.lvlPhysicalAct = int(resposta)
            if int(resposta) == 1 or 2:
                print("Obrigado! Vou registar o valor na expectativa de mudar em breve :)")

            elif int(resposta) == 3 or 4 or 5:
                print("Excelente notícia! Irei registar a informação")

        if self.glucoseLevelMgL != None and self.familyHistory != None and self.lvlPhysicalAct != None:
            resposta = input("As suas informações estão completas! Existe alguma que deseja mudar? (S/N)")
            if resposta == "S":
                self.changeValues()
            else:
                print("Obrigado pela interação!!")

    def changeValues(self):
        '''
        Permite alterar valores das informações do utilizador primário
        '''
        resposta = input("Que informação pretende alterar?")
        if resposta == "username":
            newUsername = input("Escreva o seu novo username")
            self.username = newUsername

        elif resposta == "age":
            newAge = input("Escreva o seu novo age")
            self.age = newAge

        elif resposta == "gender":
            newGender = input("Escreva o seu novo gender")
            self.gender = newGender

        elif resposta == "weight":
            newWeight = input("Escreva o seu novo weight")
            self.weightKG = newWeight

        elif resposta == "height":
            newHeight = input("Escreva o seu novo username")
            self.heightCM = newHeight

        elif resposta == "glucose":
            newGlucose = input("Escreva o seu novo username")
            self.glucoseLevelMgL = newGlucose

        elif resposta == "family":
            newFamily = input("Escreva o seu novo family(S/N)")
            if newFamily == "S":
                self.familyHistory = True
            elif newFamily == "N":
                self.familyHistory = False
            else:
                print("Resposta Inválida")

        elif resposta == "physical":
            newPhysical = input("Escreva o seu novo physical")
            self.lvlPhysicalAct = newPhysical

        elif resposta == "addMedication":
            newMedication = input("Escreva a sua nova medication")
            self.medications.append(newMedication)

        elif resposta == "removeMedication":
            newMedication = input("Escreva a medicação a remover")
            self.medications.remove(newMedication)
                
    
    def __str__(self):
        '''
        Cria uma string com as informações todas do utilizador primário
        '''
        return f"Username: {self.username}\nAge: {self.age}\nGender: {self.gender}\nWeight (KG): {self.weightKG}\nHeight (CM): {self.heightCM}\nMedications: {', '.join(self.medications[0])}\nGlucose Level (mg/L): {self.glucoseLevelMgL}\nFamily History: {self.familyHistory}\nPhysical Activity Level: {self.lvlPhysicalAct}"

##@app.route('/initialEvaluation', methods=['GET'])
##def call_class_method():
##    renato = PrimaryUser("renato", 22, "male", 70, 180)
##    result = renato.returnMedas()
##    print(result)
##    
##    if result is not None:
##        return jsonify({'result': result})
##    else:
##        return jsonify({'error': 'Failed to retrieve medas data'}), 500
##
##@app.route('/initialEvaluation', methods=["POST"])
##
##if __name__ == "__main__":
##    app.run(debug=True)


renato = PrimaryUser("renato", 22, "male", 70, 180)
renato.medas()
renato.getMedas()
renato.avaliacao()
renato.initDialogueMotor()
renato.getMedas()
renato.medas()
renato.getMedas()

#renato.medas()
#renato.getMedas()
#renato.initDialogue()
#renato.initDialogue()
#renato.initDialogue()
#renato.initDialogue()
#print(renato.__str__())
