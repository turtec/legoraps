const axios = require('axios')
const path = 'http://192.168.178.37:9006/'
//const path = 'http://localhost:9003/'

export const moveRight = () => {
  axios.get(path+'move/right').then((res) => {
    console.log(`statusCode: ${res.statusCode}`)
    console.log(res)
  })
  .catch((error) => {
    console.error(error)
  })
}

export const moveLeft = () => {
  axios.get(path+'move/left').then((res) => {
    console.log(`statusCode: ${res.statusCode}`)
    console.log(res)
  })
  .catch((error) => {
    console.error(error)
  })
}

export const moveForward = () => {
  axios.get(path+'move/forward').then((res) => {
    console.log(`statusCode: ${res.statusCode}`)
    console.log(res)
  })
  .catch((error) => {
    console.error(error)
  })
}

export const moveBackward = () => {
  axios.get(path+'move/backward').then((res) => {
    console.log(`statusCode: ${res.statusCode}`)
    console.log(res)
  })
  .catch((error) => {
    console.error(error)
  })
}

export const moveStop = () => {
  axios.get(path+'move/stop').then((res) => {
    console.log(`statusCode: ${res.statusCode}`)
    console.log(res)
  })
  .catch((error) => {
    console.error(error)
  })
}

