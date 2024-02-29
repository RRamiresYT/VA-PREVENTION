import json

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
        self.medasDict = {"m1": None, "m2": None, "m3": None, "m4": None, "m5": None, "m6": None, "m7": None, "m8": None, "m9": None, "m10": None, "m11": None}
        self.day = 0

    def medas(self):
        if self.day == 0:
            print("É bastante importante que responda às perguntas seguintes de modo a ter o melhor acompanhamento possível!")
            questions = {
                1: "Pergunta Medas 1? (S/N)",
                2: "Pergunta Medas 2? (S/N)",
                3: "Pergunta Medas 3? (S/N)",
                4: "Pergunta Medas 4? (S/N)",
                5: "Pergunta Medas 5? (S/N)",
                6: "Pergunta Medas 6? (S/N)",
                7: "Pergunta Medas 7? (S/N)",
                8: "Pergunta Medas 8? (S/N)",
                9: "Pergunta Medas 9? (S/N)",
                10: "Pergunta Medas 10? (S/N)",
                11: "Pergunta Medas 11? (S/N)"
            }

            for i in range(1, 12):
                response = input(questions[i])
                self.medasDict[f"m{i}"] = response

            print("As suas respostas ao Medas foram guardadas")
            self.day = 1

        else: # Questionar pergunta(s) a ser alterada(s), questionar e alterar valores pedidos
            questions = {
                1: "Pergunta Medas 1? (S/N)",
                2: "Pergunta Medas 2? (S/N)",
                3: "Pergunta Medas 3? (S/N)",
                4: "Pergunta Medas 4? (S/N)",
                5: "Pergunta Medas 5? (S/N)",
                6: "Pergunta Medas 6? (S/N)",
                7: "Pergunta Medas 7? (S/N)",
                8: "Pergunta Medas 8? (S/N)",
                9: "Pergunta Medas 9? (S/N)",
                10: "Pergunta Medas 10? (S/N)",
                11: "Pergunta Medas 11? (S/N)"
            }

            for i in range(1, 12):
                response = input(questions[i])
                self.medasDict[f"m{i}"] = response

            print("As suas respostas ao Medas foram alteradas")

    def getMedas(self):
        for key, value in self.medasDict.items():
            print(f"{key}: {value}")

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


renato = PrimaryUser("renato", 22, "male", 70, 180)
renato.medas()
renato.getMedas()
#renato.initDialogue()
#renato.initDialogue()
#renato.initDialogue()
#renato.initDialogue()
#print(renato.__str__())
