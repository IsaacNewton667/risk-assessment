window.onload = function() {
    const form = document.querySelector('#myForm');
    const addButton = document.querySelector('#addButton');
    const nextButton = document.querySelector('#nextButton');

    addButton.addEventListener('click', () => {
        form.action = '/decision-management-process/add-3';
        form.submit();
    });

    nextButton.addEventListener('click', () => {
        form.action = '/decision-management-process/next-3';
        form.submit();
    });
};
