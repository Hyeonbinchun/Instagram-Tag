import React, { useEffect, useState } from "react";
import axios from "axios";
import {BrowserRouter as Router, Link} from 'react-router-dom';

const Upload = () => {

  const [picture, setPicture] = useState(null);
  const [imgData, setImgData] = useState(null);

  const onChangePicture = e => {
    if (e.target.files[0]) {
      console.log(e)
      console.log("picture: ", e.target.files);
      setPicture(e.target.files[0]);
      const reader = new FileReader();
      reader.addEventListener("load", () => {
        setImgData(reader.result);
      });
      reader.readAsDataURL(e.target.files[0]);

      var formData = new FormData();
      formData.append("img", e.target.files[0])
      formData.append("file", e.target.files[0]);
      axios.post(`http://127.0.0.1:5000/api/tags`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
})



    }
  };


  
  return (
    <div>
            <div>
        <Link to="/">
          <button>HOME</button>
        </Link>
      </div>

      <p>This is the uplokad page</p>
      <div className="register_profile_image">
        <input id="profilePic" type="file" onChange={onChangePicture} />
      </div>
    </div>)

}

export default Upload;
