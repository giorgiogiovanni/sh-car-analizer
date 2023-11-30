

class Modelo(object):
	"""Representa los datos básicos de un coche"""
	_marca: str = ''
	_modelo: str = ''
	_combustible: str = ''
	_año: int = 1900
	_cv: int = 0
	_kms: int = 0
	_puertas: int = 0
	_cambio_marchas: str = ''
	_color: str = ''
	_precio: float = 0.0
	
	def __init__(self, arg):
		super(Model, self).__init__()
		self.arg = arg




