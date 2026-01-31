"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""


def has_duplicates(product_ids):
    """
    Returns True if any duplicate IDs exist, otherwise False.
    """
    seen = set()

    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)

    return False


# Justification:
# I chose a set because it supports fast membership checks, which is exactly what we need to detect repeats.
# The main operations are "in" checks and inserts into the set, which are O(1) average time.
# Expected runtime: O(n) time, O(n) space in the worst case (all IDs unique).


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque


class TaskQueue:
    def __init__(self):
        # deque is efficient for appending to the end and popping from the front
        self._tasks = deque()

    def add_task(self, task):
        self._tasks.append(task)

    def remove_oldest_task(self):
        if not self._tasks:
            return None
        return self._tasks.popleft()


# Justification:
# I chose a queue structure using collections.deque because it preserves insertion order and removes from the front efficiently.
# The main operations are append (add to back) and popleft (remove from front), both O(1).
# Expected runtime: O(1) for add_task and O(1) for remove_oldest_task; space grows O(n) with the number of tasks stored.


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""


class UniqueTracker:
    def __init__(self):
        self._seen = set()

    def add(self, value):
        self._seen.add(value)

    def get_unique_count(self):
        return len(self._seen)


# Justification:
# I chose a set because it stores only unique values automatically and allows constant-time average inserts.
# The main operations are inserting into the set and reading its length; both are O(1) average.
# Expected runtime: add is O(1) average, get_unique_count is O(1); space is O(u) where u is the number of unique values.
