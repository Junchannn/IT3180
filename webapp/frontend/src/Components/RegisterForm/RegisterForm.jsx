import React, { useState } from "react";
import './RegisterForm.css';
import { FaUser } from "react-icons/fa";
import { RiLockPasswordFill, RiMailFill } from "react-icons/ri";
import { Link, useNavigate } from 'react-router-dom';

const RegisterForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [errors, setErrors] = useState({});
    const navigate = useNavigate();

    const validate = () => {
        const errors = {};
        if (!username) errors.username = "Username is required";
        if (!email) errors.email = "Email is required";
        else if (!/\S+@\S+\.\S+/.test(email)) errors.email = "Email is invalid";
        if (!password) errors.password = "Password is required";
        if (!confirmPassword) errors.confirmPassword = "Confirm Password is required";
        else if (password !== confirmPassword) errors.confirmPassword = "Passwords do not match";
        return errors;
    };

    const handleRegister = (e) => {
        e.preventDefault();
        const validationErrors = validate();
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
        } else {
            // Proceed with form submission
            console.log("Form submitted successfully");
            navigate('/register-info');
        }
    };

    return (
        <div className="register-form">
            <form onSubmit={handleRegister}>
                <h1>Đăng Ký</h1>
                <div className="input-box">
                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                    <FaUser className="icon"/>
                    {errors.username && <p className="error-message">{errors.username}</p>}
                </div>
                <div className="input-box">
                    <input
                        type="email"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                    <RiMailFill className="icon"/>
                    {errors.email && <p className="error-message">{errors.email}</p>}
                </div>
                <div className="input-box">
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <RiLockPasswordFill className="icon"/>
                    {errors.password && <p className="error-message">{errors.password}</p>}
                </div>
                <div className="input-box">
                    <input
                        type="password"
                        placeholder="Confirm Password"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        required
                    />
                    <RiLockPasswordFill className="icon"/>
                    {errors.confirmPassword && <p className="error-message">{errors.confirmPassword}</p>}
                </div>

                <button type="submit">Đăng ký</button>

                <div className="login-link">
                    <p>Đã có tài khoản? <Link to="/login">Đăng nhập</Link></p>
                </div>
            </form>
        </div>
    );
}

export default RegisterForm;