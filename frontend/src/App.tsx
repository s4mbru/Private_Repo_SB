import { useEffect, useState } from "react"
import { io, Socket } from "socket.io-client"
import "./App.css"

const socket: Socket = io("http://localhost:5555", {
  transports: ["websocket"],
})

function App() {
  const [status, setStatus] = useState("Connecting...")

  useEffect(() => {
    socket.on("connect", () => {
      console.log("Connected to backend")
      setStatus("Connected to backend")
    })

    socket.on("status", (data) => {
      console.log("Status:", data.message)
      setStatus(data.message)
    })

    socket.on("error", (data) => {
      console.error("Error:", data.message)
      setStatus(`Error: ${data.message}`)
    })

    return () => {
      socket.off("connect")
      socket.off("status")
      socket.off("error")
    }
  }, [])

  const sendCommand = (command: string) => {
    console.log("Sending:", command)
    socket.emit("run_command", { command })
  }

  return (
    <div className="app">
      <h1>Finch Control Panel</h1>

      <p className="status">{status}</p>

      <div className="movement">
        <button onClick={() => sendCommand("forward")}>↑</button>
        <div>
          <button onClick={() => sendCommand("left")}>←</button>
          <button onClick={() => sendCommand("right")}>→</button>
        </div>
        <button onClick={() => sendCommand("turnaround")}>↓</button>
      </div>

      <div className="shapes">
        <button onClick={() => sendCommand("circle")}>Circle</button>
        <button onClick={() => sendCommand("wave")}>Wave</button>
        <button onClick={() => sendCommand("line")}>Line</button>
        <button onClick={() => sendCommand("triangle")}>Triangle</button>
      </div>

      <div className="weather">
        <button onClick={() => sendCommand("temperature")}>
          Temperature
        </button>
      </div>
    </div>
  )
}

export default App