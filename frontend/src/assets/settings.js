const aboutBtn = document.querySelector('#main-settings-about');
const aboutWindow = document.querySelector('#main-settings-about-window');
const langBtn = document.querySelector('#main-settings-lang');
const langWindow = document.querySelector('#main-settings-lang-window');
const themeBtn = document.querySelector('#main-settings-theme');

aboutBtn.addEventListener('click', () => {
  toggleWindow(aboutWindow, 'about');
});

langBtn.addEventListener('click', () => {
  toggleWindow(langWindow, 'lang');
});

function toggleWindow(window, key) {
  if (window.style.display === 'flex') {
    window.style.display = 'none';
    localStorage.removeItem('window');
  } else {
    aboutWindow.style.display = 'none';
    langWindow.style.display = 'none';
    window.style.display = 'flex';
    localStorage.setItem('window', key);
  }
}

document.addEventListener('click', (event) => {
  if (!aboutBtn.contains(event.target) && !aboutWindow.contains(event.target) && !langBtn.contains(event.target) && !langWindow.contains(event.target)) {
    aboutWindow.style.display = 'none';
    langWindow.style.display = 'none';
    localStorage.removeItem('window');
  }
});

switch(localStorage.getItem('window')) {
  case 'about':
    aboutWindow.style.display = 'flex';
    break;
  case 'lang':
    langWindow.style.display = 'flex';
    break;
  default:
    break;
}
