from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# -----------------------
# Question Bank (10 topics × 4 subtopics each, MCQs)
# -----------------------
question_bank = {
    "Algebra": {
        "Equations": [
            ("Solve x + 3 = 7", "4", ["2","4","5","3"]),
            ("Solve 2x = 10", "5", ["5","2","10","6"])
        ],
        "Inequalities": [
            ("Solve x - 5 > 2", "8", ["6","7","8","9"]),
            ("Solve 2x + 1 < 7", "3", ["2","3","4","5"])
        ],
        "Polynomials": [
            ("Simplify x^2 + 2x + x^2", "2x^2+2x", ["x^2+2x","2x^2+2x","x^2+2x^2","2x^2+x"])
        ],
        "Factoring": [
            ("Factor x^2+5x+6", "(x+2)(x+3)", ["(x+2)(x+3)","(x+1)(x+6)","(x+3)(x+3)","(x+2)(x+2)"])
        ]
    },
    "Geometry": {
        "Angles": [
            ("Sum of angles in a triangle?", "180", ["90","180","360","270"])
        ],
        "Triangles": [
            ("Right triangle sides 3,4,?", "5", ["5","6","7","4"])
        ],
        "Circles": [
            ("Radius 5, area?", "78.5", ["25","50","78.5","100"])
        ],
        "Area": [
            ("Area rectangle 4x5", "20", ["9","20","10","15"])
        ]
    },
    "Arithmetic": {
        "Addition": [
            ("5 + 7 = ?", "12", ["10","12","11","13"])
        ],
        "Subtraction": [
            ("10 - 3 = ?", "7", ["7","6","8","5"])
        ],
        "Multiplication": [
            ("4 × 6 = ?", "24", ["24","20","26","28"])
        ],
        "Division": [
            ("12 ÷ 3 = ?", "4", ["3","4","5","6"])
        ]
    },
    "Number Theory": {
        "Prime Numbers": [
            ("Next prime after 7?", "11", ["9","10","11","13"])
        ],
        "Factors": [
            ("Factors of 12?", "1,2,3,4,6,12", ["1,2,3,4,6,12","2,3,6,12","1,2,4,8","1,3,6,12"])
        ],
        "Multiples": [
            ("Multiples of 3 under 10?", "3,6,9", ["3,6,9","3,6,9,12","6,9,12","3,6"])
        ],
        "GCD": [
            ("GCD of 8 and 12?", "4", ["2","4","6","8"])
        ]
    },
    "Fractions": {
        "Simplifying": [
            ("Simplify 8/12", "2/3", ["2/3","3/4","4/6","1/2"])
        ],
        "Addition": [
            ("1/2 + 1/3", "5/6", ["2/5","5/6","3/5","1/3"])
        ],
        "Subtraction": [
            ("3/4 - 1/2", "1/4", ["1/4","1/2","2/4","1/3"])
        ],
        "Multiplication": [
            ("2/3 × 3/4", "1/2", ["1/2","2/3","3/4","1/3"])
        ]
    },
    "Decimals": {
        "Addition": [
            ("0.5 + 0.75", "1.25", ["1.25","1.15","1.35","1.05"])
        ],
        "Subtraction": [
            ("1.2 - 0.7", "0.5", ["0.6","0.5","0.7","0.4"])
        ],
        "Multiplication": [
            ("0.4 × 0.5", "0.2", ["0.2","0.3","0.4","0.1"])
        ],
        "Division": [
            ("0.6 ÷ 0.2", "3", ["2","3","4","5"])
        ]
    },
    "Percentages": {
        "Basics": [
            ("What is 50% of 200?", "100", ["100","50","150","200"])
        ],
        "Increase": [
            ("Increase 80 by 25%", "100", ["100","95","105","110"])
        ],
        "Decrease": [
            ("Decrease 90 by 20%", "72", ["72","70","74","75"])
        ],
        "Word Problems": [
            ("10 is what % of 50?", "20", ["10","20","25","50"])
        ]
    },
    "Ratios & Proportions": {
        "Simplifying Ratios": [
            ("Simplify 4:8", "1:2", ["1:2","2:4","2:1","4:8"])
        ],
        "Equivalent Ratios": [
            ("2:3 = ? : 9", "6:9", ["6:9","3:9","4:9","5:9"])
        ],
        "Proportions": [
            ("If 2/3 = x/9, x = ?", "6", ["6","3","9","12"])
        ],
        "Word Problems": [
            ("A:B = 2:3, B=15, A=?", "10", ["10","12","15","20"])
        ]
    },
    "Algebra 2": {
        "Linear Equations": [
            ("Solve 3x + 4 = 10", "2", ["1","2","3","4"])
        ],
        "Quadratic Equations": [
            ("Solve x^2 - 5x + 6 = 0", "2", ["1","2","3","4"])
        ],
        "Functions": [
            ("f(x) = 2x, f(3)?", "6", ["5","6","7","8"])
        ],
        "Graphing": [
            ("Slope of line through (0,0) & (2,4)?", "2", ["1","2","4","0.5"])
        ]
    }
}

