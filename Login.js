// Tentukan usernsme dan pasword yang valid
const validUsername = 'Hisyam Sayyid Alzam'
const validPassword = '03122008'

//Mengenai submit form login
document.getElementById('loginForm').addEventListener('submit',function(event){
    event.preventDefault(); // Mencegah reload halaman 
    
    //Mengamvil nilai dari input username dan passwoerd
    const username = document.getElementById('username').value;
    const passwoerd = document.getElementById('password').value;
    
    //Mengecek apakah username  dan password sesuai dengan yang vaild
    if (username == validUsername && passwoerd === validPassword){
        //jika benar,arahkan ke halaman utama (contohnya home.html)
        window.location.href = 'Tabel DPK 1.html';
    } else {
        // Jika salah, tampilkan pesan eror
        document.getElementById('errorMessage').innerText = 'Invalid username or password!';
    }
});

// icon mata
const togglePassword = document.getElementById('togglePassword');
const passwordInput = document.getElementById('password');
const eyeIcon = document.getElementById('eyeIcon');

togglePassword.addEventListener('click', function () {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);

    // Mengubah ikon mata berdasarkan jenis input
    if (type === 'text') {
        eyeIcon.classList.remove('fa-eye-slash');
        eyeIcon.classList.add('fa-eye'); // Mata terbuka
    } else {
        eyeIcon.classList.remove('fa-eye');
        eyeIcon.classList.add('fa-eye-slash'); // Mata tertutup
    }
});