import concurrent.futures
import traceback
import time
import sys

"""
Wrapper for conncurent.futures
Allows to create threads or processes for:
1)  Funtions call:
    def thread(function, inputs, *args, **kwargs)
    def process(function, inputs, *args, **kwargs)
    inputs:
        function:   function object
        inputs:     any iterator that will be passed as first argument to function call
        *args:      positional args that will be passed to function call
        **kwargs:   keyword args that will be passed to function call
    outputs:
        output:     list with result of functions execution
        
2)  Objects method call
    def othread(method, objects, *args, **kwargs)
    def oprocess(method, objects, *args, **kwargs)
    inputs:
        method:     method name
        objects:    any iterator with objects
        *args:      positional args that will be passed to method call
        **kwargs:   keyword args that will be passed to method call
    outputs:
        output:     list with result of methods execution
"""

def __catch_results(fs):
    output = []
    for f in concurrent.futures.as_completed(fs):
        try:
            result = f.result()
            output.append(result)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            output.append(None)

    return output

def thread(function, inputs, *args, **kwargs):
    output = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=48) as executor:

        fs = []
        for input in inputs:
            fs.append(executor.submit(function, input, *args, **kwargs))

        return __catch_results(fs)


def process(function, inputs, *args, **kwargs):
    output = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=48) as executor:

        fs = []
        for input in inputs:
            fs.append(executor.submit(function, input, *args, **kwargs))

        return __catch_results(fs)
        


def othread(method, objects, *args, **kwargs):
    output = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=48) as executor:

        fs = []
        for obj in objects:
            fs.append(executor.submit(getattr(obj, method), *args, **kwargs))

        return __catch_results(fs)


def oprocess(method, objects, *args, **kwargs):
    output = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=48) as executor:

        fs = []
        for obj in objects:
            fs.append(executor.submit(getattr(obj, method), *args, **kwargs))

        return __catch_results(fs)
