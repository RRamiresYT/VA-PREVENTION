import PrimaryUser
import SupportUser

class UserHandler:
    def __init__(self):
        self.users = []

    def addUser(self, user):
        if isinstance(user, PrimaryUser.PrimaryUser):
            self.users.append(user)
            print(f"User '{user.username}' foi adicionado com sucesso!")
        elif isinstance(user, SupportUser.SupportUser):
            self.users.append(user)
            print(f"User '{user.username}' foi adicionado com sucesso!")
        else:
            print("Tipo de utilizador incorreto")

    def remove_user(self, username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)
                print(f"User '{username}' removed successfully.")
                return
        print(f"User '{username}' not found.")

    def listUsers(self):
        if not self.users:
            print("No users in the system.")
        else:
            print("List of Users:")
            for user in self.users:
                print(f"- {user.username}")

    def listUsersDetail(self, username):
        for user in self.users:
            if user.username == username:
                if isinstance(user, PrimaryUser.PrimaryUser):
                    print("Username: " + user.username + "\nAge: " + str(user.age) + "\nGender: " + user.gender + "\nWeight (KG): " + str(user.weightKG) + "\nHeight (CM): " + str(user.heightCM) + "\nMedications: " + str(user.medications[0]) + "\nGlucose Level (mg/L): " + str(user.glucoseLevelMgL) + "\nFamily History: " + str(user.familyHistory) + "\nPhysical Activity Level: " + str(user.lvlPhysicalAct))
                elif isinstance(user, SupportUser.SupportUser):
                    print("Username: " + user.username + "\nAge: " + str(user.age) + "\nGender: " + user.gender + "\n Supporteds:")

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        print(f"User '{username}' not found.")

userHandler = UserHandler()
renato = PrimaryUser.PrimaryUser("renato", 22, "male", 70, 180)
jb = PrimaryUser.PrimaryUser("jb", 31, "male", 70, 180)
apc = PrimaryUser.PrimaryUser("apc", 32, "female", 70, 180)
mbc = PrimaryUser.PrimaryUser("mbc", 33, "female", 70, 180)
antonio = PrimaryUser.PrimaryUser("antonio", 22, "male", 70, 180)
ramires = SupportUser.SupportUser("ramires", 22, "male")
henrique = SupportUser.SupportUser("henrique", 22, "male")


userHandler.addUser(renato)
userHandler.addUser(jb)
userHandler.addUser(apc)
userHandler.addUser(mbc)
userHandler.addUser(antonio)
userHandler.addUser(ramires)
userHandler.addUser(henrique)


userHandler.listUsers()
userHandler.listUsersDetail("renato")
renato.initDialogue()
renato.initDialogue()
userHandler.listUsersDetail("ramires")

ramires.addSupporter(jb)
ramires.addSupporter(apc)
ramires.addSupporter(mbc)
ramires.showSupporter()


# Remover utilizador
userHandler.remove_user("antonio")
userHandler.listUsers()
