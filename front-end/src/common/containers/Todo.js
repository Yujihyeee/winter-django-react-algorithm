import { Button , TextField } from "@mui/material";
import React, {useState} from "react";
import styled from 'styled-components'


export default function Todo () {
    const [todo, setTodo] = useState('')
    let val= ''
    const add = e => {
        e.preventDefault()
        val = e.target.value
    }
    const del = e => {
        e.preventDefault()
        setTodo('')
    }
    const submitForm = e => {
        e.preventDefault()
        setTodo(val)
        document.getElementById('todo-input').value = ''
    }

    return(
        <form onSubmit={submitForm} method='POST'>
        <Tododiv>
            <input type='text' id='todo-input' onChange={add}/>
            <input type='submit' value='ADD'/><br/>
            <span>{todo}</span>
            <input type='button' onClick={del} value='DEL'/>
        </Tododiv></form>)
}

const Tododiv = styled.div`text-align: center;`