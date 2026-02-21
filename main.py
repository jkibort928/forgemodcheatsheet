from enum import Enum
from collections import deque

# Color "costs"
class Color(Enum):
    RED: int = 16
    ORANGE: int = 13
    YELLOW: int = 7
    GREEN: int = 2
    
    CYAN: int = -3
    LBLUE: int = -6
    DBLUE: int = -9
    PURPLE: int = -15

# Get a list of colors from a completed "visited" dict
def countsFromVisited(target: int, visited: dict[int, Color | None]):
    current = target
    counts = {color.name: 0 for color in Color}
    currColor = visited[current]
    while currColor:
        counts[currColor.name] += 1
        current = current - currColor.value
        currColor = visited[current]
    return counts

# Find the shortest sequence of colors that adds to any given number
# Returns a dict of color counts
def findCounts(target: int):
    # Basically a BFS problem
    # Each edge is one of the colors and nodes are the target numbers

    # BFS Queue. Contains the number to vist and its color that it came from
    toVisit = deque([(0, None)])
    
    # Dict where keys are target numbers,
    # and the values are the color used to get to it.
    visited = {}

    while toVisit:
        current, fromColor = toVisit.popleft()

        if current in visited:
            continue

        visited[current] = fromColor

        if current == target:
            return countsFromVisited(target, visited)

        for color in Color:
            toVisit.append((current + color.value, color))

# prints an easy to read representation of the counts
def presentCounts(counts):
    for colorname, count in counts.items():
        if count > 0:
            print(f"{colorname}:\t{count}")


def main():
    while True:
        target = int(input("Type Goal number (0 to stop): "))
        if target == 0:
            break
        presentCounts(findCounts(target))
        

main()
