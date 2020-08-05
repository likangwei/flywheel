import React from 'react';
import './App.css';
import Index from './flywheel/index'


import {
  BrowserRouter as Router,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <div>
      <Router>
      <Link to='/flywheel'>开始转动飞轮吧!</Link>
      <Route  path="/flywheel/" component={Index}/>
      </Router>
    </div>

  );
}

export default App;
