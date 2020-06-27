import React from 'react';

export default class RootCase extends React.Component {

  render(){
    return <div>分析原因: {this.props.cycle.diagnoseRootCase}</div>
  }
}