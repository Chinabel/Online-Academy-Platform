function changeLanguage(lang) {
    const greeting = document.getElementById('greeting');
    const message = document.getElementById('message');

    switch (lang) {
        case 'es':
            greeting.textContent = '¡Hola!';
            message.textContent = '¡Bienvenido a la O-Academia!';
            break;
        case 'fr':
            greeting.textContent = 'Bonjour!';
            message.textContent = 'Bienvenue à l\'O-Academy!';
            break;
        case 'de':
            greeting.textContent = 'Hallo!';
            message.textContent = 'Willkommen bei der O-Akademie!';
            break;
        case 'pt':
            greeting.textContent = 'Hola!';
            message.textContent = 'Bem-vindo à O-Academia!';
            break;
        default:
            greeting.textContent = 'Hello!';
            message.textContent = 'Welcome to the O-Academy!';
            break;
    }
}
