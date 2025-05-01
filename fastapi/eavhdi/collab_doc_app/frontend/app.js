let socket;
let editor = document.getElementById("editor");

function connectDoc() {
    const id = document.getElementById("docIdInput").value;
    fetch(`http://localhost:8000/documents/${id}`)
        .then(res => res.json())
        .then(data => {
            editor.value = data.content;
            socket = new WebSocket(`ws://localhost:8000/ws/documents/${id}`);
            // socket = new WebSocket('ws://localhost:8000/ws/documents/' + id);
            socket.onmessage = event => editor.value = event.data;
            editor.oninput = () => socket.send(editor.value);
        });
}

function createDoc() {
    fetch("http://localhost:8000/documents", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            document.getElementById("docIdInput").value = data.id;
            connectDoc();
        });
}
