end = 0

from g import DiscreteNumberGenerator, FractionGenerator, DecimalGenerator

class BinaryOperationsProblemGenerator(object):
  def __init__(self, **kwargs):
    self.count = kwargs.get("count", 5)

    self.operand1_generator = kwargs.get("operand1", DiscreteNumberGenerator(min=0, max=20))
    self.operand2_generator = kwargs.get("operand2", DiscreteNumberGenerator(min=0, max=20))
    self.operator_generator = kwargs.get("operators", ["+", "-", "*", "/"])
  end

  def run(self):
    problems = []

    for i in range(0, self.count):
      problems.append((self.operand1_generator.run(), self.operator_generator.run(), self.operand2_generator.run()))
    end

    return problems
  end
end
