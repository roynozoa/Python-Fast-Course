# Intermediate Programming in python
# Optimize python programming time with multiprocessing
# Multiprocessing can help to speed up CPU bound process
# Code reference by Corey Schafer : https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/MultiProcessing

# import library
import time
import concurrent.futures

# define do_sleeping function


def do_sleeping(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)  # this line will delay execution time for n seconds
    return f'Done sleeping for {seconds} second(s).....'


if __name__ == '__main__':
    print("=====================================================================")
    print("Example 1 implementing multiprocessing with ")
    print("process pool executor")
    print("=====================================================================")
    start = time.perf_counter()  # start performance counter

    # create a process pool executor
    with concurrent.futures.ProcessPoolExecutor() as executor:

        # list of seconds that use for multiprocessing
        seconds = [5, 4, 3, 2, 1]
        # create a future object with do_sleeping function with list comprehension loop
        results = [executor.submit(do_sleeping, sec) for sec in seconds]

        # my system uses 4 core so it's only able to do 4 process at the same time
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()  # finish performance counter

    # counting duration with round from start to finish
    duration = round(finish - start, 2)

    # printing the duration
    print(f'Code finished in {duration} second(s)\n\n')

    print("=====================================================================")
    print("Example 3 implementing thread with")
    print("process pool executor (mapping)")
    print("=====================================================================")

    start = time.perf_counter()  # start performance counter

    with concurrent.futures.ProcessPoolExecutor() as executor:

        # list of seconds that use for processing
        seconds = [5, 4, 3, 2, 1]
        # create a future object with mapping
        results = executor.map(do_sleeping, seconds)

        for result in results:
            print(result)

    finish = time.perf_counter()  # finish performance counter

    # counting duration with round from start to finish
    duration = round(finish - start, 2)

    # printing the duration
    print(f'Code finished in {duration} second(s)\n\n')
