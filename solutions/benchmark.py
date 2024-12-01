import os
import sys
import time
import subprocess


RED = '\033[0;31m'
YELLOW = '\033[0;33m'
GREEN = '\033[0;32m'
OFF = '\033[0m'

PART1_FILENAME = "part1.py"
PART2_FILENAME = "part2.py"
INPUT_FILENAME = "input.in"
REPEAT_TIMES = 5


def print_elapsed_time(elapsed_time: float) -> None:
    # Decide text colour based on running time
    colour = RED
    if elapsed_time < 10:
        colour = GREEN
    elif elapsed_time < 15:
        colour = YELLOW

    print(f"{colour}Elapsed time: {elapsed_time}{OFF}")


def run_script(script_path: str, input_path: str) -> int:
    return subprocess.run(
        ["python3", script_path, input_path],
        timeout=30,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    ).returncode


def benchmark(
    folder_path: str,
    script_filename: str,
    input_filename: str
) -> None:
    script_path = os.path.join(folder_path, script_filename)
    input_path = os.path.join(folder_path, input_filename)

    print(f"{'-' * 80}")
    print(script_path)

    # Run benchmark REPEAT_TEST amount of times
    total_elapsed_time = 0
    error = False
    for _ in range(REPEAT_TIMES):
        start_time = time.time()

        return_code = run_script(script_path, input_path)

        # Print result
        if return_code != 0:
            # There was an error with execution, break
            error = True
            print(f"{RED}[ERROR] {OFF}", end="")
            print("File does not exist!")
            break

        # Successful execution, add elapsed time
        end_time = time.time()
        total_elapsed_time += end_time - start_time

    if not error:
        averaged_elapsed_time = total_elapsed_time / REPEAT_TIMES
        print_elapsed_time(averaged_elapsed_time)

    print(f"{'-' * 80}")


# Try to read a path to an input file from command line arguments
if len(sys.argv) <= 1:
    print(f"{RED}[ERROR] {OFF}", end="")
    print("Please specify a directory to benchmark as a command line argument")
    sys.exit(0)

path = sys.argv[1]

benchmark(path, PART1_FILENAME, INPUT_FILENAME)
benchmark(path, PART2_FILENAME, INPUT_FILENAME)
