# Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def print_number(num):
    time.sleep(1)
    return f"Number: {num}"

numbers=[1,3,2,4,5,2,6,2,7,8]
t = time.time()

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(print_number, numbers)

    for result in results:
        print(result)

    finished_time=time.time()-t
    print(finished_time)