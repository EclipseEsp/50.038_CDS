import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import recycling from './recycling.svg'
import './App.css';
import Camera, { FACING_MODES } from 'react-html5-camera-photo';
import 'react-html5-camera-photo/build/css/index.css';

function App() {
  const [prediction, setPrediction] = useState(0)
  const [label, setLabel] = useState(0)
  const [image, setImage] = useState(null)

  // Function to Pass Image to be Predicted in Flask
  const fetchPrediction = (dataUri) => {
    fetch('/classify_waste',{
      method: 'POST',
      body: dataUri,
    }).then(res => res.json()).then(data => {
      setPrediction(data.pred);
      setLabel(data.label);
    });
  }

  // Select Files/Images for Prediction
  const onSelect = (event) => {
    if (event.target.files && event.target.files[0]) {
      let img = event.target.files[0];
      console.log(img)
      // FileReader to convert event.target.file to dataUri
      var reader = new FileReader()
      reader.readAsDataURL(img)
      reader.onload = function () {
        console.log(reader.result)//base64encoded string

        // send for predict after conversion (.onload)
        fetchPrediction(reader.result)
      };

      setImage(URL.createObjectURL(img)) // display selected image
    }
  }
  
  // Take Photo for Prediction
  function handleTakePhoto (dataUri) {
    // Do stuff with the photo...
    console.log(dataUri)
    document.getElementById("input").value=""

    setImage(dataUri) // display taken image

    fetchPrediction(dataUri)
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={recycling} className="App-logo" alt="logo" />
        <h1> Recycl-EZ (Garbarge Classification)</h1>
      </header>
      <body>
          <h1>Select Image or Take Picture</h1>
          {<Camera idealFacingMode = {FACING_MODES.ENVIRONMENT} isImageMirror = {false} onTakePhoto = { (dataUri) => { handleTakePhoto(dataUri); } }/>}
          <hr></hr>
          <img src={image} style={{height:'224px',width:'224px',marginRight: '10px'}}></img>
          <input id="input" type="file" name="myImage" onChange={onSelect} />
          <p>The image is predicted to be <b>{label}</b> with confidence level of <b>{prediction}%</b>.</p>
      </body>
    </div>
  );
}

export default App;
