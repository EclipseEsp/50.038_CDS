import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [prediction, setPrediction] = useState(0);

  useEffect(() => {
    fetch('/classify_waste').then(res => res.json()).then(data => {
      setPrediction(data.pred);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>The current prediction is {prediction}.</p>
      </header>
    </div>
  );
}

export default App;
