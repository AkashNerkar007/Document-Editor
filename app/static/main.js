const editor = document.getElementById("editor");
const socketProtocol = location.protocol === "https:" ? "wss:" : "ws:";
const socket = new WebSocket(`${socketProtocol}//${location.host}/ws/editor`);
const suggestionBox = document.getElementById("suggestion");
let skipBroadcast = false;

socket.onmessage = (event) => {
  skipBroadcast = true;
  editor.value = event.data;
};

editor.addEventListener("input", () => {
  if (!skipBroadcast) {
    socket.send(editor.value);
  }
  skipBroadcast = false;
  getSuggestion();
});

function getSuggestion() {
  const formData = new FormData();
  formData.append("text", editor.value);

  fetch("/suggest", {
    method: "POST",
    body: formData
  })
  .then(res => {
    if (!res.ok) {
      throw new Error("Network response was not ok");
    }
    return res.json();
  })
  .then(data => {
    suggestionBox.innerText = data.suggestion || "No suggestion available.";
  })
  .catch(err => {
    suggestionBox.innerText = "⚠️ Unable to get suggestion.";
    console.error("Suggestion error:", err);
  });
}
