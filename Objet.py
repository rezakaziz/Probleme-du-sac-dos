class Objet:
	def __init__(self,w,v):
		self.poid=w
		self.gain=v

	def __eq__(self, other):
		if (isinstance(other, Objet)):
			return self.poid == other.poid and self.gain == other.gain
		return false
	