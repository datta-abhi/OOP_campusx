class Fraction:
    # create parameterized constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y
        
    def __str__(self):
        # magic method which returns how to display object of this class
        return f"{self.num}/{self.den}"
    
    def __add__(self,other):
        add_num = (self.num*other.den + self.den*other.num)
        add_den = (self.den)*(other.den)
        
        return f"{add_num}/{add_den}"
    
    def __mul__(self,other):
        mul_num = (self.num*other.num)
        mul_den = (self.den*other.den)
        
        return f"{mul_num}/{mul_den}"