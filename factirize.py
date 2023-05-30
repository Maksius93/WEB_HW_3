import time
from multiprocessing import Pool, cpu_count


def factorize(number):
    results = []
    for i in range(1, number + 1):
        if number % i == 0:
            results.append(i)
    return results

def factorize_implementation(numbers):
    pool = Pool(cpu_count())
    result = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    return result


def sync_code(numbers) -> None:
    result = []
    start_time = time.time()
    for num in numbers:
        res = factorize(num)
        result.append(res)
    end_time = time.time()
    print(f"List {numbers} will be implementation for time {start_time - end_time}")


def async_code(numbers) -> None:
    start_time = time.time()
    result = factorize_implementation(numbers)
    end_time = time.time()

    print(f"List {numbers} will be implementation for time {start_time - end_time}")

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    sync_code(numbers)
    async_code(numbers)
