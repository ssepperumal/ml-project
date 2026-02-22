def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Zero Division Error"
        else:
            result = num1 / num2
    else:
        result = "Error: Invalid operator."
    
    return result

print(calculator(10, 5, '+'))   
  
