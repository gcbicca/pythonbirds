from unittest import TestCase

from oo.carro import Motor


class CarroTestCase(TestCase):
    """Metodos assert herdados da classe TestCase"""
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(1, motor.velocidade)  # O valor esperado e o valor que recebo

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)