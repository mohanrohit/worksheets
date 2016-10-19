# generate a number

import random

class NumberGenerator(object):
  def __init__(self):
    pass

  def run(self):
    raise Exception, "run() for %s is not implemented." % self.__class__.__name__

class DiscreteNumberGenerator(NumberGenerator):
  def __init__(self, **kwargs):
    self.allow_zero = kwargs.get("allow_zero", True)

    self.min = kwargs["min"] if "min" in kwargs else 0 if self.allow_zero else 1
    self.max = kwargs["max"] if "max" in kwargs else 10

    if self.max < self.min:
      self.max, self.min = self.min, self.max

  def run(self):
    number = random.randint(self.min, self.max)
    while number == 0:
      number = random.randint(self.min, self.max)

    return number

class FractionGenerator(NumberGenerator):
  def __init__(self, **kwargs):
    self.numerator_generator = kwargs["numerator"] if "numerator" in kwargs else DiscreteNumberGenerator(**kwargs)
    self.denominator_generator = kwargs["denominator"] if "denominator" in kwargs else DiscreteNumberGenerator(**kwargs)
    self.allow_mixed = kwargs.get("allow_mixed", False)

  def run(self):
    numerator = self.numerator_generator.run()

    while True:
      denominator = self.denominator_generator.run()
      if denominator != 0:
        break

    if not self.allow_mixed and numerator > denominator:
      numerator, denominator = denominator, numerator

    return (numerator, denominator)

class DecimalGenerator(NumberGenerator):
  def __init__(self, **kwargs):
    self.max_decimals = kwargs["max_decimals"] if "max_decimals" in kwargs else 2

    self.whole_part_generator = DiscreteNumberGenerator(**kwargs)
    self.fractional_part_generator = DiscreteNumberGenerator(max=10 ** self.max_decimals - 1, min=1)

  def run(self):
    whole_part = self.whole_part_generator.run()
    fractional_part = self.fractional_part_generator.run()

    return whole_part + (fractional_part * 1.0) / 10 ** self.max_decimals

def main():
  d1 = DiscreteNumberGenerator(max=5, min=100, allow_zero=True)
  print d1.run()

  f1 = FractionGenerator(
    numerator=DiscreteNumberGenerator(min=4, max=15),
    denominator=DiscreteNumberGenerator(min=10, max=100, allow_zero=False, allow_mixed=False)
  )

  print f1.run()

  f2 = FractionGenerator(
    numerator=DecimalGenerator(max_decimals=2, min=10, max=50),
    denominator=DiscreteNumberGenerator(min=10, max=100, allow_zero=False, allow_mixed=False)
  )

  print f2.run()

  d1 = DecimalGenerator(max_decimals=4, max=50, min=-20)
  print d1.run()

main()
