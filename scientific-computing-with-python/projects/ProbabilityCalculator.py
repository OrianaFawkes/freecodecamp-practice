# Scientific Computing with Python Project 5
# Made by Oriana Fawkes '24

import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(f'{key}')

    def draw(self, num_balls_drawn):
        removed_balls = []
        for _ in range(num_balls_drawn):
            removed_balls.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
        return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0
    for _ in range(num_experiments):
        result = hat.draw(num_balls_drawn)
        result_counts = {color: result.count(color) for color in set(result)}
        if all(result_counts.get(color, 0) >= expected_balls.get(color, 0) for color in expected_balls):
            match+=1
    return match/num_experiments

random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)