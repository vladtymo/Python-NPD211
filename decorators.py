def withTitle(input_func):    
    def output_func():    
        # code before invocation 
        print("----- Title -----")
        input_func()            
        # code after invocation   
        print("----- ----- -----")
    return output_func   
 
@withTitle
def test():
    print("Hello Vlad!")

test()