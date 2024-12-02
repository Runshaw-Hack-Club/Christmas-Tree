import os
import subprocess
import sys
import time


def run_python_file(file_path):
    try:
        proc = subprocess.Popen(
            [sys.executable, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        try:
            stdout, stderr = proc.communicate(timeout=20)
            print(f"Output of {file_path}:\n{stdout.decode()}")
            if stderr:
                print(f"Errors in {file_path}:\n{stderr.decode()}")
        except subprocess.TimeoutExpired:
            proc.kill()
            print(f"Process for {file_path} killed after 20 seconds")
    except Exception as e:
        print(f"Failed to run {file_path}: {e}")


def iterate_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                run_python_file(file_path)


def git_pull(directory):
    try:
        proc = subprocess.Popen(
            ["git", "pull"],
            cwd=directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = proc.communicate()
        print(f"Git pull output:\n{stdout.decode()}")
        if stderr:
            print(f"Git pull errors:\n{stderr.decode()}")
    except Exception as e:
        print(f"Failed to run git pull: {e}")


if __name__ == "__main__":
    path_to_search = "../examples"
    cycle_count = 0

    while True:
        iterate_files(path_to_search)
        cycle_count += 1
        if cycle_count % 3 == 0:
            git_pull(path_to_search)
        time.sleep(1)
