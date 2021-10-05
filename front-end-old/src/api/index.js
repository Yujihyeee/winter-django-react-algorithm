import axios from "axios";

const server = 'http://127.0.0.1:8000'
const header = { 'Content-Type': 'application/json' }
export const connect = () => axios.get(`${server}/api/connect`)
export const UserRegister = body => axios.post(`${server}/api/users/register`, {header, body})
export const UserList = () => axios.get(`${server}/api/users/list`)
export const UserDetail = id => axios.get(`${server}/api/users/${id}`)
export const UserRetriever = (key, value) => axios.get(`${server}/api/users/${key}/${value}`)
export const UserModify = body => axios.put(`${server}/api/users`, {header, body})
export const UserRemove = id => axios.delete(`${server}/api/users/${id}`)