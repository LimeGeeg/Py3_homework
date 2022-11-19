class Element:
	def __init__(self, t_melt, t_boil):
		self.t_melt = t_melt
		self.t_boil = t_boil

	def agg_state(self, temp, scale = "C"):
		temp = self.convert_temp(temp, scale)
		if temp < self.t_melt:
			return "Твердый"

		if temp > self.t_boil:
			return "Пар"

		return "Жидкость"

	def convert_temp(self, temp, scale = "C"):
		if scale == "K":
			return temp - 273
		if scale == "F":
			return (temp - 32) * 5 / 9
		return temp

water = Element(0, 100)
print(water.convert_temp(150))
print(water.agg_state(150))
input()