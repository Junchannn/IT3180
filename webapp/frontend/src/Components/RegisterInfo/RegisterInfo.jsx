import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './RegisterInfo.css';

const LoginInfo = () => {
    const [fullName, setFullName] = useState('');
    const [dob, setDob] = useState('');
    const [hometown, setHometown] = useState('');
    const [apartmentNumber, setApartmentNumber] = useState('');
    const [identityCard, setIdentityCard] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // CODE HERE
        console.log({ fullName, dob, hometown, identityCard, apartmentNumber });
    };

    return (
        <div className="register-info">
            <form onSubmit={handleSubmit}>
                <h1>Thông Tin Đăng Nhập</h1>
                <div className="input-box">
                    <input
                        type="text"
                        placeholder="Họ và Tên"
                        value={fullName}
                        onChange={(e) => setFullName(e.target.value)}
                        required
                    />
                </div>
                <div className="input-box">
                    <input
                        type="date"
                        placeholder="Ngày tháng năm sinh"
                        value={dob}
                        onChange={(e) => setDob(e.target.value)}
                        required
                    />
                </div>
                <div className="input-box">
                    <input
                        type="text"
                        placeholder="Quê quán"
                        value={hometown}
                        onChange={(e) => setHometown(e.target.value)}
                        required
                    />
                </div>
                <div className='input-box'>
                    <input
                        type='number'
                        placeholder='CMND/CCCD'
                        value={identityCard}
                        onChange={(e) => setApartmentNumber(e.target.value)}
                        required
                    />
                </div>
                <div className="input-box">
                    <input
                        type="text"
                        placeholder="Số căn hộ trong chung cư"
                        value={apartmentNumber}
                        onChange={(e) => setApartmentNumber(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Gửi</button>
                <div className="login-link">
                    <p>Đã có tài khoản? <Link to="/login">Đăng nhập</Link></p>
                </div>
            </form>
        </div>
    );
};

export default LoginInfo;