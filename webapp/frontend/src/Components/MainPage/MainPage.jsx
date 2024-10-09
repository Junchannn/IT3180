import React from "react";
import { useNavigate } from "react-router-dom";
import "./MainPage.css";
import skyTerrace from "../Assets/sky-terrace_1.jpg";
const MainPage = () => {
  const navigate = useNavigate();

  const handleRegisterClick = () => {
    navigate("/register");
  };

  const handleLoginClick = () => {
    navigate("/login");
  };

  return (
    <div className="mainPage">
      <div className="image-container">
        <img
          src={skyTerrace}
          alt="Placeholder"
          className="content-image"
        />
        <h1 className="overlay-text">Hệ thống quản lý chung cư</h1>
      </div>
      <div className="button-container">
        <button className="main-button" onClick={handleRegisterClick}>
          Đăng kí
        </button>
        <button className="main-button" onClick={handleLoginClick}>
          Đăng nhập
        </button>
      </div>
      {/* <footer className="footer-text">Một sản phẩm của nhóm 10</footer> */}
    </div>
  );
};

export default MainPage;
