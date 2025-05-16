// Modern Todo App JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide messages after 3 seconds
    const messages = document.querySelectorAll('.message');
    if (messages.length > 0) {
        setTimeout(() => {
            messages.forEach(message => {
                message.style.opacity = '0';
                setTimeout(() => {
                    message.remove();
                }, 300);
            });
        }, 3000);
    }

    // Add task form validation
    const taskForm = document.querySelector('.task-form');
    if (taskForm) {
        taskForm.addEventListener('submit', function(e) {
            const titleInput = this.querySelector('input[name="title"]');
            if (!titleInput.value.trim()) {
                e.preventDefault();
                titleInput.classList.add('error');
                
                // Add error message if it doesn't exist
                let errorMessage = titleInput.parentNode.querySelector('.error-message');
                if (!errorMessage) {
                    errorMessage = document.createElement('div');
                    errorMessage.classList.add('error-message');
                    errorMessage.textContent = 'Task title is required';
                    titleInput.parentNode.appendChild(errorMessage);
                }
            }
        });
    }
});