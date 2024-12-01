// Replace with your Django backend API endpoint
const API_URL = "http://127.0.0.1:8000/chat/";

document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keydown", function (e) {
    if (e.key === "Enter") sendMessage();
});

function sendMessage() {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    // Add user message to chat
    addMessageToChat(userInput, "user-message");
    document.getElementById("user-input").value = "";

    // Fetch response from Django backend
    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.response || "Sorry, I didn't understand that.";
            addMessageToChat(botResponse, "bot-message");
        })
        .catch(error => {
            console.error("Error:", error);
            addMessageToChat("An error occurred while connecting to the bot.", "bot-message");
        });
}

function addMessageToChat(message, className) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.className = `message ${className}`;
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
}
