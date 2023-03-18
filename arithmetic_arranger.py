def arithmetic_arranger(problems, show_results=False):
  # Check that there are no more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."

  # Create empty lists for the top numbers, bottom numbers, and dashes

  tops = ''
  bottoms = ''
  dashes = ''
  answers = ''

  # Split the problems into their individual components and check that they are valid
  for problem in problems:
    parts = (str(problem)).split()

    # Check that the problem has only two operands
    if len(parts) != 3:
      return "Error: Each problem must have two operands."

    #
    if len(parts[0]) > 4 or len(parts[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    # Check that the operands are valid integers
    if not parts[0].isdigit() or not parts[2].isdigit():
      return "Error: Numbers must only contain digits."

    # Check that the operator is valid
    if parts[1] != "+" and parts[1] != "-":
      return "Error: Operator must be '+' or '-'."

    top_num = parts[0]
    bottom_num = parts[2]
    op = parts[1]

    lenght = max(len(top_num), len(bottom_num)) + 2

    top = str(top_num).rjust(lenght)
    bottom = op + str(bottom_num).rjust(lenght - 1)
    dashe = '-' * lenght
    answer = ''
    if op == '+':
      answer = int(top_num) + int(bottom_num)
    else:
      answer = int(top_num) - int(bottom_num)
    answer = str(answer).rjust(lenght)

    #add values to the final string

    if problem != problems[-1]:
      tops += top + '    '
      bottoms += bottom + '    '
      dashes += dashe + '    '
      answers += answer + '    '
    else:
      tops = tops + top
      bottoms += bottom
      dashes += dashe
      answers += answer

  if show_results == False:
    arranged_problems = tops + '\n' + bottoms + '\n' + dashes
  else:
    arranged_problems = tops + '\n' + bottoms + '\n' + dashes + '\n' + answers
  return arranged_problems
