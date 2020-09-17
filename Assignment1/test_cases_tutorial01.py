import tutorial01 as A1

actual_answers = [9, 6, 28, 7, 4, [2, 6, 18, 54, 162], [2, 5, 8, 11, 14], [0.2, 0.1, 0.067, 0.05, 0.04]]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(8, 2)
student_answers.append(test_case_2)

test_case_3 = A1.multiply(14, 2)
student_answers.append(test_case_3)

test_case_4 = A1.divide(14, 2)
student_answers.append(test_case_4)

test_case_5 = A1.power(2, 2)
student_answers.append(test_case_5)

test_case_6 = A1.printGP(2,3,5)
student_answers.append(test_case_6)

test_case_7 = A1.printAP(2,3,5)
student_answers.append(test_case_7)

test_case_8 = A1.printHP(0.2,5,5)
student_answers.append(test_case_8)

print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
