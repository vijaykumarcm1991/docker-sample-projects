const express = require("express");
const app = express();
app.get("/", (req, res) => res.send("Hello from Node.js behind NGINX reverse proxy!"));
app.listen(3000);