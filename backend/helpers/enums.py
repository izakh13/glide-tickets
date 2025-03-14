from enum import Enum

class TupleEnum(Enum):
    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj

    def __str__(self):
        return f'("{self.value}", "{self.description}")'
    
    @classmethod
    def get_all(cls):
        res = []
        for value in cls.__members__.values():
            res.append(eval(str(value)))
        return tuple(res)

class TicketTypes(TupleEnum):
    CHOOSE_VALUE = ('choose_value', '--Choose a value--')
    ADULT = ('adult', 'Adult')
    CHILDREN = ('children', 'Children')


class MeansOfTransport(TupleEnum):
    CHOOSE_VALUE = ('choose_value', '--Choose a value--')
    AIRPLANE = ('airplane', 'Airplane')
    COACH = ('coach', 'Coach')
    TRAIN = ('train', 'Train')
