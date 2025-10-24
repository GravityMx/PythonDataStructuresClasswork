
from PostFixMathProgram.PostFixEvaluation import PostFixEvaluation

from PostFixMathProgram.InFixToPostFixConvertor import InFixToPostFixConvertor



test = "1 4 3 - +"

print(test, " = ", PostFixEvaluation(test))

test2 = "2 * ( 3 + 5 )"

print(test2, " = ", InFixToPostFixConvertor(test2), " = ", PostFixEvaluation(InFixToPostFixConvertor(test2)))

test3 = "9 + ( ( 2 - 4 ) / 6 ) + 4 / 2"

print(test3, " = ", InFixToPostFixConvertor(test3), " = ", PostFixEvaluation(InFixToPostFixConvertor(test3)))

