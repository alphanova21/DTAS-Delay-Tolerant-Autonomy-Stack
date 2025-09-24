const BASE = "http://127.0.0.1:5000/rover";

// --- Batch Commands ---
async function sendCommands() {
  const commands = document.getElementById("commands").value
    .split("\n").map(s => s.trim()).filter(Boolean);
  const res = await fetch(${BASE}/execute, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({commands})
  });
  const data = await res.json();
  document.getElementById("commandOutput").innerText = JSON.stringify(data, null, 2);
}

// --- Anomaly Detection ---
async function detectAnomaly() {
  try {
    const payload = JSON.parse(document.getElementById("anomalyInput").value);
    const res = await fetch(${BASE}/anomaly, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById("anomalyOutput").innerText = JSON.stringify(data, null, 2);
  } catch (e) {
    alert("Invalid JSON in anomaly input");
  }
}

// --- Predict Action (ML) ---
async function predictAction() {
  try {
    const payload = JSON.parse(document.getElementById("predictInput").value);
    const res = await fetch(${BASE}/predict, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById("predictOutput").innerText = JSON.stringify(data, null, 2);
  } catch (e) {
    alert("Invalid JSON in predict input");
  }
}

// --- Train Model ---
async function trainModel() {
  const res = await fetch(${BASE}/learn, {method: "POST"});
  const data = await res.json();
  document.getElementById("trainOutput").innerText = JSON.stringify(data, null, 2);
}