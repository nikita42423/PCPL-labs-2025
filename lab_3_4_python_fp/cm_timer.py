import time
from contextlib import contextmanager

# Способ 1: На основе класса
class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"time: {elapsed_time:.1f}")


# Способ 2: С использованием contextlib
@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"time: {elapsed_time:.1f}")


# Тестовые примеры
if __name__ == '__main__':
    print("Тест cm_timer_1 (на основе класса):")
    with cm_timer_1():
        time.sleep(2.5)

    print("\nТест cm_timer_2 (с contextlib):")
    with cm_timer_2():
        time.sleep(1.5)

    print("\nТест с вложенными блоками:")
    with cm_timer_1():
        time.sleep(0.5)
        with cm_timer_2():
            time.sleep(0.3)
        time.sleep(0.2)
