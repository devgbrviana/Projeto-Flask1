import unittest
import requests


class TestCrudAluno(unittest.TestCase):

    def setUp(self):
      
        requests.post('http://localhost:5000/reseta')
