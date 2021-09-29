import React from 'react';
import { BackTracking, BruteForce, DivideAndConquer, DynamicAndProgramming, Greedy } from 'algorithm/index';
import { Home, Counter, Todo } from 'common/index';
import { Linear, Mathematics, NonLinear } from 'datastructure/index';
import { Route, Redirect, Switch } from 'react-router-dom';
import { Menu } from 'common/index';
import {combineReducers, createStore} from "redux"
import { Provider } from 'react-redux'
import rootReducder from 'reducers'

const rootReducder = combineReducers({todoReducer})
const store = createStore(rootReducder)

const App = () => {
  return(
    <Provider store={store}>
      <Menu/>
      <Switch>
        <Route exact path = '/' component = {Home}/>
          <Redirect from = '/home' to = {'/'}/>
          <Route exact path = '/counter' component = {Counter}/>
          <Route exact path = '/todo' component = {Todo}/>
          <Route exact path = '/backtracking' component = {BackTracking}/>
          <Route exact path = '/bruteforce' component = {BruteForce}/>
          <Route exact path = '/divide' component = {DivideAndConquer}/>
          <Route exact path = '/dynamic' component = {DynamicAndProgramming}/>
          <Route exact path = '/greedy' component = {Greedy}/>
          <Route exact path = '/linear' component = {Linear}/>
          <Route exact path = '/math' component = {Mathematics}/>
          <Route exact path = '/nonlinear' component = {NonLinear}/>
      </Switch>
    </Provider>
  )
  
}

export default App;
