import React, { useState } from "react";
import './ForgotPassword.css';
import { Link } from 'react-router-dom'; 

const ForgotPassword = () => {
    // Quản lý bước => bước 1 gửi mã, bước 2 là xác nhận mã
    const [step, setStep] = useState(1); 
    // Trạng thái lưu email/số điện thoại
    const [contact, setContact] = useState('');
    // Trạng thái lưu mã xác nhận
    const [code, setCode] = useState('');

    // xử lí backend
    const handleSendCode = () => {
        console.log("Gửi mã đến:", contact);
        setStep(2);
    };

    // xử lí backend
    const handleVerifyCode = () => {
        console.log("Mã xác nhận:", code);
    };

    return (
        <div className="forgot-password">
            <h1>Quên Mật Khẩu</h1>
            {step === 1 && (
                <div>
                    <input
                        type="text"
                        placeholder="Nhập Email hoặc Số Điện Thoại"
                        value={contact}
                        onChange={(e) => setContact(e.target.value)}
                        required
                    />
                    <button onClick={handleSendCode}>Gửi Mã</button>
                </div>
            )}
            {step === 2 && (
                <div>
                    <input
                        type="text"
                        placeholder="Nhập Mã Xác Nhận"
                        value={code}
                        onChange={(e) => setCode(e.target.value)}
                        required
                    />
                    <button onClick={handleVerifyCode}>Xác Nhận</button>
                    <button onClick={handleSendCode}>Gửi Lại Mã</button>
                </div>
            )}
            <div className="back-link">
                <Link to="/login">Quay lại Đăng Nhập</Link>
            </div>
        </div>
    );
};

export default ForgotPassword;
