import shutil
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def process_file(item: Path, dist_path: Path) -> None:
    ext = item.suffix[1:]

    full_path = dist_path / ext
    full_path.mkdir(exist_ok=True)

    copy_path = full_path / item.name
    shutil.copy2(item, copy_path)


def sorting_junk(directory_path: Path) -> None:
    dist_path = Path(r'D:\dist')
    dist_path.mkdir(exist_ok=True)

    files = [
        item
        for item in directory_path.rglob("*")
        if item.is_file()
    ]

    with ThreadPoolExecutor(max_workers=4) as executor:
        for item in files:
            executor.submit(process_file, item, dist_path)


if __name__ == '__main__':
    start = time.perf_counter()

    sorting_junk(Path(r'D:\Deutsch'))

    end = time.perf_counter()
    print(end-start)
