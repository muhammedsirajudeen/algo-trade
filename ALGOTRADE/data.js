import require
import fetch from 'node-fetch'
globalThis.fetch = fetch
url = 'https://example.com';

fetch(url)
.then(res => res.json())
.then((out) => {
  console.log('Checkout this JSON! ', out);
})
.catch(err => { throw err });