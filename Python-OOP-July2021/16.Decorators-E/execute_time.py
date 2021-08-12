from datetime import datetime


def exec_time(func):
    def wrapper(*args):
        st_time = datetime.now().strftime('%H:%M:%S')
        func(*args)
        end_time = datetime.now().strftime('%H:%M:%S')
        FMT = '%H:%M:%S'
        tdelta = datetime.strptime(end_time, FMT) - datetime.strptime(st_time, FMT)
        return tdelta.seconds
    return wrapper


# test first zero
import unittest
import time

class ExecTimeTests(unittest.TestCase):
    def test_zero_first(self):
        @exec_time
        def loop(start, end):
            total = 0
            for x in range(start, end):
                total += x
            return total
        self.assertEqual(round(loop(1, 10000000)), 1)

if __name__ == '__main__':
    unittest.main()
