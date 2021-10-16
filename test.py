import unittest
import os, ast
from main import User

class TestUser(unittest.TestCase):
    def load_data(self):
        root_dir = os.getcwd()
        data_dir = os.path.join(root_dir, "list_sample_bad.txt")
        file = open(data_dir, "r")
        contents = file.read()
        self.data = ast.literal_eval(contents)
        file.close()
    def test_main_data(self):
        self.load_data()
        self.assertTrue(isinstance(self.data, list),
                        "Expected apple to be a list")
    def test_null_key(self):
        self.load_data()
        cl = User(**self.data[1])
        
    def has_key(self):
        self.load_data()
        has_key = lambda d: all([isinstance(s, str) for i in d for s in i.keys()])
        self.assertTrue(has_key(self.data),
                        "Keys are not all strings")
if __name__ == '__main__':
    unittest.main()
