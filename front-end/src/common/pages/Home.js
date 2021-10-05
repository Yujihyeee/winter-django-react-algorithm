import { SignIn } from "features/user";
import React from "react";
import { connect } from "react-redux";

export default function Home(){
    const handelClick = e =>{
        e.preventDefault()
        alert('Home Click')
        connect()
        .then(res => {alert(`접속성공 : ${res.data.connection}`)})
        .catch(err => {alert(`접속실패 : ${err}`)})
    }
    return(
        <>
        <button onClick={handelClick}>Connection</button>
        <SignIn/>
    </>
    )
    
}