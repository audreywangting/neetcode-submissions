class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 1. initialize 4 directions
        # 2. for loop iterate all commands
        # 3. calculate the distance

        # 1. initialize
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W

        # 方向在 directions 裡面的 index
        d = 0 # facing north
        x, y = 0, 0
        result = 0

        # 2. convert obstacles to set
        # turn [[0, 2], [1, 2]] into {(0, 2), (1, 2)}
        # 先把內部list轉tuple (), 再丟到set
        # map: 對 iterable 裡面的每個元素，執行指定的 function
        obstacle_set = set()
        for a, b in obstacles:
            obstacle_set.add((a, b))

        # 3. proceed command
        for command in commands:
            # turn right 
            if command == -1:
                d = (d+1) % 4 # 1 as right

            # turn left
            elif command == -2:
                d = (d-1) % 4 # 3 as left

            else:
                for _ in range(command):
                    dx, dy = direction[d]

                    nx = x + dx
                    ny = y + dy

                    # check obstacle
                    if (nx, ny) in obstacle_set:
                        break

                    # update position
                    x, y = nx, ny

                    # update max distance
                    result = max(result, x*x + y*y)

        return result










