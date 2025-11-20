const express = require("express");
const mongoose = require("mongoose");
const app = express();

mongoose.connect("mongodb://mongo:27017/testdb");

app.get("/", (req, res) => {
  res.send("API working with MongoDB inside Docker!");
});

app.listen(5000, () => console.log("API running on 5000"));
