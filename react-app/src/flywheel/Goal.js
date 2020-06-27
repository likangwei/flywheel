import React from 'react';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import { InputLabel } from '@material-ui/core';
import Button from '@material-ui/core/Button';
import axios from 'axios'


export default class Goal extends React.Component {

  constructor(props){
    super(props)
    this.state = {
      id: props.goal.id || null,
      title: props.goal.title,
    }
  }

  save(){
    let self = this
    let {id, title} = this.state
    axios.put(`/replay/goal/${id}/`, {title: title})
      .then(function (response) {
        console.log(response);
        if(response.status == 200){
          self.setState({title: response.data.title})
        }
      })
      .catch(function (error) {
        console.log(error);
        alert(JSON.stringify(error))
    });
  }

  handleChange(event){
    this.setState({title: event.target.value});
  };

  render(){
    let {id, title} = this.state
    return (
        <div>
          <TextField
            multiline
            label="目标"
            type="text"
            onChange={(e)=>this.handleChange(e)}
            value={this.state.title}
          />;
          <Button
            variant="contained"
            onClick={()=>this.save()}
            disable={id != null}
          >保存</Button>
        </div>
    )
  }
}