import React from 'react';

export default class Solution extends React.Component {

  render(){
    return <div>方案: {this.props.cycle.solution}</div>
  }
}