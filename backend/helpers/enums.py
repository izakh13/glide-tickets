from enum import Enum

class TicketTypes(Enum):
    CHOOSE_VALUE = ('choose_value', '--Choose a value--')
    ADULT = ('adult', 'Adult')
    CHILDREN = ('children', 'Children')


    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj

    def __str__(self):
        return f'("{self.value}", "{self.description}")'
    

    @staticmethod
    def get_all():
        res = []
        for value in TicketTypes.__members__.values():
            res.append(eval(str(value)))
        return tuple(res)

class MeansOfTransport(Enum):
    CHOOSE_VALUE = ('choose_value', '--Choose a value--')
    AIRPLANE = ('airplane', 'Airplane')
    COACH = ('coach', 'Coach')
    TRAIN = ('train', 'Train')

    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj

    def __str__(self):
        return f'("{self.value}", "{self.description}")'
    
    @staticmethod
    def get_all():
        res = []
        for value in MeansOfTransport.__members__.values():
            res.append(eval(str(value)))
        return tuple(res)