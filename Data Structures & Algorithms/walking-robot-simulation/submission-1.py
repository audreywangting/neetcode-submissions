class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 1. initialize 4 directions 
        # 2. use d to record facing direction
        # 3. iterate command to keep moving 

        result = 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W

        x, y = 0, 0 # starting position
        d = 0 # facing north at the beginning

        # turn obstacle into set to quickly search
        obstacle_set = set()
        for a, b in obstacles:
            obstacle_set.add((a, b))

        for command in commands:
            if command == -1:
                d = (d+1) % 4

            elif command == -2:
                d = (d-1) % 4

            else:
                for _ in range(command):
                    dx, dy = direction[d]

                    nx = x + dx
                    ny = y + dy

                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    result = max(result, x*x + y*y)

        return result






