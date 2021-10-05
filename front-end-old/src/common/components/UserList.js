import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { deleteUserAction } from "reducers/user.reducer";

export default function UserList() {
    const users = useSelector( state => state.userReducer.users)
    const dispatch = useDispatch()
    const deleteUser = email => dispatch(deleteUserAction(email)) 

    return(<>
        {users.length === 0 && (<h1>지금은 등록된 회원이 없습니다.</h1>) }
        {users.length !== 0 && (<h1>{users.length} 명의 회원이 있습니다.</h1>)}

        {users.length !== 0 && users.map(
            user => (<div key={user.email}>
                <span>{user.email}</span>&nbsp;
            <button onClick={deleteUser.bind(null, user.email)}>X</button>
            </div>)
        )}
    </>)
}