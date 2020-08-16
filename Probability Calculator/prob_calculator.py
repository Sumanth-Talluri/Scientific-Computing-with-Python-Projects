import copy
import random
# Consider using the modules imported above.


class Hat:

    contents = []

    def __init__(self, **kwargs):
        args = {}
        self.contents = []
        for key, value in kwargs.items():
            args[key] = value
            for i in range(value):
                self.contents.append(key)

    def draw(self, no_balls_to_draw):
        contents = self.contents
        if len(contents) < no_balls_to_draw:
            return contents
        else:
            balls_drawn = []
            while len(balls_drawn) < no_balls_to_draw:
                index = random.randint(0, len(contents)-1)
                ball = contents[index]
                contents.remove(ball)
                balls_drawn.append(ball)
            return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for x in range(num_experiments):
        color_count = 0
        copy_of_hat = copy.deepcopy(hat)
        ball_drawn = copy_of_hat.draw(num_balls_drawn)
        for color in expected_balls.keys():
            if ball_drawn.count(color) >= expected_balls[color]:
                color_count += 1
        if color_count == len(expected_balls):
            success_count += 1
    return success_count/num_experiments
