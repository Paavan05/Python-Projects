import random, time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + operator + str(right)
    answer = eval(expr)
    return expr, answer

input("Press Enter to start")
print("---------------")

wrong_answer = 0
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    
    while True:
        guess = input(f"Problem #{i+1}: {expr} = ")
        
        if guess == str(answer):
            break
        wrong_answer += 1
    
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------")
print(f"You finished in {total_time} seconds with {wrong_answer} wrong answers.")