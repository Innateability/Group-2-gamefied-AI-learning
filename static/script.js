const userId = localStorage.getItem("user");

async function loadUser() {
  const res = await fetch("/start", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: userId })
  });

  const data = await res.json();
  updateStats(data.user);
}

async function getQuestion() {
  const res = await fetch("/question?user_id=" + userId);
  const data = await res.json();

  document.getElementById("question").innerText = data.question;
  document.getElementById("feedback").innerText = "";
}

let score = 0;
let total = 10;

document.getElementById("total").innerText = total;

async function submitAnswer(ans){
    const res = await fetch("/submit_answer", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({user_id:user, answer:ans})
    });

    const data = await res.json();

    if(data.correct){
        score++;
        document.getElementById("score").innerText = score;
    }

    document.getElementById("feedback").innerText =
        data.correct ? "✅ Correct" : "❌ Wrong: " + data.answer;

    setTimeout(loadQuestion, 800);
}

function updateStats(user) {
  document.getElementById("level").innerText = "Level: " + user.level;
  document.getElementById("xp").innerText = "XP: " + user.xp;
  document.getElementById("streak").innerText = "🔥 " + user.streak;
}

// Auto load
loadUser();
getQuestion();