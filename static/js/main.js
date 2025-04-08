console.log('This is js from your Home page')


document.addEventListener("DOMContentLoaded", function () {
    const logoutForm = document.getElementById("logout-form");
  
    if (logoutForm) {
      logoutForm.addEventListener("submit", function (event) {
        const confirmLogout = confirm("Are you sure you want to log out?");
        if (!confirmLogout) {
          event.preventDefault();
        }
      });
    }
  });
  