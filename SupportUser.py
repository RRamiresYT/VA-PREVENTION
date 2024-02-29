class SupportUser:
    def __init__(self, username, age, gender):
        self.username = username
        self.age = age
        self.gender = gender
        self.supportersUsername = []

    def addSupporter(self, primaryUser):
        self.supportersUsername.append(primaryUser)

    def showSupporter(self):
        for user in self.supportersUsername:
            print(user.username) 