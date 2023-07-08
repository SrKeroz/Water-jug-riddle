def save_state_changes(solution):
    """
        This function saves the state changes for each state in the solution.

    Args:
        solution(list or None): The solution returned by the solve_water_jug_riddle function.

    Returns:
        If a solution exists, the function returns a list of tuples, where each tuple contains an action name and the corresponding state.
        If no solution exists, it returns the string "There is no solution".

    """
    if solution:
        result = []
        for action_name, state in solution:
            result.append((action_name, str(state)))
        # return a list with the result
        return result
    else:
        # return a string 
        return "There is no solution"