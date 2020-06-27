import React from 'react';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import { InputLabel } from '@material-ui/core';
import Button from '@material-ui/core/Button';
import axios from 'axios'
import Goal from './Goal'
import RootCase from './RootCase'
import RoadBlock from './RoadBlock'
import Solution from './Solution'
import Execute from './Execute'


class Cycle extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      cycle: {
        goal: {id: 1, title: "帮大家更好的成长"},
        roadBlock: {id: 1, title: "不知道怎么帮"},
        diagnoseRootCase: "分析不出来..",
        solution: "so",
        execute: "do"
      }
     }
  }

  render(){
    return (
        <GridList cellHeight={100} cols={1}>
          <GridListTile cols={1}>
            <div><Goal goal={this.state.cycle.goal}/></div>
          </GridListTile>
          <GridListTile cols={1}>
            <RoadBlock roadBlock={this.state.cycle.roadBlock} cycle={this.state.cycle}/>
          </GridListTile>
          <GridListTile cols={1}>
            <RootCase cycle={this.state.cycle}/>
          </GridListTile>
          <GridListTile cols={1}>
            <Solution cycle={this.state.cycle}/>
          </GridListTile>
          <GridListTile cols={1}>
            <Execute cycle={this.state.cycle}/>
          </GridListTile>
        </GridList>
    );
  }
}

export default Cycle;
