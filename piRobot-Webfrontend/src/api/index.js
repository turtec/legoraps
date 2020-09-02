const axios = require('axios')
const path = 'http://localhost:9003/'


export const moveRight = () => {
  console.log('api move Right')
  console.log(path)
  axios.get(path+'comtest').then((res) => {
    console.log(`statusCode: ${res.statusCode}`)
    console.log(res)
  })
  .catch((error) => {
    console.error(error)
  })
}

export const moveLeft = () => {
  console.log('move Left')
}