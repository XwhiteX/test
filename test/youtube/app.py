from Question import Question

question_prompts = [
    "what color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "what color are apples1?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "what color are apples2?\n(a) Red\n(b) Purple\n(c) Orange\n\n"
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'a'),
    Question(question_prompts[2], 'a')
]


def run_test(questions):
    score = 0
    for quesiton in questions:
        answer = input(quesiton.prompt)
        if answer == quesiton.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(questions)



