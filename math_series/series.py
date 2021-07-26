def fibonacci(dict):
    sol={}
    for key in dict:
            sol[key]= fibonacciassest(key)       
    return sol
           
def fibonacciassest(n):
        if n==1:
            return  1

        if n==0:

            return  0
        else:
            return fibonacciassest(n-1)+fibonacciassest(n-2)

def lucas(dict):
        sol={}
        for key in dict:
            sol[key]= lucas_assest(key)       
        return sol

def lucas_assest(n):
        if n==1:
            return  1

        if n==0:

            return  2
        else:
            return lucas_assest(n-1)+lucas_assest(n-2)

  

def sum_series(dict):
        sol={}
        for key in dict:
            sol[key]= sum_series_assest(key,dict[0],dict[1])       
        return sol



def sum_series_assest(num,first =3, second =4):
        if num==1:
            return  second

        if num==0:

            return  first
        else:
            return sum_series_assest(num-1,first,second)+sum_series_assest(num-2,first,second)




