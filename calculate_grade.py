#รับจำนวนวิชาที่จะคำนวณ
def get_order(prompt):
    while True:
        try:
            count = int(input(prompt))
            return count
        except ValueError:
            print("Please enter a number of subject! Enter an integer.")

#รับคะแนน
def get_score(prompt,min_value=0,max_value=100):
    while True:
        try:
            score = float(input(prompt))
            if min_value <= score <= max_value:
                return score
            else:
                print(f"Please enter a score between {min_value} and {max_value}:")
        except ValueError:
            print("Please enter a score as number only!")

#คำนวณเกรดออกมาเป็นเลข
def calculate_grade(score):
    if score > 100 or score < 0:
        return "error"
    elif score >= 80:
        return 4.0
    elif score >= 75:
        return 3.5
    elif score >= 70:
        return 3.0
    elif score >= 65:
        return 2.5
    elif score >= 60:
        return 2.0
    elif score >= 55:
        return 1.5
    elif score >= 50:
        return 1.0
    else:
        return 0.0

#แสดงผลลัพธ์จากการคำนวณ
def show_result(score,grade):
    print("-"*30)
    if grade == "error":
        print(f"Error {score} is impossible score!")
        print("Please enter scores between 0-100 only.")
    else:
        print(f'Your score is {score}')
        if grade == 4.0:
            print(f"Your grade is {grade}.")
            score_over_4 = score - 80
            if score_over_4 == 0:
                print("Very good.")
            else:
                print(f"Got enough points for grade {grade}, {score_over_4} points more than that.")
        elif grade != 0.0:
            print(f"Your grade is {grade}.")
            point_to_4 = 80 - score
            print(f"Another {point_to_4:2f} point will grade 4.")
        else:
            point_to_1 = 50 - score
            print(f"Another {point_to_1:2f} points will pass!")
        print("-" * 30)


#เปิดการทำงานของโปรแกรม
if __name__ == "__main__":
    print("Welcome to The Calculate Grade Generator!")

    count = get_order("How many subjects do you want to enter? ")
    for i in range(1, count + 1):
        prompt = f"Enter score for subject {i}: "
        user_score = get_score(prompt)
        final_grade = calculate_grade(user_score)
        show_result(user_score, final_grade)