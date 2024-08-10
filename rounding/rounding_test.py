import rounding

known_values=[(123.5, 0, '124', {}),
(-123.5, 0, '-124', {}),
(17.456, 1, '17.5', {}),
(-17.456, 1, '-17.5', {}),
(123, 2, '123.00', {}),
(-123, 2, '-123.00', {}),
('123.', 0, '123', {}),
('-123.', 0, '-123', {}),
(1234567, 0, '1 234 567', {'separate_thousands':True}),
(1234567, 2, '1 234 567.00', {'separate_thousands':True}),
(123, 1, '123.0', {'separate_thousands':True}),
(-123, 1, '-123.0', {'separate_thousands':True}),
('1.234.567,555', 2, '1.234.567,56', {'separate_thousands':True, 'thousands_separator':'.', 'decimal_separator':','}),
]
for x, y, z, kwargs in known_values:
	print(x, y, rounding.rd(x, y, kwargs=kwargs))
	assert rounding.rd(x, y, kwargs=kwargs) == z, f'{x} roundet to {y} is {(rounding.rd(x, y, kwargs=kwargs))} expecting {z}'