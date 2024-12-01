// Replace with your Django backend API endpoint
const API_URL = "http://127.0.0.1:8000/chat/";

const sendButton = document.getElementById("send-btn");
const userInputField = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

// Add event listeners
sendButton.addEventListener("click", sendMessage);
userInputField.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && userInputField.value.trim()) {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = userInputField.value.trim();
    if (!userInput) return;

    // Add user message to chat
    addMessageToChat(userInput, "user-message");
    userInputField.value = "";

    // Show typing indicator
    const typingIndicator = addMessageToChat("Typing...", "bot-message");

    // Disable send button to prevent spamming
    sendButton.disabled = true;

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
            typingIndicator.remove(); // Remove typing indicator
            addMessageToChat(botResponse, "bot-message");
        })
        .catch(error => {
            console.error("Error:", error);
            typingIndicator.remove(); // Remove typing indicator
            addMessageToChat("An error occurred while connecting to the bot. Please try again later.", "bot-message");
        })
        .finally(() => {
            sendButton.disabled = false; // Re-enable send button
        });
}

function addMessageToChat(message, className) {
    const messageElement = document.createElement("div");
    messageElement.className = `message ${className}`;
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
    return messageElement; // Return the created element (useful for typing indicators)
}
