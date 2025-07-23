import time

class Timer:
    def __init__(self, name="Process"):
        self.name = name

    def __enter__(self):
        print(f"[{self.name}] Started...")
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start
        print(f"[{self.name}] Finished in {elapsed:.2f} seconds.")