import { Image, Box } from '@chakra-ui/react'
import React, { useEffect, useState } from "react";
import { Input } from '@chakra-ui/react'
import styled from "styled-components";
import axios from "axios";

const Title = styled.h1`
color :brown;
font-size: 64px;
`

const Center = styled.h2`
  display: flex;
  alignItems: center;
  justifyContent: center;
  height: 20vh;
`



const ImageView = (props) => {

    const [tag, setTag] = useState('');

    function deleteImage() {
        console.log("hit")
        // var json = ({'_id': props.id})
        // axios.delete(`http://127.0.0.1:5000/api/tags`, { '_id': props.id }, {
        //     headers: {
        //         'Content-Type': 'application/json'
        //     }
        // });

        axios.delete("http://127.0.0.1:5000/api/tags", { data: { '_id': props.id }, headers: { 'Content-Type': 'application/json' } });
        window.location.reload()
        // refresh page

    }

    function add_tags() {
        axios.put("http://127.0.0.1:5000/api/tags/custom", { '_id': props.id, 'tag': tag });
        window.location.reload()
    }



    return (
        <div>
            <button onClick={() => deleteImage()}>Delete</button>
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                height: '20vh',
            }}>
                <Title>
                    {props.title}
                </Title>
            </div>

            {<Box boxSize='sm'>
                <Image src={props.image} alt='Dan Abramov' style={{
                    width: "100%",
                    height: "auto"
                }} />
            </Box>}
            <br></br>
            <button onClick={() => add_tags()}>Add</button>

            <Input placeholder='add tags here'
                size='md'
                onChange={event => setTag(event.currentTarget.value)}
            />



            <h2 style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                height: '10vh',
            }}>{props.tags}</h2>

        </div>
    )

}

export default ImageView;
