// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    const textContainers = document.querySelectorAll('.tariff-body');

    textContainers.forEach(container => {
        const fullText = container.querySelector('.full-text');
        const shortText = container.querySelector('.short-text');
        const button = container.querySelector('.show-more');

        // Если текст короткий, показываем его полностью и скрываем кнопку
        if (fullText.textContent.length <= 200) {
            fullText.style.display = 'block';
            shortText.style.display = 'none';
            if (button) button.style.display = 'none';
        } else {
            // Для длинного текста показываем сокращенную версию
            fullText.style.display = 'none';
            shortText.style.display = 'block';
        }
    });
});

function toggleText(button) {
    const container = button.parentElement;
    const fullText = container.querySelector('.full-text');
    const shortText = container.querySelector('.short-text');

    if (fullText.style.display === 'none' || fullText.style.display === '') {
        fullText.style.display = 'block';
        shortText.style.display = 'none';
        button.textContent = 'hide';
    } else {
        fullText.style.display = 'none';
        shortText.style.display = 'block';
        button.textContent = 'read more';
    }
}