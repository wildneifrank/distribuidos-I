"use client";

import React, { useState } from "react";
import Sidebar from "../components/Sidebar";
import Dashboard from "../components/Dashboard";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const Home = () => {
  const [scene, setScene] = useState(0);
  const [mode, setMode] = useState(false);
  return (
    <div className={`w-full h-screen flex ${mode ? "dark" : ""}`}>
      <ToastContainer position="bottom-left" autoClose={5000} />
      <Sidebar
        mode={mode}
        setMode={setMode}
        setScene={setScene}
        scene={scene}
      />
      <Dashboard />
    </div>
  );
};

export default Home;
