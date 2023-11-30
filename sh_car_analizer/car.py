from extractor import InterfazExtractor


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
	_extractors: List[InterfazExtractor] = []
	
	def __init__(self, marca, modelo):
		""" Se cargan los datos básicos para luego extraer 
		la información común desde algún extractor de datos """
		super(Model, self).__init__()
		self._marca = marca
		self._modelo = modelo




