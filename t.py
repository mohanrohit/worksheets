# number types

end = 0

class Number(object):
  def __init__(self):
    pass
  end

  def value(self):
    raise Exception, "value() for %s is not implemented." % self.__class__.__name__
  end
end

class DiscreteNumber(Number):
  def __init__(self, n):
    self.n = n
  end

  def value(self):
    return self.n
  end

  def __repr__(self):
    return str(self.n)
  end
end

class Fraction(Number):
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
  end

  def value(self):
    return (self.numerator, self.denominator)
  end

  def __repr__(self):
    return str(self.numerator) + "/" + str(self.denominator)
end

class Decimal(Number):
  def __init__(self, d):
    self.d = d
  end

  def value(self):
    return self.d
  end

  def __repr__(self):
    return str(self.d)
end
