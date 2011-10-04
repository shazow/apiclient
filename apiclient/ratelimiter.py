import time
from threading import Lock


class RateExceededError(Exception):
    pass


class RateLimiter(object):
    def __init__(self, max_messages=10, every_seconds=1):
        self.max_messages = max_messages
        self.every_seconds = every_seconds
        self.lock = Lock()

        self._reset_window()

    def _reset_window(self):
        self.window_num = 0
        self.window_time = time.time()

    def acquire(self, block=True, timeout=None):
        self.lock.acquire()

        now = time.time()
        if now - self.window_time > self.every_seconds:
            # New rate window
            self._reset_window()

        if self.window_num >= self.max_messages:
            # Rate exceeding
            if not block:
                self.lock.release()
                raise RateExceededError()

            wait_time = self.window_time + self.every_seconds - now
            if timeout and wait_time > timeout:
                self.lock.release()
                time.sleep(timeout)

                raise RateExceededError()

            self.lock.release()
            time.sleep(wait_time)
            self.lock.acquire()

            self._reset_window()

        self.window_num += 1

        self.lock.release()
