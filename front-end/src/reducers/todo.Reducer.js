const initalState = {todos:[], todo:{}}
export const addTodoAction = todo => ({type: "ADD_TODO", payload:todo})
const todoReducer = (state = initalState, action) => {
    switch(action.type){
        default : return state
    }
}

export default todoReducer