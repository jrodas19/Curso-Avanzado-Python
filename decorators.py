from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elpased = final_time - initial_time
        print('Time to run function: '+ str(time_elpased.total_seconds()) + ' seconds')
    
    return wrapper
 
@execution_time       
def randon_fun():
    for _ in range(1,100000):
        pass
    
# randon_fun()


@execution_time
def suma(a: int, b: int) -> int:
    return a + b

suma(8,9)