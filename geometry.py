### Write OOP classes to handle the following scenarios:

# - A user can create and view 2D coordinates
# - A user can find out the distance between 2 coordinates
# - A user can find find the distance of a coordinate from origin
# - A user can check if a point lies on a given line
# - A user can find the distance between a given 2D point and a given line

class Point:
    
    def __init__(self,x,y) -> None:
        self.xcord = x
        self.ycord = y
    
    def __str__(self) -> str:
        return f"<{self.xcord},{self.ycord}>"
    
    def dist_bw_points(self,other):
        x1 = self.xcord
        y1 = self.ycord
        
        x2 = other.xcord
        y2 = other.ycord
        
        dist = round(((x1-x2)**2 + (y1-y2)**2)**0.5,3)
        return dist
    
    def dist_from_origin(self):
        x1 = self.xcord
        y1 = self.ycord
        
        dist = round((x1**2 + y1**2)**0.5,3)
        return dist

class Line:
    # Line class is defined by Ax+By+C = 0
    def __init__(self,a,b,c) -> None:
        self.A = a
        self.B = b
        self.C = c
    
    def __str__(self) -> str:
        return f"{self.A}x + {self.B}y + {self.C}"
    
    def point_on_line(self,point):
        
        if self.A*(point.xcord) + self.B*(point.ycord)+ self.C == 0:
            return True
        else:
            return False
    
    def shortest_distance(self,point):
        num = abs(self.A*point.xcord + self.B*point.ycord + self.C)
        den = (self.A**2 + self.B**2)**0.5
        
        dist = num/den
        return dist    
        