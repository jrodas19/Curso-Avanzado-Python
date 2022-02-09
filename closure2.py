def make_division_by(K):
    def divisor(n):
         assert type(n) == int, 'Just introduce integer'
         return n/K
   
    return divisor


def run():
    divisionby5 = make_division_by(5)
    print(divisionby5(100))
    
if __name__ == '__main__':
    run()