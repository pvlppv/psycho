const popup = document.querySelector('.hero-settings-user-popup');
const popupBackground = document.querySelector('.hero-settings-user-popup-background')
const acceptBtn = document.querySelector('.hero-settings-user-popup-accept');

if (!localStorage.getItem('policy', 'accepted')) {
  popup.style.display = 'flex';
  popupBackground.style.display = 'block';
}
  
acceptBtn.addEventListener('click', function() {
  popup.style.display = 'none';
  popupBackground.style.display = 'none';
  localStorage.setItem('policy', 'accepted');
});

