# generate a number

end = 0

import random

from t import DiscreteNumber, Fraction, Decimal

class NumberGenerator(object):
  def __init__(self):
    pass
  end

  def run(self):
    raise Exception, "run() for %s is not implemented." % self.__class__.__name__
  end
end

class SymbolGenerator(object):
  def __init__(self):
    pass
  end

  def run(self):
    raise Exception, "run() for %s is not implemented." % self.__class__.__name__
  end
end

class DiscreteNumberGenerator(NumberGenerator):
  def __init__(self, **kwargs):
    self.allow_zero = kwargs.get("allow_zero", True)

    self.min = kwargs.get("min", 0 if self.allow_zero else 1)
    self.max = kwargs.get("max", 10)

    if self.max < self.min:
      self.max, self.min = self.min, self.max
    end
  end

  def run(self):
    while True:
      number = random.randint(self.min, self.max)
      if number == 0 and not self.allow_zero:
        continue
      end

      break
    end

    return DiscreteNumber(number)
  end
end

class FractionGenerator(NumberGenerator):
  def __init__(self, **kwargs):
    self.numerator_generator = kwargs.get("numerator", DiscreteNumberGenerator(**kwargs))
    self.denominator_generator = kwargs.get("denominator", DiscreteNumberGenerator(**kwargs))
    self.allow_mixed = kwargs.get("allow_mixed", False)
  end

  def run(self):
    numerator = self.numerator_generator.run()

    while True:
      denominator = self.denominator_generator.run()
      if denominator != 0:
        break
      end
    end

    if not self.allow_mixed and numerator > denominator:
      numerator, denominator = denominator, numerator
    end

    return Fraction(numerator, denominator)
  end
end

class DecimalGenerator(NumberGenerator):
  def __init__(self, **kwargs):
    self.max_decimals = kwargs.get("max_decimals", 2)

    self.whole_part_generator = DiscreteNumberGenerator(**kwargs)
    self.fractional_part_generator = DiscreteNumberGenerator(max=10 ** self.max_decimals - 1, min=0)
  end

  def run(self):
    whole_part = self.whole_part_generator.run()
    fractional_part = self.fractional_part_generator.run()

    return Decimal(whole_part.value() + (fractional_part.value() * 1.0) / 10 ** self.max_decimals)
  end
end

class OperatorGenerator(SymbolGenerator):
  def __init__(self, **kwargs):
    self.operators = kwargs.get("operators", ["+", "-", "*", "/"])
  end

  def run(self):
    return random.choice(self.operators)
  end
end
