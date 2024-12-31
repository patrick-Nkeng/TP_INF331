const authContainer = document.getElementById('auth-container');
const authLink = document.getElementById('auth-link');
let currentForm = 'login'; // Par défaut, on affiche le formulaire de connexion

function showRegistrationForm() {
  authContainer.innerHTML = `
    <h2>Inscription</h2>
    <form id="registration-form">
      <div class="form-group">
        <label for="reg-name">Nom complet</label>
        <input type="text" id="reg-name" name="name" required>
      </div>
      <div class="form-group">
        <label for="reg-email">Email</label>
        <input type="email" id="reg-email" name="email" required>
      </div>
      <div class="form-group">
        <label for="reg-password">Mot de passe</label>
        <input type="password" id="reg-password" name="password" required>
      </div>
      <div class="form-group">
        <label for="reg-confirm-password">Confirmer le mot de passe</label>
        <input type="password" id="reg-confirm-password" name="confirm-password" required>
      </div>
      <button type="submit" class="btn">S'inscrire</button>
    </form>
    <div class="switch-form">
      <p>Déjà inscrit ? <a href="#" id="switch-to-login">Se connecter</a></p>
    </div>
  `;

  document.getElementById('switch-to-login').addEventListener('click', (e) => {
    e.preventDefault();
    showLoginForm();
  });

  document.getElementById('registration-form').addEventListener('submit', handleRegistration);
}

function showLoginForm() {
  authContainer.innerHTML = `
    <h2>Connexion</h2>
    <form id="login-form">
      <div class="form-group">
        <label for="login-email">Email</label>
        <input type="email" id="login-email" name="email" required>
      </div>
      <div class="form-group">
        <label for="login-password">Mot de passe</label>
        <input type="password" id="login-password" name="password" required>
      </div>
      <button type="submit" class="btn">Se connecter</button>
    </form>
    <div class="switch-form">
      <p>Pas encore de compte ? <a href="#" id="switch-to-register">S'inscrire</a></p>
    </div>
  `;

  document.getElementById('switch-to-register').addEventListener('click', (e) => {
    e.preventDefault();
    showRegistrationForm();
  });

  document.getElementById('login-form').addEventListener('submit', handleLogin);
}

async function handleRegistration(e) {
  e.preventDefault();
  const name = document.getElementById('reg-name').value;
  const email = document.getElementById('reg-email').value;
  const password = document.getElementById('reg-password').value;
  const confirmPassword = document.getElementById('reg-confirm-password').value;

  if (password !== confirmPassword) {
    alert("Les mots de passe ne correspondent pas.");
    return;
  }

  try {
    const response = await axios.post('https://api.recrutement-interactif.com/register', {
      name,
      email,
      password
    });
    
    if (response.data.success) {
      alert('Inscription réussie ! Vous pouvez maintenant vous connecter.');
      showLoginForm();
    } else {
      alert('Erreur lors de l\'inscription : ' + response.data.message);
    }
  } catch (error) {
    console.error('Erreur:', error);
    alert('Une erreur est survenue lors de l\'inscription. Veuillez réessayer.');
  }
}

async function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;

  try {
    const response = await axios.post('https://api.recrutement-interactif.com/login', {
      email,
      password
    });
    
    if (response.data.success) {
      alert('Connexion réussie !');
      window.location.href = '/dashboard';
    } else {
      alert('Erreur de connexion : ' + response.data.message);
    }
  } catch (error) {
    console.error('Erreur:', error);
    alert('Une erreur est survenue lors de la connexion. Veuillez réessayer.');
  }
}

// Afficher le formulaire de connexion par défaut
showLoginForm();

// Gestionnaire d'événements pour le lien d'authentification dans la navigation
authLink.addEventListener('click', (e) => {
  e.preventDefault();
  if (currentForm === 'login') {
    showRegistrationForm();
    currentForm = 'register';
  } else {
    showLoginForm();
    currentForm = 'login';
  }
});
