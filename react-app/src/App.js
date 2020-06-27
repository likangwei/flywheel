import React from 'react';
import logo from './logo.svg';
import './App.css';
import Cycle from './flywheel/cycle'
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button';


import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <Router>
    <Link to='/flywheel'>开始转动飞轮吧!</Link>
    <Route exact path="/flywheel" component={Cycle}/>
    </Router>

  );
}

export default App;
