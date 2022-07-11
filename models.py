class WeightResult:
    def __init__(self):
        self.__current_weight = None
        self.__last_weight = None
    
    @property
    def current_weight(self):
        return self.__current_weight
    
    @current_weight.setter
    def current_weight(self, value):
        if value is None:
            raise Exception("There is no current weight")
        self.__current_weight = float("{:.3f}".format(value))

    @property
    def last_weight(self):
        return self.__last_weight
    
    @last_weight.setter
    def last_weight(self, value):
        if value is None:
            raise Exception("There is no last weight")
        self.__last_weight = float("{:.3f}".format(value))

    @property
    def difference(self):
        return float("{:.3f}".format(self.__current_weight - self.__last_weight))


