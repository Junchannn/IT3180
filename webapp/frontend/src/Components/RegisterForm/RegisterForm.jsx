import React from "react";
import './RegisterForm.css';
import { FaUser } from "react-icons/fa";
import { RiLockPasswordFill, RiMailFill } from "react-icons/ri";
import { Link } from 'react-router-dom';

const RegisterForm = () => {
    return (
        <div className="register-form">
            <form action="">
                <h1>Đăng Ký</h1>
                <div className="input-box">
                    <input type="text" placeholder="Username" required />
                    <FaUser className="icon"/>
                </div>
                <div className="input-box">
                    <input type="email" placeholder="Email" required />
                    <RiMailFill className="icon"/>
                </div>
                <div className="input-box">
                    <input type="password" placeholder="Password" required />
                    <RiLockPasswordFill className="icon"/>
                </div>
                <div className="input-box">
                    <input type="password" placeholder="Confirm Password" required />
                    <RiLockPasswordFill className="icon"/>
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
