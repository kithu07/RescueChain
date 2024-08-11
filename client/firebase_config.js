import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDwM9z9QjNA0V21Jxbh6xiIy3MYF6Jjzs4",
  authDomain: "rescuechain.firebaseapp.com",
  projectId: "rescuechain",
  storageBucket: "rescuechain.appspot.com",
  messagingSenderId: "41147908434",
  appId: "1:41147908434:web:bc8d2d82631f6acb97ba8b",
  measurementId: "G-HPLBEYFYN4"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export { auth, signInWithEmailAndPassword };
