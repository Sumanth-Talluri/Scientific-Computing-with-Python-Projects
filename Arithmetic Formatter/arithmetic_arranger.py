def arithmetic_arranger(problems, print_ans = False):
  count = 1

  if len(problems)>5:
    return "Error: Too many problems."
  
  line_1 = ""
  line_2 = ""
  dash_line = ""
  ans_line = ""

  for problem in problems:

    chars = problem.split()

    try :
      num1 = int(chars[0])
      operator = chars[1]
      num2 = int(chars[2])
    except :
      return "Error: Numbers must only contain digits."

    if len(chars[0])>4 or len(chars[2])>4 :
      return "Error: Numbers cannot be more than four digits."

    if chars[1] not in ["+", "-"]:
        return "Error: Operator must be '+' or '-'." 

    if print_ans:
      if operator == "+":
        answer = num1 + num2
      else:
        answer = num1 - num2

    maxx = num1
    if num2>num1:
      maxx = num2

    str_num1 = str(num1).rjust(len(str(maxx))+2)
    str_num2 = operator + str(num2).rjust(len(str(maxx))+1)

    line_1 = line_1 + str_num1
    line_2 = line_2 + str_num2
    dash_line = dash_line + ("-"*(2+len(str(maxx))))

    

    if print_ans:
      ans_line = ans_line + str(answer).rjust(len(str(maxx))+2)

    if count<len(problems) :
      line_1 += "    "
      line_2 += "    "
      dash_line += "    "
      if print_ans:
        ans_line += "    "

    count += 1
  
  if print_ans:
    arranged_problems = line_1 + "\n" + line_2 + "\n" + dash_line + "\n" + ans_line
  else:
    arranged_problems = line_1 + "\n" + line_2 + "\n" + dash_line

  return arranged_problems