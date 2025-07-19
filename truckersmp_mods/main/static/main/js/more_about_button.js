document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggle-history');
    const historyContent = document.getElementById('history-content');

    // Инициализация состояния
    historyContent.classList.add('collapsed');

    toggleButton.addEventListener('click', function() {
        if (historyContent.classList.contains('expanded')) {
            // Сворачиваем контент
            historyContent.classList.remove('expanded');
            historyContent.classList.add('collapsed');
            toggleButton.textContent = 'read';
        } else {
            // Разворачиваем контент
            historyContent.classList.remove('collapsed');
            historyContent.classList.add('expanded');
            toggleButton.textContent = 'hide';
        }
    });
});