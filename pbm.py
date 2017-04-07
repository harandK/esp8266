import math
 
class PBM_P1:
   
    width = None
    height = None
    size_already_seen = False
    pixels =[]
   
    INT = 32
   
    counter = 0
   
    def __init__(self,filename):
        f = open(filename,"r")
       
        self.__parse(f)
    def __parse(self,f):
       
        
        
        for line in f:
           
            if line[0] =='#': continue
           
            if line[0] == 'P': 
                if line[0:2] != "P1":
                    raise ValueError("unsupported pbm type")
                continue
           
            print (line)
            if len(line.split() ) == 2 and not self.size_already_seen:
                self.width,self.height = map(int,line.split())
                self.pixels = [0]* int(math.ceil(self.width*self.height / self.INT))
                self.size_already_seen = True
                continue
           
 
            for s in line.replace("\n", "").replace(" ", ""):
                
                if s == "1":
                    self.pixels[self.counter // self.INT]  <<= 1
                    self.pixels[self.counter // self.INT]  |= 1                
                else:
                    self.pixels[self.counter // self.INT]  <<= 1
           
                self.counter +=1
                
                
                
    def get(self,row,col):
        rest = (row*self.width+col)%self.INT

        result = self.pixels[(row*self.width+col)//self.INT] & (1 << (self.INT-1 -rest))
        if result:
            return 1
        else:
            return 0
        