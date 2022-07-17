import React, { useEffect, useState } from "react";
import axios from "axios";
import { Image, Box } from '@chakra-ui/react'

import './App.css';

export default () => {

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
    <div> {data.map((d, i) =>
      <div>
        {/* <p>{d}</p> */}
        <h1>image {i}</h1>
        <div>
          <Box boxSize='sm'>
            <Image src={d["image_link"]}  alt='Dan Abramov' />
          </Box>
          <h2>{d["tags"]}</h2>
        </div>
      </div>)}</div>
  )



}
