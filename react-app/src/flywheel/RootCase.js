import React from 'react';

export default class RootCase extends React.Component {

  render(){
    return <div>根本原因: {this.props.cycle.diagnoseRootCase}<button>添加解决方案</button></div>
  }
}