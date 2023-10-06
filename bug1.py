class Base:
     def __init__(self, x,y,size):
         self.x = x
         self.y = y
         self.size = size
class Circle(Base):
    def __init__(self,x,size):
        super().__init__(x,x,size)
        
    def shape(self):
        print("This is a circle")
        
        
    def draw(self):
        return f""" ({self.x}, {self.y}) 
        {self.size}
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
    s = Circle(2,1)
    s.shape()
    print(s.draw())
main()