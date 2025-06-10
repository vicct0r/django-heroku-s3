document.addEventListener('DOMContentLoaded', function() {
    // Fechar mensagens manualmente
    document.querySelectorAll('.close-message').forEach(button => {
        button.addEventListener('click', function() {
            this.closest('.message-alert').style.display = 'none';
        });
    });
    
    // Remover mensagens após o tempo de exibição
    setTimeout(() => {
        document.querySelectorAll('.message-alert').forEach(message => {
            message.style.display = 'none';
        });
    }, 5000);
});