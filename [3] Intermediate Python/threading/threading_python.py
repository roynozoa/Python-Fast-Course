# Intermediate Programming in python
# Optimize python programming time with threading
# Threading can help to speed up I/O bound process
# Code reference by Corey Schafer : https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Threading

# import library
import time
import threading
import concurrent.futures


# define do_sleeping function
def do_sleeping(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)  # this line will delay execution time for n seconds
    return f'Done sleeping for {seconds} second(s).....'


print("=====================================================================")
print("Example 1 implementing thread sleep/delay")
print("method and measure how long the code load")
print("=====================================================================")


# PROGRAM WITHOUT THREADING
print("==============PROGRAM WITHOUT THREADING==============\n")
start = time.perf_counter()  # start performance counter

# call do_sleeping() 10 times
for _ in range(10):
    print(do_sleeping(1))
    print()

finish = time.perf_counter()  # finish performance counter

# counting duration with round from start to finish
duration = round(finish - start, 2)

# printing the duration
print(f'Code finished in {duration} second(s)\n\n')


# THREADING IMPLEMENTATION
print("==============THREADING IMPLEMENTATION==============\n")


start = time.perf_counter()  # start performance counter

# empty list of thread
threads = []

# call do_sleeping() 10 times with threading
for _ in range(10):
    t = threading.Thread(target=do_sleeping, args=[1])
    t.start()
    threads.append(t)  # put each thread into a threads list

# for loop that call thread.join() to execute each thread at same time
for thread in threads:
    thread.join()


finish = time.perf_counter()  # finish performance counter

# counting duration with round from start to finish
duration = round(finish - start, 2)

# printing the duration
print(f'Code finished in {duration} second(s)\n\n')


print("=====================================================================")
print("Example 2 implementing thread with")
print("thread pool executor")
print("=====================================================================")

start = time.perf_counter()  # start performance counter

with concurrent.futures.ThreadPoolExecutor() as executor:

    # list of seconds that use for threading
    seconds = [5, 4, 3, 2, 1]
    # create a future object with do_sleeping function with list comprehension loop
    results = [executor.submit(do_sleeping, sec) for sec in seconds]

    # result showing that function will be called 5 times *at the same time*
    # with 5 different argunemts and finish depending on the longest argument
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()  # finish performance counter

# counting duration with round from start to finish
duration = round(finish - start, 2)
# printing the duration
print(f'Code finished in {duration} second(s)\n\n')


print("=====================================================================")
print("Example 3 implementing thread with")
print("thread pool executor (mapping)")
print("=====================================================================")

start = time.perf_counter()  # start performance counter

with concurrent.futures.ThreadPoolExecutor() as executor:

    # list of seconds that use for threading
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
