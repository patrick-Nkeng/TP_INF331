function openReplyModal(notificationId) {
    document.getElementById('replyModal').style.display = 'block';
}

function closeReplyModal() {
    document.getElementById('replyModal').style.display = 'none';
}

// Fermer la modal si on clique en dehors
window.onclick = function(event) {
    let modal = document.getElementById('replyModal');
    if (event.target == modal) {
        closeReplyModal();
    }
}

document.querySelector('.reply-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const replyText = this.querySelector('textarea').value;
    if (replyText.trim()) {
        alert('Réponse envoyée avec succès !');
        closeReplyModal();
        this.reset();
    }
});