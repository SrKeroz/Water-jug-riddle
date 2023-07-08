# import deque
from collections import deque

# import class State
from app.water_jug_riddle.state import State


def solve_water_jug_riddle(x, y, z):
    """
    This function solves the Water Jug Riddle using a breadth-first search algorithm.

    Parameters:
        x (int): The capacity of the x_gallon jug.
        y (int): The capacity of the y_gallon jug.
        z (int): The desired amount of water to measure.

    Returns:
        If a solution exists, the function returns a list of actions and corresponding states that lead to the desired measurement.
        If no solution exists, it returns None.

    """

    # Create a queue for breadth-first search
    queue = deque()

    # Create a set to store visited states
    visited = set()

    # Enqueue the initial state (both jugs empty)
    initial_state = State(0, 0)
    queue.append(initial_state)
    visited.add(initial_state)

    # Dictionary to keep track of the actions leading to each state
    actions = {initial_state: []}

    # Breadth-first search
    while queue:
        current_state = queue.popleft()

        if current_state.x == z or current_state.y == z:
            # Found a solution
            return actions[current_state]

        # Perform all possible actions
        actions_list = [
            ("Fill X", x, current_state.y),
            ("Fill Y", current_state.x, y),
            ("Empty X", 0, current_state.y),
            ("Empty Y", current_state.x, 0),
            ("Transfer X to Y", max(0, current_state.x + current_state.y - y), min(y, current_state.x + current_state.y)),
            ("Transfer Y to X", min(x, current_state.x + current_state.y), max(0, current_state.x + current_state.y - x))
        ]

        for action_name, new_x, new_y in actions_list:
            new_state = State(new_x, new_y)

            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
                actions[new_state] = actions[current_state] + [(action_name, new_state)]

    # No solution found
    return None