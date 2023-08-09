import time
import multiprocessing


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def parallel_factorize_list(numbers, num_workers):
    with multiprocessing.Pool(num_workers) as pool:
        result = pool.map(factorize, numbers)
    return result


if __name__ == "__main__":
    test_numbers = [100000, 200000, 300000, 400000, 500000]
    num_workers = multiprocessing.cpu_count()
    print(f'{num_workers} - Amount of CPU in your PC')

    start_time = time.time()
    parallel_result = parallel_factorize_list(test_numbers, num_workers)
    end_time = time.time()

    print("Parallel Execution Time:", end_time - start_time)
    print(parallel_result)
