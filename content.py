import random

questions = {
    "math": [
        ("2 + 2", "4"),
        ("5 * 3", "15"),
        ("10 - 6", "4")
    ],
    "english": [
        ("Synonym of 'big'", "large"),
        ("Opposite of 'hot'", "cold")
    ]
}

def get_question(topic):
    return random.choice(questions[topic])