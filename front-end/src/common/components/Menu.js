import React from "react"
import { Link } from "react-router-dom"
import styled from "styled-components"

const Menu = () => {
    return(
    <Nav>
        <NavList>
            <NavItem><Link to = '/math'>Mathematics</Link></NavItem>
            <NavItem><Link to = '/linear'>Linear</Link></NavItem>
            <NavItem><Link to = '/nonlinear'>NonLinear</Link></NavItem>
            <NavItem><Link to = '/bruteforce'>BruteForce</Link></NavItem>
            <NavItem><Link to = '/divide'>DivideAndConquer</Link></NavItem>
            <NavItem><Link to = '/greedy'>Greedy</Link></NavItem>
            <NavItem><Link to = 'dynamic'>DynamicAndProgramming</Link></NavItem>
            <NavItem><Link to = 'backtracking'>BackTracking</Link></NavItem>
        </NavList>
    </Nav>
    )
}

export default Menu

const Nav = styled.div`
    width: 100%;
    height: 100px;
    border-bottom: 1px soild #d1d8e4;
`
const NavList = styled.ul`
    width: 1080px;
    display: flex;
    margin: 0 auto;
`

const NavItem = styled.li`
    width: auto;
    margin-left: 20px;
    margin-top: 30px;
    display: flex;
`