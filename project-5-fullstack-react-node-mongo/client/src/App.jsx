import { useEffect, useState } from "react";

export default function App() {
  const [msg, setMsg] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000")
      .then(res => res.text())
      .then(setMsg)
      .catch(err => setMsg("API not reachable"));
  }, []);

  return <h1>React + Node + Mongo App: {msg}</h1>;
}

