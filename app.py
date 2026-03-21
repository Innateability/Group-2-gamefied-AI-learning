from flask import Flask, request, jsonify, render_template
import random
from database import create_tables

app = Flask(__name__)
create_tables()

# -----------------------
# QUESTION BANK (USE YOUR FULL ONE HERE)
# -----------------------
from content import question_bank

sessions = {}

# -----------------------
# SELECT 1 QUESTION PER TOPIC
# -----------------------
def select_placement_questions():
    selected = []

    for topic, subtopics in question_bank.items():
        subtopic = random.choice(list(subtopics.keys()))
        q, ans, options = random.choice(subtopics[subtopic])

        random.shuffle(options)

        selected.append({
            "topic": topic,
            "subtopic": subtopic,
            "question": q,
            "answer": ans,
            "options": options
        })

    return selected

# -----------------------
# STUDY PLAN
# -----------------------
# def generate_study_plan(weak):
#     plan = {f"Week {i}": [] for i in range(1, 9)}

#     week = 1
#     for topic in weak:
#         for sub in weak[topic]:
#             plan[f"Week {week}"].append(f"{topic} - {sub}")
#             week = week + 1 if week < 8 else 1

#     return plan

import random

def generate_study_plan(weak_subtopics):
    """
    Generate a 2-month (10-lesson) personalized plan:
    - Split weak topics into part 1 & part 2
    - Fill remaining lessons with default topics
    - Shuffle the order while keeping sequential numbering
    """

    # Step 1: Flatten weak topics into part 1 & part 2
    weak_lessons = []
    for topic, subs in weak_subtopics.items():
        for sub in subs:
            weak_lessons.append(f"{topic} - {sub} (Part 1)")
            weak_lessons.append(f"{topic} - {sub} (Part 2)")

    # Step 2: Define default lessons similar to normal topics
    default_lessons = [
        "AI Basics - Components",
        "AI Basics - Introduction",
        "Agents - Agent Structure",
        "Agents - Agent Concepts",
        "Search - Search Techniques",
        "Search - Search Basics",
        "Problem Solving - Concepts",
        "Expert Systems - Components",
        "Expert Systems - Basics",
        "Ethics - Issues"
    ]

    # Step 3: Fill remaining lessons to reach 10
    total_lessons = 10
    lessons_needed = total_lessons - len(weak_lessons)
    if lessons_needed > 0:
        weak_lessons.extend(random.sample(default_lessons, lessons_needed))

    # Step 4: Shuffle lessons randomly but maintain sequential order
    random.shuffle(weak_lessons)

    # Step 5: Arrange into 8 weeks (or 10 lessons sequentially)
    plan = {}
    week = 1
    for idx, lesson in enumerate(weak_lessons):
        week_name = f"Week {week}"
        if week_name not in plan:
            plan[week_name] = []
        plan[week_name].append(lesson)
        week = week + 1 if week < 8 else 1

    return plan

# -----------------------
# ROUTES
# -----------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/start", methods=["POST"])
def start():
    user_id = request.json["user_id"]

    sessions[user_id] = {
        "questions": select_placement_questions(),
        "index": 0,
        "score": 0,
        "weak": {}
    }

    return jsonify({"total": len(sessions[user_id]["questions"])})

@app.route("/next")
def next_q():
    user_id = request.args.get("user_id")
    session = sessions[user_id]

    if session["index"] >= len(session["questions"]):
        return jsonify({
            "done": True,
            "score": session["score"],
            "plan": generate_study_plan(session["weak"])
        })

    q = session["questions"][session["index"]]

    return jsonify({
        "done": False,
        "topic": q["topic"],
        "subtopic": q["subtopic"],
        "question": q["question"],
        "options": q["options"]
    })

@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    user_id = data["user_id"]
    ans = data["answer"]

    session = sessions[user_id]
    q = session["questions"][session["index"]]

    correct = ans.lower() == q["answer"].lower()

    if correct:
        session["score"] += 1
    else:
        session["weak"].setdefault(q["topic"], []).append(q["subtopic"])

    session["index"] += 1

    return jsonify({
        "correct": correct,
        "answer": q["answer"],
        "score": session["score"]
    })

@app.route("/study_plan")
def study_plan():
    user_id = request.args.get("user_id")
    session_data = sessions.get(user_id)
    if not session_data:
        return "Session not found", 404

    # Use the same 'weak' dictionary you already store in session
    weak_subtopics = session_data.get("weak", {})

    # Generate study plan (can handle empty weak_subtopics)
    study_plan_data = generate_study_plan(weak_subtopics)

    return render_template("study_plan.html", plan=study_plan_data)

if __name__ == "__main__":
    app.run(debug=True)