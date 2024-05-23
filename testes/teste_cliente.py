import unittest
from cliente.main import send_request

class TestCliente(unittest.TestCase):

    def test_soma(self):
        result = send_request("soma", [2, 3])
        self.assertEqual(result, 5)

    def test_fatorial(self):
        result = send_request("fatorial", [5])
        self.assertEqual(result, 120)

if __name__ == "__main__":
    unittest.main()