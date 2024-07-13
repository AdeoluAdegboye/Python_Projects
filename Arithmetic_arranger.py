def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Incorrect problem format.'

        first_num, operator, second_num = parts
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not first_num.isdigit() or not second_num.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(first_num) > 4 or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if operator == '+':
            answer = str(int(first_num) + int(second_num))
        else:
            answer = str(int(first_num) - int(second_num))

        width = max(len(first_num), len(second_num)) + 2
        first_line.append(first_num.rjust(width))
        second_line.append(operator + second_num.rjust(width - 1))
        dashes.append('-' * width)
        answers.append(answer.rjust(width))

    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    if display_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems
    
      
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],  True)}')
