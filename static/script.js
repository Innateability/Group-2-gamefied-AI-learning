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

async function submitAnswer() {
  const answer = document.getElementById("answer").value;

  const res = await fetch("/answer", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: userId, answer })
  });

  const data = await res.json();

  document.getElementById("feedback").innerText = data.message;
  document.getElementById("answer").value = "";

  updateStats(data.user);
  getQuestion();
}

function updateStats(user) {
  document.getElementById("level").innerText = "Level: " + user.level;
  document.getElementById("xp").innerText = "XP: " + user.xp;
  document.getElementById("streak").innerText = "🔥 " + user.streak;
}

// Auto load
loadUser();
getQuestion();