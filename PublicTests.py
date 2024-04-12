import unittest
from cmsc389OHW8.solution import isValid

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):
        self.assertEqual(False, isValid(["<p>","<div>", "<h>", "</div>","</p>"]))

    def test2(self):
        self.assertEqual(True , isValid(["<p>", "<h>","<div>",  "</div>", "</h>", "</p>"]))

    def test3(self):
        self.assertEqual(False,isValid(["<p>"]))

    def test4(self):
        self.assertEqual(True , isValid(["<div>",  "</div>","<div>","</div>","<div>",  "</div>",]))
    def test5(self):
        self.assertEqual(True, isValid(["<p>", "</p>"]))
  

    

if __name__ == "__main__":
    unittest.main()


