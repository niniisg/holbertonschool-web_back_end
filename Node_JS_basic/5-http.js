const http = require('http');
const countStudents = require('./3-read_file_async');

//const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    let dbInfo = 'This is the list of our students\n';

    try {
      const studentData = await countStudents(process.argv[2]);
      dbInfo += studentData;
      res.end(dbInfo);
    } catch (err) {
      dbInfo += 'Cannot load the database';
      res.end(dbInfo);
    }
  } else {
    res.statusCode = 404;
    res.end('404 Not Found');
  }
});

app.listen(port);

module.exports = app
