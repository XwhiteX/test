import pygal
from random import randint

class Die:
    """
    一个骰子类
    """

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die = Die()
results = []
# 掷100次骰子，并将结果放在列表中
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果可视化
hist = pygal.Bar()
hist.title = "result of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "frequency of result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
