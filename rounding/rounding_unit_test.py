import rounding
import unittest

class KnownValues(unittest.TestCase):
    known_values_basic=[
        (123.5, 0, '124', {}),
        (-123.5, 0, '-124', {}),
        (17.456, 1, '17,5', {}),
        (-17.456, 1, '-17,5', {}),
        (123, 2, '123,00', {}),
        (-123, 2, '-123,00', {}),
        ('123.', 0, '123', {}),
        ('-123.', 0, '-123', {}),
        ('-999', -2, '-1000', {'thousands_separator':{'':''}}),
        ('999', -3, '1000', {'thousands_separator':{'':''}}),
        ]
    known_values_negative_decimal=[
        ('811', -1, '810', {}),
        ('811', -2, '800', {}),
        ('811', -3, '1000', {'thousands_separator':{'':''}}),
        ('811', -4, '0', {}),
        ('999', -1, '1000', {'thousands_separator':{'':''}}),
        ('999', -2, '1000', {'thousands_separator':{'':''}}),
        ('999', -3, '1000', {'thousands_separator':{'':''}}),
        ('-999', -1, '-1000', {'thousands_separator':{'':''}}),
        ('-999', -2, '-1000', {'thousands_separator':{'':''}}),
        ('-999', -3, '-1000', {'thousands_separator':{'':''}}),
        ('-999', -4, '0', {}),
        ]
    known_values_thousands=[
        (1234567, 0, '1 234 567', {'thousands_separator':{'':' '}}),
        (1234567, 2, '1 234 567,00', {'thousands_separator':{'':' '}}),
        (123, 1, '123,0', {'thousands_separator':{'':' '}}),
        (-123, 1, '-123,0', {'thousands_separator':{'':' '}}),
('1.234.567,555', 2, '1.234.567,56', {'thousands_separator':{'.':'.'}, 'decimal_separator':{',':','}}),
        (-11125, -1, '-11 130', {'thousands_separator':{'':' '}})
        ]
    known_values_specks=[
        ('.1', 0, '0', {}),
        ('-.1', 0, '0', {}),
        ]
    unknown_key = 'ahoj'

    #musi zacinat test
    def test_rounding_known_values_basic(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_basic:
            result = rounding.rd(x, y, **kwargs)
            self.assertEqual(z, result)
    
    def test_rounding_known_values_negative_decimals(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_negative_decimal:
            result = rounding.rd(x, y, **kwargs)
            self.assertEqual(z, result)
            
    def test_rounding_known_values_thousands(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_thousands:
            result = rounding.rd(x, y, **kwargs)
            self.assertEqual(z, result)

    def test_rounding_known_values_specks(self):
        '''rounding.rd(num, dec, kwargs) should give known result with known input'''
        for x, y, z, kwargs in self.known_values_specks:
            result = rounding.rd(x, y, **kwargs)
            self.assertEqual(z, result)
    
    def test_rounding_unknown_key_exception_text(self):
        '''rounding.rd(num, dec, kwargs) should raise Error with unknown key'''
        with self.assertRaises(Exception) as context:
            rounding.rd(123, 2, **{self.unknown_key: 0})
        self.assertTrue(f"rd() got an unexpected keyword argument '{self.unknown_key}'" in str(context.exception),
		f"rd() got an unexpected keyword argument '{self.unknown_key}'" + " != " + str(context.exception))

    def test_rounding_unknown_key_exception_type(self):
        '''rounding.rd(num, dec, kwargs) should raise TypeError with unknown key'''
        with self.assertRaises(TypeError):
            rounding.rd(123, 2, **{self.unknown_key: 0})


#if __name__ == '__main__':
#    unittest.main()
    
unittest.main(argv=[''], verbosity=2, exit=False)
