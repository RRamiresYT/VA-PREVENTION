import json
import random

class DialogueMotor:
    def __init__(self, currentAction):
        '''
        Inicializa uma instância do Motor de Diálogo 
        '''
        # States possíveis da conversa
        self.allActions = ["opening", "socialTalk", "reviewTasks", "acess", "conseling", "assignTasks", "preClosing", "closing"]
        # Quantidade de mensagens necessárias por estate
        self.quantidade = [0, 2, 0, 0, 0, 0, 1, 0]
        # Total de mensagens que faltam do State atual
        self.total = 0
        # State atual
        self.currentAction = currentAction
        # Listas para carregar os json
        self.opening = []
        self.socialTalk = []
        self.reviewTasks = []
        self.acess = []
        self.conseling = []
        self.assignTasks = []
        self.preClosing = []
        self.closing = []

    def getCurrentAction(self):
        '''
        Retorna o state atual do diálogo
        '''
        return self.currentAction

    def furfillLists(self, currentAction):
        '''
        Carrega o json com as mensagens possíveis para o state atual
        '''
        fileName = currentAction + ".json"
        data = None
        try:
            with open(fileName, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            # Handle the case when the file doesn't exist, e.g., you can set data to an empty list or handle it as needed.
            data = []
        
        if currentAction == "opening":
            self.opening.extend(data)

        elif currentAction == "socialTalk":
            self.socialTalk.extend(data)
            
        elif currentAction == "reviewTasks":
            self.reviewTasks.extend(data)
            
        elif currentAction == "acess":
            self.acess.extend(data)
            
        elif currentAction == "conseling":
            self.conseling.extend(data)
            
        elif currentAction == "assignTasks":
            self.assignTasks.extend(data)
            
        elif currentAction == "preClosing":
            self.preClosing.extend(data)
            
        elif currentAction == "closing":
            self.closing.extend(data)

    def initDialogue(self):
        '''
        Escolhe aleatóriamente uma mensagem das possíveis e alterna os states
        '''
        dialogue = True
        while dialogue:
            #
            self.furfillLists(self.currentAction)
            dialogue_list = []
            if self.currentAction == "opening":
                dialogue_list = self.opening

            elif self.currentAction == "socialTalk":
                dialogue_list = self.socialTalk
                
            elif self.currentAction == "reviewTasks":
                dialogue_list = self.reviewTasks

            elif self.currentAction == "acess":
                dialogue_list = self.acess

            elif self.currentAction == "conseling":
                dialogue_list = self.conseling

            elif self.currentAction == "assignTasks":
                dialogue_list = self.assignTasks

            elif self.currentAction == "preClosing":
                dialogue_list = self.preClosing

            elif self.currentAction == "closing":
                dialogue_list = self.closing

            else:
                print("Invalid currentAction")
                return

            if len(dialogue_list) > 0:
                fala = random.choice(dialogue_list)
                input(fala)

            else:
                print("The selected list is empty")

            if self.total == 0:
                if self.currentAction == "closing":
                    print("---------- Conversa fechada ----------")
                    dialogue = False

                else:
                    posicao = self.allActions.index(self.currentAction)
                    self.total = self.quantidade[posicao+1]
                    self.currentAction = self.allActions[posicao+1]
                    
            else:
                self.total = self.total - 1
            
        


#dm = DialogueMotor("opening")
#dm.initDialogue()


