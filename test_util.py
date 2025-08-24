import unittest
import utils

class Testutils(unittest.TestCase):
    def test_utils1(self):
        self.assertEqual(utils.To_lowercase("two"),"two")
      
    def test_utils2(self):
       
        self.assertEqual(utils.To_lowercase("THREE"),"three")
    def test_utils3(self):
        
        self.assertEqual(utils.To_lowercase("fOur"),"four")
       


       

