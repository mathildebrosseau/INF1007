from game import *


def main():
	print("\nC'EST LA GUERRE!!!\n")
	c1 = Character("Méchant", 200, 150, 70, 70)
	c2 = Character("Grognon", 250, 100, 120, 60)

	c1.weapon = Weapon("batte de baseball", 100, 69)
	c2.weapon = Weapon("son âme plus noire que le charbon", 120, 1)

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")
	print("\nFIN DE LA GUERRE")


if __name__ == "__main__":
	main()
