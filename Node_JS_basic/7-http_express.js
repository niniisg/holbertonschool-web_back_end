const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const path = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const msg = 'This is the list of our students\n';
  try {
    const students = await countStudents(path);
    res.send(`${msg}${students.join('\n')}`);
  } catch (err) {
    res.send(`${msg}${err.message}`);
  }
});

app.listen(port);

module.exports = app;
