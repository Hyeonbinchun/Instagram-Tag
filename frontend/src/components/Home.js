import React, { useEffect, useState } from "react";
import axios from "axios";
import { Image, Box } from '@chakra-ui/react'
import ImageView from "../components/ImageView";
import '../App.css';
import styled from "styled-components";
import {BrowserRouter as Router, Link} from 'react-router-dom';

const Container = styled.div`
background: beige;
padding: 4rem;
`


const Home = () => {

  const [data, setData] = useState([]);

  const getData = async () => {
    const { data } = await axios.get(`http://127.0.0.1:5000/api/images`);
    console.log(data["data"])
    setData(data["data"]);
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <Container> 

      <div>
        <Link to="/upload">
          <button>UPLOAD</button>
        </Link>
      </div>

      
      
      {data.map((d, i) =>
      <div>
        <div>
          <ImageView
            title={"Image " + i}
            tags={d["tags"].map(string => ("#") + string + (" "))}
            image={d["image_link"]}
            id={d["_id"]} />
        </div>
      </div>)}</Container>
  )


}

export default Home;
