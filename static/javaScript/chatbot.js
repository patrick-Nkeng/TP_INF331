const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const historyList = document.getElementById('historyList');

let messageHistory = [];
let currentConversationId = Date.now();

const botResponses = {
    'bonjour': 'Bonjour ! Comment puis-je vous aider ?',
    'salut': 'Salut ! Que puis-je faire pour vous ?',
    'au revoir': 'Au revoir ! Passez une excellente journée !',
    'merci': 'Je vous en prie ! N\'hésitez pas si vous avez d\'autres questions.',
    'default': 'Je suis désolé, je ne comprends pas. Pourriez-vous reformuler votre question ?'
};

function formatDate(date) {
    return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`;
}

function startNewChat() {
    currentConversationId = Date.now();
    messageHistory.push({
        message: "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
        timestamp: new Date(),
        isUser: false,
        conversationId: currentConversationId
    });
    chatMessages.innerHTML = '<div class="message bot-message">Bonjour ! Comment puis-je vous aider aujourd\'hui ?</div>';
    updateHistory();
}

function addMessage(message, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    messageHistory.push({
        message: message,
        timestamp: new Date(),
        isUser: isUser,
        conversationId: currentConversationId
    });
    
    updateHistory();
}

function updateHistory() {
    historyList.innerHTML = '';
    const groupedHistory = {};
    
    messageHistory.forEach(item => {
        if (!groupedHistory[item.conversationId]) {
            groupedHistory[item.conversationId] = {
                firstMessage: item.message,
                timestamp: item.timestamp
            };
        }
    });

    Object.entries(groupedHistory).reverse().forEach(([convId, data]) => {
        const historyItem = document.createElement('div');
        historyItem.classList.add('history-item');
        
        const timeDiv = document.createElement('div');
        timeDiv.classList.add('time');
        timeDiv.textContent = formatDate(data.timestamp);
        
        const messageDiv = document.createElement('div');
        messageDiv.textContent = data.firstMessage.substring(0, 30) + '...';
        
        historyItem.appendChild(timeDiv);
        historyItem.appendChild(messageDiv);
        
        historyItem.onclick = () => {
            currentConversationId = parseInt(convId);
            loadConversation(currentConversationId);
        };
        
        historyList.appendChild(historyItem);
    });
}

function loadConversation(conversationId) {
    chatMessages.innerHTML = '';
    const conversationMessages = messageHistory.filter(msg => msg.conversationId === conversationId);
    
    if (conversationMessages.length === 0) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', 'bot-message');
        messageDiv.textContent = "Début de la conversation";
        chatMessages.appendChild(messageDiv);
        return;
    }
    
    conversationMessages.forEach(msg => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(msg.isUser ? 'user-message' : 'bot-message');
        messageDiv.textContent = msg.message;
        chatMessages.appendChild(messageDiv);
    });
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.classList.add('bot-typing');
    typingDiv.id = 'typingIndicator';
    typingDiv.textContent = 'Bot est en train d\'écrire...';
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

function getBotResponse(userMessage) {
    const message = userMessage.toLowerCase();
    for (const [key, value] of Object.entries(botResponses)) {
        if (message.includes(key)) {
            return value;
        }
    }
    return botResponses.default;
}

function sendMessage() {
    const message = userInput.value.trim();
    if (message === '') return;

    addMessage(message, true);
    userInput.value = '';

    showTypingIndicator();

    // Remplacer le setTimeout par une requête fetch
    fetch('/chat/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => {
        console.log('Response status:', response.status);
        return response.json();
    })
    .catch(error => {
        console.error('Détails de l\'erreur:', error);
    });
}

// Fonction pour récupérer le cookie CSRF (à implémenter)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});