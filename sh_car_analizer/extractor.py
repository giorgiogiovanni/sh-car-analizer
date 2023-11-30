from datetime import datetime


class InterfazExtractor():
	""" 
	Interfaz básica de los datos a extraer 
	y métodos comunes para extraer los datos
	"""
	_precio: float = 0.0
	_last_updated: datetime = None

	def __init__(self):
		self.get_data()

	def get_data():
		pass
