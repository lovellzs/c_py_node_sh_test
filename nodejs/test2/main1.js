//main.js
var mod = require('./lib');

console.log(mod.counter);  // 3
mod.incCounter();
console.log(mod.counter); // 3
mod.storage.name='zhangsan'
console.log(mod.storage); // 3


// main.js
// import { counter, incCounter } from './lib';
// console.log(counter); // 3
// incCounter();
// console.log(counter); // 4