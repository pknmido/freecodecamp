import random
import copy


class Hat:

  def __init__(self, **balls):
    self.contents = []
    for ball, count in balls.items():
      self.contents.extend([ball] * count)

  def draw(self, num_balls):
    if num_balls >= len(self.contents):
      return self.contents
    drawn_balls = random.sample(self.contents, num_balls)
    for ball in drawn_balls:
      self.contents.remove(ball)
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    drawn_balls_count = {
      color: drawn_balls.count(color)
      for color in set(drawn_balls)
    }
    success = True
    for color, count in expected_balls.items():
      if drawn_balls_count.get(color, 0) < count:
        success = False
        break
    if success:
      success_count += 1
  return success_count / num_experiments
