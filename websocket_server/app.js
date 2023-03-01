const WebSocket = require('ws')

const wss = new WebSocket.Server({ port: 8088 })


wss.broadcast = function broadcast(data) {
  wss.clients.forEach((client) => {
    client.send(data)
  })
}

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    try {
      wss.broadcast(message)
    }
    catch (err) {
      console.log(err)
    }
  })
