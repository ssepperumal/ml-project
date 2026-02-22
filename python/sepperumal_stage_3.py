def calculate_grade(name, m1, m2, m3):
    total = m1 + m2 + m3
    percentage = (total / 300) * 100
    
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"
    
    print(name)
    print(f"Total: {total}/300")
    print(f"Percentage: {percentage}%")
    print(f"Grade: {grade}")

calculate_grade("Rajkumar", 80, 70, 90)
