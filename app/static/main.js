const editor = document.getElementById("editor");
const socket = new WebSocket(`ws://${location.host}/ws/editor`);
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

  // 🔥 Trigger suggestion on every keystroke
  getSuggestion();
});

function getSuggestion() {
  const formData = new FormData();
  formData.append("text", editor.value);

  fetch("/suggest", {
    method: "POST",
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    suggestionBox.innerText = data.suggestion;
  })
  .catch(err => {
    suggestionBox.innerText = "Error getting suggestion.";
    console.error(err);
  });
}
