const buttonSubmit = document.querySelector('.hero-settings-user-window-registration-button') 
const passwordField = document.querySelectorAll('.hero-settings-user-window-registration-password')
const passwordShow = document.querySelector('.hero-settings-user-window-registration-password-show-checkbox')


// passwordField.forEach((passwordField) => {
//   passwordField.addEventListener('blur', (e) => {
//     const passwordVal = e.target.value;
//     const buttonSubmit = document.querySelector('.hero-settings-user-window-registration-submit');
    
//     passwordField.style.borderColor = '';
  
//     if (passwordField.checkValidity()) {
//       fetch('', {
//         body: JSON.stringify({password: passwordVal}),
//         method: 'POST',
//       })
//       .then((res) => res.json())
//       .then((data) => {
//         if (data.valid) {
//           passwordField.style.borderColor = 'red';
//           buttonSubmit.disabled = true;
//         } else {
//           passwordField.style.borderColor = 'green';
//           buttonSubmit.disabled = false;
//         }
//       });
//     } else {
//       passwordField.style.borderColor = 'red';
//       buttonSubmit.disabled = true;
//     }
//   });
// });


const passwordToggle = () => {
  if (passwordShow.checked) {
    passwordField.forEach((field) => {
      field.setAttribute('type', 'text');
    });
  } else {
    passwordField.forEach((field) => {
      field.setAttribute('type', 'password');
    });
  }
};

passwordShow.addEventListener('click', passwordToggle);