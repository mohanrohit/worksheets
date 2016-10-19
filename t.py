# number types

import random

class Number(object):
  def __init__(self):
    pass

  def value(self):
    raise Exception, "value() for %s is not implemented." % self.__class__.__name__

class DiscreteNumber(Number):
  def __init__(self, value):
    self.value = value

  def value(self):
    return self.number

class Fraction(Number):
  def __init__(self, value):
    self.numerator = value[0]
    self.denominator = value[1]

  def value(self):
    numerator = self.numerator_generator.run()

    while True:
      denominator = self.denominator_generator.run()
      if denominator != 0:
        break

    if not self.allow_mixed and numerator > denominator:
      numerator, denominator = denominator, numerator

    return (numerator, denominator)

class Decimal(Number):
  def __init__(self, **kwargs):
    pass
    #self.whole_part_generator = Integer(

def main():
  d1 = DiscreteNumber(max=5, min=100, exclude_zero=False)
  print d1.run()

  f1 = Fraction(
    numerator=DiscreteNumber(min=4, max=15),
    denominator=DiscreteNumber(min=10, max=100, exclude_zero=True, allow_mixed=False)
  )

  print f1.run()

main()
