import { auth, signInWithEmailAndPassword } from '../firebase_config';
console.log("auth started")
document.getElementById('loginbtn').addEventListener('submit', async (event) => {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    console.log(email,password)

    try {
        // Sign in and get the token
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;
        console.log(user)
        const token = await user.getIdToken();
        console.log(token)

        // Send the token to the FastAPI backend
        const response = await fetch('http://127.0.0.1:8000/app/login', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });


        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error.message);
    }
});
