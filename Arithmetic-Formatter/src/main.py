def calculate(num1, num2, operator):
    num1 = int(num1)
    num2 = int(num2)
    if operator == "+":
        return str(num1 + num2)
    elif operator == "-":
        return str(num1 - num2)

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_number_line = ""
    second_number_line = ""
    separation_line = ""
    result_line = ""

    for i, problem in enumerate(problems):
        parts = problem.split()
        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(num1), len(num2)) + 2
        top = num1.rjust(length)
        bottom = operator + num2.rjust(length - 1)
        line = '-' * length
        result = calculate(num1, num2, operator).rjust(length)

        if i > 0:
            first_number_line += " " * 4 + top
            second_number_line += " " * 4 + bottom
            separation_line += " " * 4 + line
            result_line += " " * 4 + result
        else:
            first_number_line = top
            second_number_line = bottom
            separation_line = line
            result_line = result

    if show_answers:
        return f"{first_number_line}\n{second_number_line}\n{separation_line}\n{result_line}"
    else:
        return f"{first_number_line}\n{second_number_line}\n{separation_line}"

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))