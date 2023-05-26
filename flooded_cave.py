def solution(x):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    m = len(x)
    n = len(x[0])
    map = x

    queue = [(0, 0, 0)]  # (row, column, steps)
    visited = set([(0, 0)])
    flooded_steps = 0
    is_fully_flooded = False
    is_resimulate = False

    while queue:
        queue_length = len(queue)
        row, col, steps = queue.pop(0)
        
        # Stop expanding the flood if re-simulate is required
        if is_resimulate is True:
            is_resimulate = False
        else:
            map, flooded_steps, is_fully_flooded = flooding_map(map, flooded_steps)

        # Reached the exit
        if row == m - 1 and col == n - 1:
            # Fully flooded, now calculate the maximum turn we can stay
            if is_fully_flooded:
                return flooded_steps - steps if flooded_steps != 0 else 1e9
            # Not fully flooded yet, please be patient until fully flooded
            queue.insert(0, (row, col, steps))
            continue

        # Next move guessing
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy

            if (
                0 <= new_row < m
                and 0 <= new_col < n
                and map[new_row][new_col] == 0
                and (new_row, new_col) not in visited
            ):
                queue.append((new_row, new_col, steps + 1))
                visited.add((new_row, new_col))

        # Wrong bet on the move, re-simulate
        if queue_length > len(queue):
            is_resimulate = True

    # Mission impossible and I'm not Tom Cruise
    return -1
    

def flooding_map(map, steps):
    new_map = []
    is_fully_flooded = False

    # Deep copy the map
    for row in map:
        new_map.append(row[:])

    # Simulate the flooding
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col != 2:
                continue

            # First row
            if i == 0:
                if j-1 >= 0:
                    new_map[i][j-1] = 2 if map[i][j-1] == 0 else map[i][j-1]
                if j+1 < len(row):
                    new_map[i][j+1] = 2 if map[i][j+1] == 0 else map[i][j+1]
                new_map[i+1][j] = 2 if map[i+1][j] == 0 else map[i+1][j]
            # Last row
            elif i == len(map) - 1:
                new_map[i-1][j] = 2 if map[i-1][j] == 0 else map[i-1][j]
                if j-1 >= 0:
                    new_map[i][j-1] = 2 if map[i][j-1] == 0 else map[i][j-1]
                if j+1 < len(row):
                    new_map[i][j+1] = 2 if map[i][j+1] == 0 else map[i][j+1]
            # Middle rows
            else:
                new_map[i-1][j] = 2 if map[i-1][j] == 0 else map[i-1][j]
                if j-1 >= 0:
                    new_map[i][j-1] = 2 if map[i][j-1] == 0 else map[i][j-1]
                if j+1 < len(row):
                    new_map[i][j+1] = 2 if map[i][j+1] == 0 else map[i][j+1]
                new_map[i+1][j] = 2 if map[i+1][j] == 0 else map[i+1][j]

    if new_map[len(map)-1][-1] == 2:
        is_fully_flooded = True
    else:
        steps += 1

    # Flood is stopped somehow
    if new_map == map:
        is_fully_flooded = True
        steps = 0

    return (new_map, steps, is_fully_flooded)


if __name__ == "__main__":
    assert solution(
        [
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 2, 0],
            [0, 1, 0, 0, 2, 1, 0],
            [0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0]
        ]
    ) == 3

    assert solution(
        [
            [0, 0, 0, 0],
            [0, 2, 1, 0],
            [0, 1, 0, 0]
        ]
    ) == -1

    assert solution(
        [
            [0, 0, 0],
            [1, 1, 0],
            [2, 1, 0]
        ]
    ) == 1e9

    assert solution(
        [
            [0, 0, 0, 0, 2],
            [1, 0, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ) == 1

    assert solution(
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 2],
        ]
    ) == -1

    assert solution(
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 2],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
        ]
    ) == 0

    assert solution(
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 2],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
        ]
    ) == -1

    assert solution(
        [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0],
            [0, 0, 2, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    ) == 3

    print("All tests passed!")
