from collections import deque        # Import deque from collections module to use a double-ended queue

class RecentCounter:                 # Define a class named RecentCounter

    def __init__(self):              # Constructor method, initializes an empty deque
        self.deque = deque()         # Create a deque instance to store timestamps

    def ping(self, t: int) -> int:   # Define the ping method, which takes an integer t as input and returns an integer
        deque = self.deque           # Assign self.deque to a local variable for convenience
        deque.append(t)              # Add the current timestamp t to the deque
        start = t - 3000             # Calculate the starting threshold, 3000 milliseconds before t
        while deque[0] < start:      # Remove outdated timestamps that are outside the 3000ms window
            deque.popleft()          # Remove the leftmost element from the deque
        return len(deque)            # Return the number of elements in the deque, representing the count of pings
