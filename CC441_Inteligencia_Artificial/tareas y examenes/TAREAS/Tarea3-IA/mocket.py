class MockObject:
    def __init__(self):
        self.users = {}
    
    def addUser(self, user):
        print("Añadiendo..")
        print("ID: {}  USER: {}".format(user.getId(), user.getName()))
        self.users[user.getId()] = user
        print("Done!")

    def getUser(self, id):
        print("Obteniendo usuario..")
        user = self.users[id]
        print("ID: {}  USER: {}".format(user.getId(), user.getName()))
        print("Done!")

    def removeUser(self, id):
        print("Removiendo usuario..")
        user = self.users[id]
        print("ID: {}  USER: {}".format(user.getId(), user.getName()))
        del self.users[id]
        print("Done!")
    
    def showUsers(self):
        print("Imprimiendo usuarios actuales..")
        values = list(self.users.values())
        for i in range(len(self.users)):
            print("USER: {}".format(values[i].getName()))

class User:
    def __init__(self, id, name, mail, gender, age):
        self.id = id
        self.name = name
        self.mail = mail
        self.gender = gender
        self.age = age
    def getName(self):
        return self.name
    
    def setName(new_name):
        self.name = new_name
    
    def getId(self):
        return self.id
    
    def setId(new_id):
        self.id = new_id

if __name__  == '__main__':
    user1 = User(id = '0806', name = 'Wiki', mail = 'csanchezs@uni.pe',
                gender = 'male', age = 22)

    user2 = User(id = '0807', name = 'cesar', mail = 'cs@uni.pe',
                gender = 'male', age = 22)
    
    user3 = User(id = '0808', name = 'jhon', mail = 'cj@uni.pe',
                gender = 'male', age = 22)

    mock = MockObject()
    mock.addUser(user1)
    mock.addUser(user2)
    mock.addUser(user3)

    mock.getUser(user1.getId())
    mock.removeUser(user2.getId())
    mock.showUsers()
    