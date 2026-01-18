from degree import celsius_to_fahrenheit

def test_temp():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
