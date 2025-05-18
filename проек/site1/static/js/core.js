document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('modal');
    const closeBtn = document.querySelector('.close');
    
    if (!modal || !closeBtn) {
        console.error('Не найдены элементы модального окна!');
        return;
    }
    
    document.querySelectorAll('.modal-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            console.log('Кнопка нажата!');
            
            const card = this.closest('.card-2');
            if (!card) {
                console.error('Не найдена родительская карточка');
                return;
            }
            
            const title = card.querySelector('.h3-text-img').textContent;
            const imgSrc = card.querySelector('.card-img').src;
            
            document.getElementById('modal-title').textContent = title;
            document.getElementById('modal-image').src = imgSrc;
            
            modal.style.display = 'block';
            console.log('Модальное окно должно быть видно!');
        });
    });
    
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });
    
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
        }
    });
});