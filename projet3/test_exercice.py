import unittest
import exercice as ex


ex.proprietes_eau(14.3)


class TestExercice(unittest.TestCase):

    def test_proprietes_eau(self):
        # Comparer les résultats de la fonction avec les résultats attendus présentés dans le README
        self.assertEqual(ex.proprietes_eau(14.3), (999.184, 0.0011638))

        # Comparer les résultats de la fonction avec des valeurs fournies dans le fichier data.csv
        self.assertEqual(ex.proprietes_eau(30), (995.7, 0.80e-3))
        self.assertEqual(ex.proprietes_eau(10), (999.7, 1.31e-3))

        # Comparer les résultats de la fonction lorsqu'on lui passe une valeur très près d'un des valeurs
        #   fournies dans le fichier data.csv
        self.assertEqual((round(ex.proprietes_eau(0.001)[0], 1), round(ex.proprietes_eau(0.001)[1], 5)),
                         ex.proprietes_eau(0))

    def test_regime_stockes(self):
        rp = 2000
        dp = 1.0e-3
        t = 14.3
        reau, meau = ex.proprietes_eau(t)

        # Comparer les résultats de la fonction avec les résultats attendus présentés à la fin du README
        self.assertEqual(round(ex.regime_stockes(dp, rp, reau, meau)[0], 3), 0.469)
        self.assertEqual(round(ex.regime_stockes(dp, rp, reau, meau)[1], 3), 0.060)
        self.assertEqual(round(ex.regime_stockes(dp, rp, reau, meau)[2], 3), 402.245)

        # Vérifier qu'il n'y a pas de division par 0 (si mu_eau = 0 ou diamètre_particule = 0)
        self.assertRaises(ZeroDivisionError, ex.regime_stockes, dp, rp, reau, 0)
        self.assertRaises(ZeroDivisionError, ex.regime_stockes, 0, rp, reau, meau)

    def test_regime_intermediaire(self):
        rp = 2000
        dp = 1.0e-3
        t = 14.3
        reau, meau = ex.proprietes_eau(t)
        rep = ex.regime_stockes(dp, rp, reau, meau)[2]

        # Comparer les résultats de la fonction avec les résultats attendus présentés à la fin du README
        self.assertEqual(round(ex.regime_intermediaire(ex.regime_stockes(dp, rp, reau, meau)[2],
                                                       dp, rp, reau, meau)[0], 3), 0.146)
        self.assertEqual(round(ex.regime_intermediaire(ex.regime_stockes(dp, rp, reau, meau)[2],
                                                       dp, rp, reau, meau)[1], 3), 0.616)
        self.assertEqual(round(ex.regime_intermediaire(ex.regime_stockes(dp, rp, reau, meau)[2],
                                                       dp, rp, reau, meau)[2], 3), 125.232)

        # Vérifier qu'il n'y a pas de division par 0 (si mu_eau = 0 ou diamètre_particule = 0)
        self.assertRaises(ZeroDivisionError, ex.regime_intermediaire, 0, dp, rp, reau, meau)
        self.assertRaises(ZeroDivisionError, ex.regime_intermediaire, rep, dp, 600, 0, meau)

        # Vérifier qu'on ne calcule pas la racine carrée d'un nombre négatif (si rho_eau négatif ou
        #   si rho_eau > rho_particule)
        self.assertRaises(ValueError, ex.regime_intermediaire, rep, dp, rp, -999, meau)
        self.assertRaises(ValueError, ex.regime_intermediaire, rep, dp, rp, 2050, meau)

    def test_calcule_vitesse(self):
        rp = 2000
        dp = 1.0e-3
        t = 14.3
        reau, meau = ex.proprietes_eau(t)

        # Comparer les résultats de la fonction avec les résultats attendus selon la fin du README
        self.assertEqual(ex.calcule_vitesse(rp, dp, t), 0.10813081995597007)

        # Tester si la fonction retourne bien la vitesse calculée dans le régime de Stockes lorsque Rep <= 0.3
        self.assertEqual(ex.calcule_vitesse(rp, 5.0e-5, t), ex.regime_stockes(5.0e-5, rp, reau, meau)[0])

        # Tester si la fonction retourne None lorsque Rep > 1000
        self.assertIsNone(ex.calcule_vitesse(rp, 4.2e-3, t))


if __name__ == '__main__':
    unittest.main()
