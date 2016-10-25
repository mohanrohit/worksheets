end = 0

from p import BinaryOperationsProblemGenerator
from g import DiscreteNumberGenerator, FractionGenerator, OperatorGenerator
from f import formatters

def main1():
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

  o1 = OperatorGenerator(operators=["+", "-"])
  print o1.run()

  b1 = BinaryOperationsProblemGenerator(
    numbers=DiscreteNumberGenerator(min=-40, max=40),
    operators=OperatorGenerator(operators=["+","-", "*", "/"])
  )

  print b1.run()
end

def format(problem, formatter_type):
  operand1 = problem[0]
  operand1_formatter = formatters[operand1.__class__.__name__][formatter_type]
  
  operand2 = problem[2]
  operand2_formatter = formatters[operand2.__class__.__name__][formatter_type]

  return operand1_formatter().format(operand1) + problem[1] + operand2_formatter().format(operand2)

def main():
  b = BinaryOperationsProblemGenerator(
    count=5,
    operand1=FractionGenerator(min=1, max=10, allow_mixed=False),
    operand2=DiscreteNumberGenerator(min=0, max=50),
    operators=OperatorGenerator(operators=["*"])
  )

  problems = b.run()

  for p in problems:
    print format(p, "latex")
  end
end

main()
