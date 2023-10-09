class Base:
     def __init__(self, x,y,size):
         self.x = x
         self.y = y
         self.size = size
class Square(Base):
        def __init__(self,x,y):
            super().__init__(x,y)
            
        def shape(self):
            return f"This is a square"
        
        def draw(self):
            return f""" ({self.x}, {self.y})
        __________________________
        |                        |
        |                        |
        |                        |
        |                        |
        |                        |
        |                        |
        |                        |
        |________________________|
        
        """
class Circle(Base):
    def __init__(self,x,y,size):
        super().__init__(x,y,size)
        
    def shape(self):
        print("This is a circle")
        
        
    def draw(self):
        return f""" ({self.x}, {self.y}) 

        
          , - ~ ~ ~ - ,
     , '                  ' ,
    ,                         ,
   ,                          ,
   ,                           ,
   ,                           ,
   ,                           ,
   ,                           ,
    ,                        ,
      ,                   , '
        '  - , _ _ _ , '
"""
    
def main():
    s = Circle(1,2,3)
    print(s.shape())
    print(s.draw())

main()
#     sq = Square(2,1,3)
#     sq.shape()
#     print(sq.draw())
# main()