from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food # food position

        self.snake = deque([(0, 0)]) # 紀錄蛇身體的順序，知道誰是head, tail，每次移動都是加入新的head、移除舊的tail
        self.occupied = {(0, 0)} # 用set紀錄蛇的身體佔的哪些格子

        self.score = 0
        self.food_index = 0 # 紀錄下一個應該出現的食物，要照順序吃

        self.game_over = False

    def move(self, direction: str) -> int:
        # bump into food -> length & score += 1
        # game over when 1. snake goes out of bound 2. run into itself

        # 1. move
        # get current head
        row, col = self.snake[0]
        directions = {"R": (0, 1), # col + 1: 往右
                    "D": (1, 0), # row + 1: 往下
                    "L": (0, -1), # col -1: 往左
                    "U": (-1, 0)} # row - 1: 往上
        dr, dc = directions[direction]
        new_row = row + dr
        new_col = col + dc
        new_head = (new_row, new_col)

        # 2. game over - 1. check boundary
        if not (0 <= new_row < self.height and 0 <= new_col < self.width):
            self.game_over = True
            return -1
            
        # 2. check food
        get_food = (self.food_index < len(self.food) and new_head == tuple(self.food[self.food_index]))
        
        # if no food -> snake 不會變長，tail要remove
        if not get_food:
            tail = self.snake.pop()
            self.occupied.remove(tail)

        # 3. game over - 2. run into itself
        if new_head in self.occupied:
            self.game_over = True
            return -1

        # 4. add new head
        self.snake.appendleft(new_head)
        self.occupied.add(new_head)

        # update score if get food
        if get_food:
            self.score += 1
            self.food_index += 1

        return self.score





# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
