const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(process.cwd());
const types = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8'
};

http.createServer((req, res) => {
  let pathname;
  try { pathname = decodeURIComponent(new URL(req.url, 'http://127.0.0.1').pathname); }
  catch { res.writeHead(400).end('Bad request'); return; }
  const target = path.resolve(root, '.' + pathname);
  if (target !== root && !target.startsWith(root + path.sep)) {
    res.writeHead(403).end('Forbidden');
    return;
  }
  fs.stat(target, (err, stat) => {
    const file = err ? path.join(root, 'index.html') : (stat.isDirectory() ? path.join(target, 'index.html') : target);
    fs.readFile(file, (readErr, data) => {
      if (readErr) { res.writeHead(404).end('Not found'); return; }
      res.writeHead(200, { 'Content-Type': types[path.extname(file)] || 'application/octet-stream' });
      res.end(data);
    });
  });
}).listen(4173, '127.0.0.1');
