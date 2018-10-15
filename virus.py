class Virus(object):
	"""Properties and attributes of the virus used in Simulation """
	def __init_(self, name, mortality_rate, repro_rate):
		self.name = name
		self.mortality_rate = mortality_rate
		self.repro_rate = repro_rate


	def test_virus_instantiation():
		"""Check to make sure that the virus instantiator is working."""
		virus = Virus("HIV", 0.8, 0.3)
		assert virus.name == "HIV"
		assert virus.mortality_rate == 0.8
		assert virus.repro_rate == 0.3