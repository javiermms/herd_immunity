import pytest
from person import Person 


def test_instance_functionality():
	person = Person(12, False, None)

	assert person._id == 12
	assert person.is_alive is True
	assert person.is_vaccinated is False
	assert person.infected is None

def test_did_survive_method():
	person_infected = Person(20, False, True)

	assert person_infected.did_survive_infection(12) is False
	assert person_infected.is_alive is False
	

	



	