# -----------------------
# Sessions
# -----------------------
sessions = {}

# -----------------------
# Helpers
# -----------------------

def select_placement_questions():
    placement_questions = []
    for topic, subtopics in question_bank.items():
        for subtopic, questions in subtopics.items():
            q, ans, options = random.choice(questions)
            random.shuffle(options)
            placement_questions.append({
                "topic": topic,
                "subtopic": subtopic,
                "question": q,
                "answer": ans,
                "options": options
            })
    return placement_questions

def generate_study_plan(weak_subtopics):
    plan = {}
    weeks = 8
    for i in range(1, weeks+1):
        plan[f"Week {i}"] = []
    week_counter = 1
    for topic, subtopics in weak_subtopics.items():
        for subtopic in subtopics:
            plan[f"Week {week_counter}"].append({"topic": topic, "subtopic": subtopic})
            week_counter = (week_counter % weeks) + 1
    return plan

# -----------------------
# Routes
# -----------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game")
def game_page():
    return render_template("game.html")

@app.route("/start", methods=["POST"])
def start():
    user_id = request.json["user_id"]
    placement_questions = select_placement_questions()
    sessions[user_id] = {
        "questions": placement_questions,
        "current_index": 0,
        "weak_subtopics": {},
        "history": []
    }
    return jsonify({"message":"Placement test started","total":len(placement_questions)})

@app.route("/next_question")
def next_question():
    user_id = request.args.get("user_id")
    session = sessions.get(user_id)
    if not session:
        return jsonify({"error":"Session not found"}), 404

    if session["current_index"] >= len(session["questions"]):
        study_plan = generate_study_plan(session["weak_subtopics"])
        return jsonify({"done": True, "study_plan": study_plan})

    qdata = session["questions"][session["current_index"]]
    return jsonify({
        "done": False,
        "question": qdata["question"],
        "topic": qdata["topic"],
        "subtopic": qdata["subtopic"],
        "options": qdata["options"]
    })

@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    data = request.json
    user_id = data["user_id"]
    user_answer = data["answer"]

    session = sessions.get(user_id)
    if not session:
        return jsonify({"error":"Session not found"}), 404

    current_q = session["questions"][session["current_index"]]
    correct = user_answer.strip().lower() == current_q["answer"].strip().lower()

    if not correct:
        session["weak_subtopics"].setdefault(current_q["topic"], []).append(current_q["subtopic"])

    session["history"].append({
        "topic": current_q["topic"],
        "subtopic": current_q["subtopic"],
        "correct": correct
    })

    session["current_index"] += 1

    return jsonify({
        "correct": correct,
        "answer": current_q["answer"]
    })

if __name__ == "__main__":
    app.run(debug=True)