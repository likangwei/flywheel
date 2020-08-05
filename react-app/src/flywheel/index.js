import React from 'react';
import Cycle from './cycle'
import CycleList from './CycleList'

import {
  Route,
} from "react-router-dom";



export default class Index extends React.Component {


  render(){
    return (
      <div>
        index
        <Route key="list" path="/flywheel/" exact ><CycleList/></Route>
        <Route key="cycle" path="/flywheel/cycle/:id" component={Cycle}/>
      </div>
      

    )
 }
}