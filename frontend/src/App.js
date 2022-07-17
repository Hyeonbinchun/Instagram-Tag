import React, { useEffect, useState } from "react";



// import { BrowserRouter as Router, Route } from "react-router-dom";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./components/Home";
import Upload from "./components/Upload";

const App = () => {

  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<Upload/>}/>
      </Routes>
      
    </div>


  );


}


export default App;