# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_deque

import unittest
import time
from deque import Deque


class TestDeque(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        Test 1: A Deque exists.
        """
        try:
            Deque()
        except NameError:
            self.fail("Could not instantiate Deque.")

    def test_initial_size(self):
        """
        Test 2: A deque size is initially zero
        """
        q = Deque()
        self.assertEqual(0,q.items)

    """
    Guiding enqueuing and dequeuing with internal storage
    """

    def test_has_doubly_linked_list_internal(self):
        """
        Test 3: A deque has a data member, which is a dllist.
        """
        from pyllist import dllist # Hint: pip3 install pyllist
        d = Deque()
        self.assertEqual(dllist, type(d.data))

    def test_enqueue_left_one_internal(self):
        """
        Test 4: Enqueueing a 'left' value adds it to the beginning of the internal dllist.
        """
        d = Deque()
        d.enqueue_left('do')
        self.assertEqual('do', d.data.first.value)

    def test_enqueue_left_two_internal(self):
        """
        Test 5: Enqueueing two values to the left results in the first enqueued value
        being the second one in the list, and the second value being the first
        one in the list.
        """
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        self.assertEqual('do', d.data.last.value)
        self.assertEqual('ray', d.data.first.value)

    def test_enqueue_left_three_internal(self):
        """
        Test 6: Enqueueing three values results in the first enqueued value being the
        last one in the list, and the third value being the first one in the list.
        """
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        d.enqueue_left('me')
        self.assertEqual('do', d.data.last.value)
        self.assertEqual('me', d.data.first.value)

    def test_enqueue_right_one_internal(self):
        """
        Test 7: Enqueueing a 'right' value adds it to the beginning of the internal dllist.
        """
        d = Deque()
        d.enqueue_right('do')
        self.assertEqual('do', d.data.first.value)

    def test_enqueue_right_two_internal(self):
        """
        Test 8: Enqueueing two values to the right results in the first enqueued value
        being the first one in the list, and the second value being the last
        one in the list.
        """
        d = Deque()
        d.enqueue_right('do')
        d.enqueue_right('ray')
        self.assertEqual('do', d.data.first.value)
        self.assertEqual('ray', d.data.last.value)

    def test_enqueue_right_three_internal(self):
        """
        Test 9: Enqueueing three values results in the first enqueued value being the
        first one in the list, and the third value being the last one in the list.
        """
        d = Deque()
        d.enqueue_right('do')
        d.enqueue_right('ray')
        d.enqueue_right('me')
        self.assertEqual('do', d.data.first.value)
        self.assertEqual('me', d.data.last.value)

    def test_dequeue_left_one(self):
        """
        Test 10: Dequeuing from the left of a single-element deque returns the single value.
        """
        d = Deque()
        d.enqueue_left('do')
        self.assertEqual('do', d.dequeue_left())
        d.enqueue_right('do')
        self.assertEqual('do', d.dequeue_left())

    def test_dequeue_left_one_internal(self):
        """
        Test 11: Dequeuing from the left of a single-element deque removes it from the
        internal dllist.
        """
        d = Deque()
        d.enqueue_left('do')
        self.assertEqual(1, d.size())
        _ = d.dequeue_left()
        self.assertEqual(0, d.size())

    def test_dequeue_left_two(self):
        """
        Test 12: Dequeuing from the left of a two-element deque returns the last
        left-enqueued value.
        """
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        self.assertEqual('ray', d.dequeue_left())

    def test_dequeue_left_two_internal(self):
        """
        Test 13: Dequeuing from the left of a two-element deque removes the last
        left-enqueued value from the dllist.
        """
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        _ = d.dequeue_left()
        self.assertEqual('do', d.data.first.value)

    def test_dequeue_left_three(self):
        """
        Test 14: Dequeuing from the left of a three-element deque returns each enqueued
        value in FIFO order.
        """
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        d.enqueue_left('me')
        self.assertEqual('me', d.dequeue_left())
        self.assertEqual('ray', d.dequeue_left())
        self.assertEqual('do', d.dequeue_left())

    def test_dequeue_left_three_internal(self):
        """
        Test 15: Dequeuing from the left of a three-element deque removes each dequeued
        value from the internal dllist, in FIFO order.
        """
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        d.enqueue_left('me')
        _ = d.dequeue_left()
        self.assertEqual('ray', d.data.first.value)
        _ = d.dequeue_left()
        self.assertEqual('do', d.data.first.value)

    def test_dequeue_right_one(self):
        """
        Test 16: Dequeuing from the right of a single-element deque returns the single value.
        """
        d = Deque()
        d.enqueue_right('do')
        self.assertEqual('do', d.dequeue_right())
        d.enqueue_left('do')
        self.assertEqual('do', d.dequeue_right())

    def test_dequeue_right_one_internal(self):
        """
        Test 17: Dequeuing from the right of a single-element deque removes it from the
        internal dllist.
        """
        d = Deque()
        d.enqueue_right('do')
        self.assertEqual(1, d.size())
        _ = d.dequeue_right()
        self.assertEqual(0, d.size())

    def test_dequeue_right_two(self):
        """
        Test 18: Dequeuing from the right of a two-element deque returns the last
        right-enqueued value.
        """
        d = Deque()
        d.enqueue_right('do')
        d.enqueue_right('ray')
        self.assertEqual('ray', d.dequeue_right())

    def test_dequeue_right_two_internal(self):
        """
        Test 19: Dequeuing from the right of a two-element deque removes the last
        right-enqueued value from the dllist.
        """
        d = Deque()
        d.enqueue_right('do')
        d.enqueue_right('ray')
        _ = d.dequeue_right()
        self.assertEqual('do', d.data.first.value)

    def test_dequeue_right_three(self):
        """
        Test 20: Dequeuing from the right of a three-element deque returns each enqueued
        value in LIFO order.
        """
        d = Deque()
        d.enqueue_right('do')
        d.enqueue_right('ray')
        d.enqueue_right('me')
        self.assertEqual('me', d.dequeue_right())
        self.assertEqual('ray', d.dequeue_right())
        self.assertEqual('do', d.dequeue_right())

    def test_dequeue_right_three_internal(self):
        """
        Test 21: Dequeuing from the right of a three-element deque removes each dequeued
        value from the internal dllist, in LIFO order.
        """
        d = Deque()
        d.enqueue_right('do')
        d.enqueue_right('ray')
        d.enqueue_right('me')
        _ = d.dequeue_right()
        self.assertEqual('do', d.data.first.value)
        _ = d.dequeue_right()
        self.assertEqual('do', d.data.first.value)

    def test_enqueue_left_dequeue_right(self):
        """
        Test 22: Dequeuing from the right returns each left-enqueued value in FIFO order.
        """
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        d.enqueue_left('me')
        self.assertEqual('do', d.dequeue_right())
        self.assertEqual('ray', d.dequeue_right())
        self.assertEqual('me', d.dequeue_right())

    def test_enqueue_right_dequeue_left(self):
        """
        Test 23: Dequeuing from the left returns each right-enqueued value in FIFO order.
        """
        d = Deque()
        d.enqueue_right('do')
        d.enqueue_right('ray')
        d.enqueue_right('me')
        self.assertEqual('do', d.dequeue_left())
        self.assertEqual('ray', d.dequeue_left())
        self.assertEqual('me', d.dequeue_left())


    """
    Emptiness
    """

    def test_empty(self):
        d = Deque()
        self.assertTrue(d.is_empty())

    def test_not_empty_left(self):
        d = Deque()
        d.enqueue_left('do')
        self.assertFalse(d.is_empty())

    def test_not_empty_right(self):
        d = Deque()
        d.enqueue_right('do')
        self.assertFalse(d.is_empty())

    def test_empty_after_dequeue_left(self):
        d = Deque()
        d.enqueue_left('do')
        _ = d.dequeue_left()
        self.assertTrue(d.is_empty())

    def test_empty_after_dequeue_right(self):
        d = Deque()
        d.enqueue_left('do')
        _ = d.dequeue_right()
        self.assertTrue(d.is_empty())

    def test_not_empty_multiple_left(self):
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        _ = d.dequeue_left()
        self.assertFalse(d.is_empty())

    def test_not_empty_multiple_right(self):
        d = Deque()
        d.enqueue_left('do')
        d.enqueue_left('ray')
        _ = d.dequeue_right()
        self.assertFalse(d.is_empty())

    """
    Size
    """

    def test_dequeue_right_from_an_empty_deque(self):
        q = Deque()
        try:
            q.dequeue_right()
            self.fail("Did not raise an Exception")
        except ValueError:
            self.assertEqual(0, q.size())

    def test_dequeue_left_from_an_empty_deque(self):
        q = Deque()
        try:
            q.dequeue_left()
            self.fail("Did not raise an Exception")
        except ValueError:
            self.assertEqual(0, q.size())

    def test_size_after_enqueue_right(self):
        q = Deque()
        q.enqueue_right('do')
        self.assertEqual(1, q.size())

    def test_size_after_enqueue_left(self):
        q = Deque()
        q.enqueue_left('ray')
        self.assertEqual(1, q.size())

    def test_size_after_dequeue_right(self):
        q = Deque()
        q.enqueue_right('do')
        q.enqueue_right('ray')
        q.enqueue_right('me')
        q.enqueue_right('fa')
        self.assertEqual(4, q.size())
        q.dequeue_right()
        self.assertEqual(3, q.size())

    def test_size_after_dequeue_left(self):
        q = Deque()
        q.enqueue_left('do')
        q.enqueue_left('ray')
        q.enqueue_left('me')
        q.enqueue_left('fa')
        self.assertEqual(4, q.size())
        q.dequeue_left()
        self.assertEqual(3, q.size())

    def test_size_after_dequeue_right_or_left(self):
        q = Deque()
        q.enqueue_left('do')
        q.enqueue_right('ray')
        q.enqueue_left('me')
        q.enqueue_right('fa')
        self.assertEqual(4, q.size())
        q.dequeue_left()
        self.assertEqual(3, q.size())
        q.dequeue_right()
        self.assertEqual(2, q.size())


    """
    Algorithmic complexity
    """

    def test_enqueue_left_vs_right_efficiency(self):
        time_samples = []
        for _ in range(1000):
            d = Deque()
            start = time.time()
            d.enqueue_left('fake')
            end = time.time()
            time_samples.append(end - start)
        small = sum(time_samples) / len(time_samples)

        large = Deque()
        for _ in range(1_000_000):
            large.enqueue_left('fake')

        time_samples = []
        for _ in range(1000):
            start = time.time()
            large.enqueue_left('fake')
            end = time.time()
            time_samples.append(end - start)
        large_avg = sum(time_samples) / len(time_samples)
        self.assertAlmostEqual(small, large_avg, delta=small)

        large = Deque()
        for _ in range(1_000_000):
            large.enqueue_right('fake')

        time_samples = []
        for _ in range(1000):
            start = time.time()
            large.enqueue_right('fake')
            end = time.time()
            time_samples.append(end - start)
        large_avg = sum(time_samples) / len(time_samples)
        self.assertAlmostEqual(small, large_avg, delta=small)

    def test_dequeue_left_vs_right_efficiency(self):
        time_samples = []
        for _ in range(1000):
            d = Deque()
            d.enqueue_left('fake')
            start = time.time()
            d.dequeue_left()
            end = time.time()
            time_samples.append(end - start)
        small = sum(time_samples) / len(time_samples)

        large = Deque()
        for _ in range(1_000_000):
            large.enqueue_left('fake')

        time_samples = []
        for _ in range(1000):
            start = time.time()
            large.dequeue_left()
            end = time.time()
            time_samples.append(end - start)
        large_avg = sum(time_samples) / len(time_samples)
        self.assertAlmostEqual(small, large_avg, delta=small)

        large = Deque()
        for _ in range(1_000_000):
            large.enqueue_left('fake')

        time_samples = []
        for _ in range(1000):
            start = time.time()
            large.dequeue_right()
            end = time.time()
            time_samples.append(end - start)
        large_avg = sum(time_samples) / len(time_samples)
        self.assertAlmostEqual(small, large_avg, delta=small)


def fake_value():
    return f"FAKE {time.time()}"


if __name__ == '__main__':
    unittest.main()