

def mandlebrot(x,y):
  
    n = 0
    oldx = x
    oldy = y
    
    while n < 9:
        a = x * x - y *y
        b = 2 * x * y
        x = a + oldx
        y = b + oldy


        if (x*x) + (y*y) > 9:
            return n
            
        n = n + 1
    return n
  
  

y = -1.2


while (y < 1.2):
    y = y + 0.03
    x = -2.1
    line = ""
    

    while (x < 1.1):
        x = x + 0.0125
        
        
        m = mandlebrot(x,y)
        if (m == 9):
            m = " "

        line = line + str(m)
    
    print(line)