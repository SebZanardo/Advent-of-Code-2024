import os
import time
import subprocess
import argparse


RED = '\033[0;31m'
YELLOW = '\033[0;33m'
GREEN = '\033[0;32m'
MAGENTA = '\033[0;35m'
OFF = '\033[0m'

PYTHON_FILE_EXTENSION = ".py"
SCRIPT_FILE_EXTENSIONS = (PYTHON_FILE_EXTENSION)


def print_error(message: str) -> None:
    print(f"{RED}[ERROR] {OFF}{message}")


def print_elapsed_time(elapsed_time: float, repeat_times: int) -> None:
    # Decide text colour based on running time
    colour = RED
    if elapsed_time < 10:
        colour = GREEN
    elif elapsed_time < 15:
        colour = YELLOW

    if repeat_times <= 1:
        print(f"{colour}Elapsed time: {elapsed_time}{OFF}")
    else:
        print(f"{colour}Average elapsed time: {elapsed_time}{OFF}")


def run_python_script(script_path: str) -> int:
    return subprocess.run(
        ["python3", script_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    ).returncode


def benchmark_script(
    script_path: str,
    extension: str,
    repeat_times: int
) -> None:
    print(f"{'-' * 80}")
    print(f"{MAGENTA}{script_path}{OFF}")

    # Run benchmark repeat_times amount of times
    total_elapsed_time = 0
    error = False
    for _ in range(repeat_times):
        start_time = time.time()

        # Call function to run code for filetype
        return_code = -1
        if extension == PYTHON_FILE_EXTENSION:
            return_code = run_python_script(script_path)

        # Print result
        if return_code != 0:
            # There was an error with execution, break
            error = True
            print_error("Could not successfully run code")
            break

        # Successful execution, add elapsed time
        end_time = time.time()
        total_elapsed_time += end_time - start_time

    if not error:
        averaged_elapsed_time = total_elapsed_time / repeat_times
        print_elapsed_time(averaged_elapsed_time, repeat_times)

    print(f"{'-' * 80}")


def benchmark(
    folder_path: str,
    repeat_times: int
) -> None:
    # Change directory to solution path
    os.chdir(folder_path)

    print(f"\nBenchmarking solutions in '{folder_path}'")

    # Collect list of file types
    for file_name in os.listdir():
        extension = os.path.splitext(file_name)[1]

        if not extension or extension not in SCRIPT_FILE_EXTENSIONS:
            continue

        benchmark_script(file_name, extension, repeat_times)


# For parsing arguments correctly and giving detailed help
parser = argparse.ArgumentParser(
    description="benchmark all .py scripts in a directory"
)
parser.add_argument(
    "path",
    help="path to directory that contains scripts to benchmark",
    type=str
)
parser.add_argument(
    "--repeat_times",
    "-r",
    help="how many times to repeat benchmark and average results",
    type=int,
    default=1
)
args = parser.parse_args()

path = args.path
repeat_times = args.repeat_times

benchmark(path, repeat_times)
