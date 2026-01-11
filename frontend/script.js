// script.js - frontend logic for AI Climate Action Advisor

const activityEl = document.getElementById("activity");
const analyzeBtn = document.getElementById("analyze");
const resultEl = document.getElementById("result");

analyzeBtn.addEventListener("click", async () => {
  const activity = activityEl.value.trim();

  if (!activity) {
    resultEl.textContent = "❗ Please enter an activity.";
    return;
  }

  analyzeBtn.disabled = true;
  resultEl.textContent = "🔍 Analyzing...";

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ activity })
    });

    const data = await response.json();

    if (!response.ok || data.error) {
      resultEl.textContent = "❌ Error: " + (data.error || "Something went wrong");
      analyzeBtn.disabled = false;
      return;
    }

    // -------------------------
    // DISPLAY RESULT (CORRECTLY)
    // -------------------------
    let output = "";
    output += `Category: ${data.category}\n`;
    output += `Impact: ${data.impact}\n`;
    output += `Carbon Footprint: ${data.carbon_footprint}\n`;
    output += `Suggestions:\n`;

    if (Array.isArray(data.suggestions)) {
      data.suggestions.forEach(s => {
        output += `- ${s}\n`;
      });
    } else {
      output += "- No suggestions available\n";
    }

    output += `Confidence: ${data.confidence}\n`;

    resultEl.textContent = output;

  } catch (err) {
    resultEl.textContent = "❌ Network error. Backend not reachable.";
  } finally {
    analyzeBtn.disabled = false;
  }
});
