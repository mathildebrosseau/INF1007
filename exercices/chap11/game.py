"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20

	def __init__(self, name: str, power: int, min_level: int):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp

	@property
	def name(self):
		return self.__name

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, value):
		if value is None:
			value = Weapon.make_unarmed()
		if value.min_level > self.level:
			raise ValueError(Weapon)
		self.__weapon = value

	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, value):
		self.__hp = utils.clamp(value, 0, self.max_hp)

	def compute_damage(self, oponent):
		critical = random.random() <= 1/16
		modifier = (2 if critical else 1) * random.uniform(0.85, 1.0)
		level_factor = 2 * self.level / 5 + 2
		damage = modifier * (((level_factor * self.weapon.power * (self.attack / oponent.defense)) / 50) + 2)
		return int(round(damage)), critical


def deal_damage(attacker: Character, defender: Character):
	# TODO: Calculer dégâts
	damage, critical = attacker.compute_damage(defender)
	defender.hp -= damage
	print(f"{attacker.name} used {attacker.weapon.name}.")

	if critical:
		print("   Critical hit!")
	print(f"   {defender.name} took {damage} dmg")


def run_battle(c1: Character, c2: Character):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	defender = c2
	round_number = 1
	print(f"{attacker.name} starts a battle with {defender.name} !")

	while True:
		deal_damage(attacker, defender)
		if defender.hp == 0:
			print(f"{defender.name} s'est fait assassiner.")
			break
		round_number += 1
		attacker, defender = defender, attacker

	return round_number
