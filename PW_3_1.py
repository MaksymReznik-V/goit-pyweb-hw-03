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


def sorting_junk(directory_path: Path, dist_path: Path) -> None:
    dist_path.mkdir(exist_ok=True)

    with ThreadPoolExecutor(max_workers=4) as executor:
        for item in directory_path.rglob("*"):
            if item.is_file():
                executor.submit(process_file, item, dist_path)


if __name__ == '__main__':
    start = time.perf_counter()

    source_path = Path(sys.argv[1])

    if len(sys.argv) > 2:
        dist_path = Path(sys.argv[2])
    else:
        dist_path = Path('Dist')

    sorting_junk(source_path, dist_path)


    end = time.perf_counter()
    print(end-start)
