import React from "react";
import { useSelector } from "react-redux";
import styled from "styled-components"

export default function UserList(){
    const users = useSelector(state => state.useSelector.users)
    return(
        <UserListDiv>
            {users.length === 0 && (<h2>등록된 회원수 : </h2>)}
            {users.length !== 0 && (<h2> {}명의 회원 목록이 있습니다.</h2>)}
        </UserListDiv>
    )
}

const UserListDiv = styled.div`text-align: center;`