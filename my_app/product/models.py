from my_app import db
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String)
    password = db.Column(db.String)
 
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
 
    def __repr__(self):
        return '<Product %d>' % self.id