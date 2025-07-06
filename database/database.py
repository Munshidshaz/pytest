class Database:
    """Simulates a basic user database"""
    def __init__(self):
        self.data={} #Simulating an in-memory database

    def add_user(self,user_id,name):
        if user_id in self.data:
            raise ValueError ("User already exists")
        self.data[user_id]=name
    
    def get_user(self,user_id):
        if user_id in self.data:
            return self.data.get(user_id)
        else:
            raise ValueError("User not found")
    
    def delete_user(self,user_id):
        if user_id in self.data:
            del self.data[user_id]