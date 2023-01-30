import queue
import random
from threading import Thread


class Calculating(Thread):

    def __init__(self, N):
        super().__init__()
        self.N = N

    def run(self) -> None:
        for _ in range(100):
            number = random.randint(1, 100)
            degree = random.randint(1, 100)
            print(f'{self.N} -- {number} ** {degree} = ', number ** degree)

calc1 = Calculating(N=1)
calc2 = Calculating(N=2)

calc1.start()
calc2.start()

calc1.join()
calc2.join()

print('Готово')


