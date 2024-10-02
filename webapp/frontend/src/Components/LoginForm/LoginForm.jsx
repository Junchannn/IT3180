import React from "react";
import './LoginForm.css';
import { FaUser } from "react-icons/fa";
import { RiLockPasswordFill } from "react-icons/ri";
import { Link } from 'react-router-dom';  // Sử dụng Link từ react-router-dom để điều hướng


const LoginForm = () => {
    return (
        <div className="login-form">
            <form action="">
                <h1>Đăng Nhập</h1>
                <div className="input-box">
                    <input type="text" placeholder="Tên Đăng nhập/Email" required />
                    <FaUser className="icon"/>
                </div>
                <div className="input-box">
                    <input type="text" placeholder="Password" required />
                    <RiLockPasswordFill className="icon"/>
                </div>

                <div className="remember-forgot">
                    <label><input type="checkbox" /> Lưu truy cập</label>
                    <a href="/forgot-password"> Quên mật khẩu?</a>
                </div>

                <button type="submit">Đăng nhập</button>

                <div className="register-link">
                    <p>Chưa có tài khoản? <Link to="/register">Đăng ký</Link></p> 
                </div>
            </form>
        </div>
    );
}

export default LoginForm