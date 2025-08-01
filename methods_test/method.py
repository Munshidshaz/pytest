class UserManager:
    def __init__(self):
        self.users={}
    
    def add_user(self,username,email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username]=email
        return True
    
    def get_user(self,username):
        if username in self.users:
            return self.users.get(username)
        else :
            raise ValueError ("User not found")


 