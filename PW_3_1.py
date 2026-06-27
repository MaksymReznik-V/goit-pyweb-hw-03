import shutil
import time
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def process_file(item: Path, dist_path: Path) -> None:
    ext = item.suffix[1:] or 'no_extension'

    full_path = dist_path / ext
    full_path.mkdir(exist_ok=True)

    copy_path = full_path / item.name
    shutil.copy2(item, copy_path)

def process_directory(directory: Path, dist_path: Path, executor):
    for item in directory.iterdir():
        if item.is_file():
            executor.submit(process_file, item, dist_path)
        elif item.is_dir():
            executor.submit(process_directory, item, dist_path, executor)

def sorting_junk(directory_path: Path, dist_path: Path) -> None:
    dist_path.mkdir(exist_ok=True)

    with ThreadPoolExecutor(max_workers=4) as executor:
        process_directory(directory_path, dist_path, executor)


if __name__ == '__main__':
    start = time.perf_counter()

    source_path = Path(sys.argv[1])

    if len(sys.argv) > 2:
        dist_path = Path(sys.argv[2])
    else:
        dist_path = Path('dist')

    sorting_junk(source_path, dist_path)


    end = time.perf_counter()
    print(end-start)
