import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        with open(self.filename, "r") as file:
            for line in file:
                email, password, name, created = line.strip().split(";")
                self.users[email] = (password, name, created)

    def get_user(self, email):
        return self.users.get(email, -1)

    def add_user(self, email, password, name):
        email = email.strip()
        if email not in self.users:
            self.users[email] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        user = self.get_user(email)
        if user != -1:
            return user[0] == password
        return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(f"{user};{self.users[user][0]};{self.users[user][1]};{self.users[user][2]}\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

# Example usage
if __name__ == '__main__':
    db = DataBase("users.txt")
    db.add_user("test@example.com", "password123", "Test User")
    print(db.validate("test@example.com", "password123"))
