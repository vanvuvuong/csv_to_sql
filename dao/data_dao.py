

class Data(object):

	def __init__(self) -> None:
		pass

	def select(self, session, column, data, condition):
		pass

	def insert(self, session):
		session.add()
		session.commit()
	
	def update(self):
		pass

	def delete(self):
		pass
