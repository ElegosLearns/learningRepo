#take in: arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
#put out "   "32      3801      45      123" \n "+ 698    -    2    + 43    +  49" \n "_____    ______    ____    _____" "
import re

def arithmetic_arranger(problems, answers=False):
    
  #create placeholders for end solution
  line_1 = ""
  line_2 = ""
  line_3 = ""
  answer = ""
  combined_string = ""

  #error check 1
  if (len(problems)>5):
    return "Error: Too many problems."
  #error check 2 & 3
  for problem in problems:
    if(re.search("[*/]", problem)):
      return "Error: Operator must be '+' or '-'."
    if(re.search("[^\s0-9.+-]", problem)):
      return "Error: Numbers must only contain digits."
      
    #seperate each operand and the operator
    operand_a = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    operand_b = problem.split(" ")[2]
    
    #error check 4
    if (len(operand_a) > 4 or len(operand_b) > 4):
      return "Error: Numbers cannot be more than four digits."

    #determine answers based on operator
    solution = ""
    if operator == '+':
      solution = int(operand_a) + int(operand_b)
    elif operator == '-':
      solution = int(operand_a) - int(operand_b)

    #prepare data to be right aligned
    digits = max(len(operand_a), len(operand_b))
    num_1 = str(operand_a).rjust(digits+2)
    num_2 = operator + str(operand_b).rjust(digits+1)
    underline = "-" * (digits + 2)
    underline_rj = underline.rjust(digits)
    solution_rj = str(solution).rjust(digits + 2)

    #format 4 spaces between each problem
    if problem != problems[-1]:
      line_1 += num_1 + "    "
      line_2 += num_2 + "    "
      line_3 += underline_rj + "    "
      answer += solution_rj + "    "
    #do not include spaces at the end of the last problem
    else:
      line_1 += num_1
      line_2 += num_2
      line_3 += underline_rj
      answer += solution_rj

  #put necesarry information into placeholders depending on optional argument
  if answers != True:
    combined_string = line_1 + "\n" + line_2 + "\n" + line_3
  else:
    combined_string = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + answer

  #return formatted problems
  return combined_string