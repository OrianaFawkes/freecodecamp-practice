# Scientific Computing with Python Project 1
# Made by Oriana Fawkes '24

import re

def arithmetic_arranger(problems, display_answers = False):
    # Note: Error checking limited to instruction details

    # Error Checking Start #
    # Error 1: Too many problems (more than 5) supplied to the function
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        # Error 2: Operators are not addition or subtraction
        if re.search('[*/]', problem):
            return "Error: Operator must be '+' or '-'."

        # Error 3: Operand does not contain only digits
        operand = re.split(' [+-] ', problem)
        if re.search(r'[\D+]', operand[0]) or re.search(r'[\D+]', operand[1]):
            return "Error: Numbers must only contain digits."
    
        # Error 4: Operand has more than four digits in width
        if 4 < len(operand[0]) or 4 < len(operand[1]):
            return "Error: Numbers cannot be more than four digits."
    # Error Checking Stop #
        
    arranged_problems = ''
    augend_list = []
    addend_list = []
    line_list = []
    sum_list = []
    
    for problem in problems:
        augend = ''
        addend = ''
        line = ''
        sum_space = ''
        width = (2 + len(problem.split(' ')[0]) 
                if len(problem.split(' ')[0]) > len(problem.split(' ')[-1]) 
                else 2 + len(problem.split(' ')[-1]))
        sum = (int(problem.split(' ')[0]) + int(problem.split(' ')[-1]) 
                if problem.split(' ')[1] == '+' 
                else int(problem.split(' ')[0]) - int(problem.split(' ')[-1]))
        
        # Augend with right formatting 
        for _ in range(width - len(problem.split(' ')[0])):
            augend += ' '
        augend_list.append(augend + problem.split(' ')[0])
        
        # Operand and Addend with right formatting
        addend += problem.split(' ')[1]
        for _ in range(width - len(problem.split(' ')[-1]) - 1):
            addend += ' '
        addend_list.append(addend + problem.split(' ')[-1])
        
        # Correct number of dashes 
        for _ in range(width):
            line += '-'
        line_list.append(line)
        
        # Sum with right formatting
        for _ in range(width - len(str(sum))):
            sum_space += ' '
        sum_list.append(sum_space + str(sum))

    arranged_problems += '    '.join(augend_list) + '\n'
    arranged_problems += '    '.join(addend_list) + '\n'
    arranged_problems += '    '.join(line_list)
    if display_answers:
        arranged_problems += '\n' + '    '.join(sum_list)
    
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))