import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import {
  Link,
} from "react-router-dom";


export default class CycleList extends React.Component {

  constructor(props){
    super(props)
    this.state = {
      data: [
        {
            "id": 1,
            "title": "test"
        },
        {
            "id": 2,
            "title": "2"
        },
        {
            "id": 3,
            "title": "23"
        },
        {
            "id": 4,
            "title": "234"
        }
      ]
    }
  }

  render(){

    return (
      <TableContainer component={Paper}>
        <Table  aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Dessert (100g serving)</TableCell>
              <TableCell align="right">Calories</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.data.map((row) => (
              <TableRow key={row.id}>
                <TableCell component="th" scope="row">
                  <Link to={`/flywheel/cycle/${row.id}`}>{row.title}</Link>
                </TableCell>
                <TableCell >{row.url}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

    )
 }
}