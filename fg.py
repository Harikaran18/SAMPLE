'''
class vector:
    def __init__(self,x,y,z):
        self.xcord=x
        self.ycord=y
        self.zcord=z
      
    def __add__(self,other):
        a=self.xcord +other.xcord
        b=self.ycord +other.ycord
        c=self.zcord +other.zcord
        return vector(a,b,c)
    def __sub__(self,other):
        a=self.xcord -other.xcord
        b=self.ycord -other.ycord
        c=self.zcord -other.zcord
        return vector(a,b,c)
    
    def __mul__(self,other):
        a=self.xcord *other.xcord
        b=self.ycord *other.ycord
        c=self.zcord *other.zcord
        return vector(a,b,c)
    
    def __str__(self):
        return ('('+str(self.xcord)+')i+('+str(self.ycord)+')j+('+str(self.zcord)+')k')



v1=vector(1,10,5)
v2=vector(2,7,6)
print("The sum of the 2 vectors is : ",v1+v2)
print("The difference of the 2 vectors is : ",v1-v2)
print("The dot product of the 2 vectors is : ",v1*v2)        
'''
class Matrix:
    def __init__(self,r,c,l=[]):
        self.rows=r
        self.columns=c
        self.l=l
    def mat(self):
        self.l=[]
        for i in range(1,self.rows+1):
            R=[]
            for j in range(1,self.columns+1):
                ip=input("enter the value of a{}{}:".format(i,j))
                if ip=='':
                    
                    R.append(0)
                else:
                    R.append(int(ip)) 
            self.l.append(R)
    
        
    def __list__(self):
        return self.l

    def __add__(self,other):
         
        if self.rows==other.rows and self.columns==other.columns:
           
            m3=Matrix(self.rows,other.columns)
            m3.l=[]
            for i in range(self.rows):
                
                R=[]
                for j in range(self.columns):
                    R.append(self.l[i][j]+other.l[i][j])
                m3.l.append(R)            
                
        else:
            print("unequal matrices are given")
        return m3.l

    def __sub__(self,other):
        
        if self.rows==other.rows and self.columns==other.columns:
            
            m3=Matrix(self.rows,other.columns)
            m3.l=[]
            for i in range(self.rows):
                
                R=[]
                for j in range(self.columns):
                    R.append(self.l[i][j]-other.l[i][j])
                m3.l.append(R)

        else:
            print("unequal matrices are given")
        return m3.l                

    

m1=Matrix(3,3)
m1.mat()
print("The matrix is: ",m1.l)

m2=Matrix(3,3)
m2.mat()
print("The Matrix is: ",m2.l)
print()
print("The sum of the matrices is: ",m1+m2)
print("The subtraction of the matrices is: ",m1-m2)






                






        
