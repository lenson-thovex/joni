class Auto:

	def __init__(self, color, weight):
		self.color = color
		self.weight = weight

car = Auto('green', 1500)

print(f'Das Auto hat die Farbe: {car.color}')
print(f'Das Auto wiegt: {car.weight}')
