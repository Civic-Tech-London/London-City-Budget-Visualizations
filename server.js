const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/data', (req, res) => {
  const jsonFilePath = path.join(__dirname, 'budget.json');
  fs.readFile(jsonFilePath, 'utf8', (err, data) => {
    if (err) {
      res.status(500).send('Error reading the JSON file');
      return;
    }
    res.send(data);
  });
});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.get('/gross-op-expend', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'gross-op-expend.html'));
});

app.get('/other-revenues', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'other-revenues.html'));
});

app.get('/levy-supported-operating', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'levy-supported-operating.html'));
});

app.get('/total-cap-expenditures', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'total-cap-expenditures.html'));
});

app.get('/fte', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'fte.html'));
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});


