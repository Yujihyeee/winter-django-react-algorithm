import React from "react";
import styled from 'styled-components'
import { TodoList, TodoInput } from 'features/todos/index'

export default function Todo() {
    return(
        <TodoDiv>
            <TodoInput/>
            <TodoList/>
        </TodoDiv>
    )
}

const TodoDiv = styled.div` text-align: center; `