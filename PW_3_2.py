import time
from multiprocessing import Pool, cpu_count


def get_division(n: int) -> list[int]:
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result


def factorize_parallel(*number: int) -> list[list[int]]:
    with Pool(cpu_count()) as pool:
        return pool.map(get_division, number)


def factorize_sync(*number: int) -> list[list[int]]:
    results =[]

    for n in number:
        results.append(get_division(n))

    return results


if __name__ == '__main__':

    start = time.perf_counter()
    factorize_parallel(128, 255, 99999, 10651060)
    end = time.perf_counter()
    print("Parallel:", end - start)

    start = time.perf_counter()
    factorize_sync(128, 255, 99999, 10651060)
    end = time.perf_counter()
    print("Sync:", end - start)

