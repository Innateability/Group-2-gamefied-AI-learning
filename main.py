from database import create_tables
from user_model import get_user, update_user
from gamification import add_xp
from content import get_question
from ai_engine import choose_topic, update_weak_topic

def run():
    create_tables()

    user_id = input("Enter your name: ")
    user = get_user(user_id)

    while True:
        topic = choose_topic(user)
        question, answer = get_question(topic)

        print(f"\n[Level {user[1]} | Topic: {topic}]")
        print("Question:", question)

        user_answer = input("Your answer: ")

        correct = user_answer.strip().lower() == answer.lower()

        if correct:
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! Answer: {answer}")

        xp, level, streak = add_xp(user, correct)
        weak = update_weak_topic(user, topic, correct)

        update_user(user_id, xp, level, streak, weak)
        user = (user_id, level, xp, streak, weak)

        print(f"XP: {xp} | Level: {level} | Streak: {streak}")

        cont = input("Continue? (y/n): ")
        if cont.lower() != "y":
            break


if __name__ == "__main__":
    run()