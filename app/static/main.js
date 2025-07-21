const editor = document.getElementById("editor");
const socket = new WebSocket(`ws://${location.host}/ws/editor`);

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
});
