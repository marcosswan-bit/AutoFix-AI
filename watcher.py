import time
import os
from fixer import analyze_file

def watch_directory(path):
    files_last_modified = {}

    while True:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    last_modified = os.path.getmtime(full_path)

                    if full_path not in files_last_modified or files_last_modified[full_path] != last_modified:
                        print(f"📝 Change detected: {file}")
                        analyze_file(full_path)
                        files_last_modified[full_path] = last_modified

        time.sleep(2)
