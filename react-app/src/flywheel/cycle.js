import React from 'react';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Goal from './Goal'
import RootCase from './RootCase'
import RoadBlock from './RoadBlock'
import Solution from './Solution'
import Execute from './Execute'

import {fetchCycle} from '../api/cycle_api'

class Cycle extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      cycle: {
        goals: [],
        roadBlock: {id: 1, title: "不知道怎么帮"},
        diagnoseRootCase: "分析不出来..",
        solution: "so",
        execute: "do"
      }
     }
  }

  componentDidMount(){
    let id = this.props.match.params.id
    let self = this
    fetchCycle(id, function(data){
      console.log(data)
      self.setState({cycle: data})
    }, function(err){
      console.log(err)
    })
  }

  render(){
    let id = this.props.match.params.id
    let {cycle} = this.state
    return (
        <div>
         id: {id}, data: {JSON.stringify(cycle)}
         <button>添加目标</button>
         <GridList cols={1}>
            {
              cycle.goals.map(function(goal){
                return (
                  <GridListTile key={`goal{goal.id}`} cols={1}><Goal goal={goal}/></GridListTile>
                )
              })
            }
          
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
        </div>
        
    );
  }
}

export default Cycle;
