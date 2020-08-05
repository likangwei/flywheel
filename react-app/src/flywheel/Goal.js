import React from 'react';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import axios from 'axios'
import RoadBlock from './RoadBlock'


export default class Goal extends React.Component {

  constructor(props){
    super(props)
    this.state = {
      goal: props.goal
    }
  }

  save(){
    let self = this
    let {id, title} = this.state.goal
    console.log(this.state.goal)
    axios.put(`/replay/goal/${id}/`, {title: title})
      .then(function (response) {
        console.log(response);
        if(response.status === 200){
          self.setState({goal: response.data})
        }
      })
      .catch(function (error) {
        console.log(error);
        alert(JSON.stringify(error))
    });
  }

  handleChange(event){
    let goal = {...this.state.goal}
    goal.title = event.target.value
    this.setState({goal});
  };

  render(){
    let blocks = this.state.goal.blocks
    return (
        <div>
          <TextField
            multiline
            label="目标"
            type="text"
            onChange={(e)=>this.handleChange(e)}
            defaultValue={this.props.goal.title}
          />;
          <Button
            variant="contained"
            onClick={()=>this.save()}
          >保存</Button>
          <button>添加障碍</button>
          {
            blocks.map(function(b){
              return <RoadBlock key={`b${b.id}`} block={b}></RoadBlock>
            })
          }
          
        </div>
    )
  }
}