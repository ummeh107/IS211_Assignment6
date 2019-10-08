def convert(fromUnit, toUnit, value):
    try:
            # miles to yards
        if str(fromUnit).lower() == 'miles' and str(toUnit).lower() == 'yards':
            return   value * 1760
        # miles to meters
        elif str(fromUnit).lower() == 'miles' and str(toUnit).lower() == 'meters':
            return   value * 1609.344
        #  yards to miles
        elif str(fromUnit).lower() == 'yards' and str(toUnit).lower() == 'miles':
            return   value * 0.0005681
        # yards to meters
        elif str(fromUnit).lower() == 'yards' and str(toUnit).lower() == 'meters':
            return   value * 0.9144
        # meters to miles
        elif str(fromUnit).lower() == 'meters' and str(toUnit).lower() == 'miles':
            return   value * 0.000621
        # meters to yards
        elif str(fromUnit).lower() == 'meters' and str(toUnit).lower() == 'yards':
            return   value * 1.09361
        elif str(fromUnit).lower() == fromUnit.lower() and toUnit.lower() == toUnit.lower():
            return value 
        else:
            raise ConversionNotPossible("Conversion Not Possible") 
    except ConversionNotPossible as error:
        print(error.message)
        return error.message




class ConversionNotPossible(Exception):
    def __init__(self, message):
        self.message = message 
    def __str__(self):
        return str(self.message) 