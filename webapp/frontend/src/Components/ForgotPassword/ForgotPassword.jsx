import React, { useState } from "react";
import './ForgotPassword.css';
import { Link } from 'react-router-dom'; 

const ForgotPassword = () => {
    const [step, setStep] = useState(1); 
    const [contact, setContact] = useState('');
    const [code, setCode] = useState('');
    const [error, setError] = useState('');

    const handleSendCode = () => {
        if (!isValidEmail(contact)) {
            setError('Đề nghị điền theo format email');
            return;
        }
        setError('');
        console.log("Gửi mã đến:", contact);
        setStep(2);
    };

    const handleVerifyCode = () => {
        console.log("Mã xác nhận:", code);
    };

    const isValidEmail = (email) => {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    };

    return (
        <div className="forgot-password">
            <form action="">
            <h1>Quên Mật Khẩu</h1>
            {step === 1 && (
                    <div>
                        <input
                            type="email"
                            placeholder="Nhập Email"
                            required
                            value={contact}
                            onChange={(e) => setContact(e.target.value)}
                        />
                        {error && <p className="error-message">{error}</p>}
                        <button onClick={handleSendCode} disabled={!contact}>Gửi Mã</button>
                    </div>
            )}
            {step === 2 && (
                    <div>
                        <input
                            type="text"
                            placeholder="Nhập Mã Xác Nhận"
                            required
                            value={code}
                            onChange={(e) => setCode(e.target.value)}
                        />
                        <button onClick={handleVerifyCode} disabled={!code}>Xác Nhận</button>
                        <button onClick={handleSendCode}>Gửi Lại Mã</button>
                    </div>
            )}
            <div className="back-link">
                <Link to="/login">Quay lại Đăng Nhập</Link>
            </div>
            </form>
        </div>
    );
};

export default ForgotPassword;