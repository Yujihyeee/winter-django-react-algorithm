const initialState = {users:[], user:{}}
export const addUserAction = user => ({type: "ADD_USER", payload: user})
export const deleteUserAction = userEmail => ({type: "DELETE_USER", payload: userEmail})
const userReducer = (state = initialState, action) => {
    switch(action.type){
        case "ADD_USER": return {...state, users:[...state.users, action.payload]}
        case "DELETE_USER": return {...state, users:state.users.filter(user => user.email !== action.payload)}
        default: return state
    }
}

export default userReducer