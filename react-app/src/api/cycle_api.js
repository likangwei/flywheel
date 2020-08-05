import axios from 'axios'

const HOST = ''

export function fetchCycle(id, suc, fail){
  let url = `${HOST}/replay/cycle/${id}`

  axios.get(url)
    .then(function(rsp){
      if(rsp.status === 200){
      	suc(rsp.data)
      }else{
      	fail(rsp)
      }
      
    })
    .catch(function(err){
      fail(err)
    }).then(function(){
      // alway exec
    })

}