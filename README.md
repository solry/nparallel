# nparallel
Easy-to-use concurrent.futures wrapper

Allows to create parallel threads or processes for:
1)  **Funtions call**:

    def thread(function, inputs, *args, **kwargs)
    
    def process(function, inputs, *args, **kwargs)
    
    inputs:
    
        function:   function object    
        inputs:     any iterator that will be passed as first argument to function call
        *args:      positional args that will be passed to function call
        **kwargs:   keyword args that will be passed to function call
        
    outputs:
    
        output:     list with result of functions execution
        
2)  Objects **method call**:

    def othread(method, objects, *args, **kwargs)
    
    def oprocess(method, objects, *args, **kwargs)
    
    inputs:
    
        method:     method name
        objects:    any iterator with objects
        *args:      positional args that will be passed to method call
        **kwargs:   keyword args that will be passed to method call
        
    outputs:
    
        output:     list with result of methods execution


**Example**:
    
    
        import nparallel
        
        def some_func(pos_arg, keyword_arg):
            return pos_arg, keyword_arg
            
        list_of_args = ['1','2','3']
        
        nparallel.thread(some_func, list_of_args, keyword_arg='this is kwarg')
 
        Out[7]: [('3', 'this is kwarg'), ('1', 'this is kwarg'), ('2', 'this is kwarg')]
