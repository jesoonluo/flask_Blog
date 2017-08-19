from flask.ext.sqlalchemy import SQLAlchemy

#collection mysql
mysql://root:mysql@localhost:3306/test

class User(db.Model):

	__tablename__ = 'user_table_name'

	id = db.Column(db.Interger(),primary_key=Ture)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))
	
	def __init__(self,username):
		self.username = username
	
	def __repr__(self):
		return "<User '{}'>".format(self.username)
def main():
	app = Flask(__name__)
	app.config.from_object(DevConfig)
	db = SQLAlchemy(app)
	



if __name__=="__main__":
	main()
