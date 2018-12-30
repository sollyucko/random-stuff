import unittest
from dataclasses import field

from webify_v2.db.types.password import Password
from webify_v2.db import Table


class PasswordTest(unittest.TestCase):
    def setUp(self):
        class TestTable(Table):
            password: Password = field(metadata={'hasher_name': 'blake2b512'})
        
        self.TestTable = TestTable
    
    def test_correct_password(self):
        row = self.TestTable('correct horse battery staple')
        self.assertEqual(row.password, 'correct horse battery staple')
    
    def test_incorrect_password(self):
        row = self.TestTable('Tr0ub4dor&3')
        self.assertNotEqual(row.password, 'correct horse battery staple')


if __name__ == '__main__':
    unittest.main()
