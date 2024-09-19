const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  const { url } = req;
  const filePath = process.argv[2];
  if (url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (url === '/students') {
    if (filePath !== null) {
      const message = 'This is the list of our students\n';
      try {
        const students = await countStudents(filePath);
        res.end(`${message}${students.join('\n')}`);
      } catch (error) {
        res.end(`${message}${error.message}`);
      }
    }
  } else {
    res.write('Not Found');
    res.end();
  }
});

app.listen(1245);

module.exports = app;