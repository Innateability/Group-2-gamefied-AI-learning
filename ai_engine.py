# ai_engine.py

def choose_topic(user):
    _, level, _, _, weak = user

    # If weak topic exists → prioritize it
    if weak:
        return weak

    # Otherwise mix topics
    return "math" if level < 3 else "english"


def update_weak_topic(user, topic, correct):
    user_id, level, xp, streak, weak = user

    if not correct:
        return topic
    return ""


# 🔥 NEW: Placement evaluation
def evaluate_user_performance(history):
    """
    history = [{"topic": "math", "correct": True}, ...]
    """
    topic_scores = {}

    for item in history:
        topic = item["topic"]
        topic_scores.setdefault(topic, []).append(item["correct"])

    weak_topics = []

    for topic, results in topic_scores.items():
        accuracy = sum(results) / len(results)
        if accuracy < 0.6:
            weak_topics.append(topic)

    return weak_topics