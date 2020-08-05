import React from 'react';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import axios from 'axios'


export default class RoadBlock extends React.Component {

  constructor(props){
    super(props)
    this.state = {
      block: props.block
    }
  }

  save(){
    let self = this
    let {id} = this.state.block
    axios.put(`/replay/road_block/${id}/`, this.state.block)
      .then(function (response) {
        console.log(response);
        if(response.status === 200){
          self.setState({block: response.data})
        }
      })
      .catch(function (error) {
        console.log(error);
        alert(JSON.stringify(error))
    });
  }

  handleChange(event){
    let block = {...this.state.block}
    block.title = event.target.value
    this.setState({block});
  };

  render(){
    let {title} = this.state.block

    return (
        <div>
          <TextField
            multiline
            label="障碍"
            type="text"
            onChange={(e)=>this.handleChange(e)}
            value={title}
          />;
          <Button
            variant="contained"
            onClick={()=>this.save()}
          >保存</Button>
          <button>分析根本原因</button>
        </div>
    )
  }
}