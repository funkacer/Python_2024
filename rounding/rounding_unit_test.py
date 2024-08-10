import rounding
import unittest

class KnownValues(unittest.TestCase):
    known_values_basic=[
        (123.5, 0, '124', {}),
        (-123.5, 0, '-124', {}),
        (17.456, 1, '17.5', {}),
        (-17.456, 1, '-17.5', {}),
        (123, 2, '123.00', {}),
        (-123, 2, '-123.00', {}),
        ('123.', 0, '123', {}),
        ('-123.', 0, '-123', {})
        ]
    known_values_thousands=[
        (1234567, 0, '1 234 567', {'separate_thousands':True}),
        (1234567, 2, '1 234 567.00', {'separate_thousands':True}),
        (123, 1, '123.0', {'separate_thousands':True}),
        (-123, 1, '-123.0', {'separate_thousands':True}),
        ('1.234.567,555', 2, '1.234.567,56', {'separate_thousands':True, 'thousands_separator':'.', 'decimal_separator':','}),
        ]
    unknown_key = 'ahoj'

    #musi zacinat test
    def test_rounding_known_values_basic(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_basic:
            result = rounding.rd(x, y, kwargs=kwargs)
            self.assertEqual(z, result)
            
    def test_rounding_known_values_thousands(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_thousands:
            result = rounding.rd(x, y, kwargs=kwargs)
            self.assertEqual(z, result)
    
    def test_rounding_unknown_key(self):
        '''rounding.rd(num, dec, kwargs) should raise Error with unknown key'''
        with self.assertRaises(Exception) as context:
            rounding.rd(123, 2, kwargs={self.unknown_key: 0})
        self.assertTrue(f"Key argument '{self.unknown_key}' not accepted!" in str(context.exception),
		f"Key argument '{self.unknown_key}' not accepted!" + " != " + str(context.exception))

#if __name__ == '__main__':
#    unittest.main()
    
unittest.main(argv=[''], verbosity=2, exit=False)