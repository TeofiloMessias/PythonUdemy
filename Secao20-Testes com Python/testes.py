import unittest

from atividades import comer, dormir, eh_engracada

class AtividadeTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudavel."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
       )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente so vive uma vez.'
        )
    def test_dormindo_pouco(self):
        """Testando o retorno dormindo pouco."""
        self.assertEqual(
            dormir(4),
            'Cintinuo cansado após dormir 4 horas. :('
        )
    def test_dormir_muito(self):
        """Testando o retorno dormindo muito."""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho'
        )

    def test_eh_egracada(self):
        #self.assertEqual(eh_engracada('Sérgio Malandro'), False)
        self.assertFalse(eh_engracada('Ségio Malandro'))
        self.assertTrue(eh_engracada('Jim Carry'), 'Jim Carry deveria se engraçado')



if __name__ == '__main__':
   unittest.main()
