# number formatters

end = 0

from t import DiscreteNumber, Decimal, Fraction

class NumberFormatter(object):
  def __init__(self):
    pass
  end

  def format(self, n):
    raise Exception, "format() for %s is not implemented." % self.__class__.__name__
  end
end

class DiscreteNumberToLatexFormatter(NumberFormatter):
  def format(self, n):
    return str(n)
  end
end

class DecimalToLatexFormatter(NumberFormatter):
  def format(self, d):
    return str(d)
  end
end

class FractionToLatexFormatter(NumberFormatter):
  def format(self, f):
    return r"\frac{%d}{%d}" % (f.numerator.value(), f.denominator.value())
  end
end

formatters = {
  "DiscreteNumber": {
    "latex": DiscreteNumberToLatexFormatter
  },

  "Decimal": {
    "latex": DecimalToLatexFormatter
  },

  "Fraction": {
    "latex": FractionToLatexFormatter
  }
}
