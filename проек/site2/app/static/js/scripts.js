document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registration-form');
    const counter = document.getElementById('participant-counter');
    const notification = document.getElementById('notification');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            if (key === 'profession') {
                if (!data[key]) data[key] = [];
                data[key].push(value);
            } else {
                data[key] = value;
            }
        });
        
        if (data['profession'] && Array.isArray(data['profession'])) {
            data['profession'] = data['profession'].join(', ');
        }
        
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                counter.textContent = data.count;
                showNotification('Регистрация прошла успешно!', 'success');
                form.reset();
            } else {
                showNotification(data.message, 'danger');
            }
        })
        .catch(error => {
            showNotification('Ошибка при отправке формы', 'danger');
            console.error('Error:', error);
        });
    });
    
    function showNotification(message, type) {
        notification.textContent = message;
        notification.className = `alert alert-${type} alert-notification show-notification`;
        notification.style.display = 'block';
        
        setTimeout(() => {
            notification.classList.remove('show-notification');
            setTimeout(() => {
                notification.style.display = 'none';
            }, 500);
        }, 3000);
    }
});