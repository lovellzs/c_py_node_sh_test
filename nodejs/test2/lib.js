// lib.js
var counter = 3;
function incCounter() {
  counter++;
}
module.exports = {
  counter: counter,
  incCounter: incCounter,
  storage:{}
};


// lib.js
// var counter = 3;
// function incCounter() {
//   counter++;
// }
// module.exports = {
//   get counter() {
//     return counter
//   },
//   incCounter: incCounter,
// };

// var counter = 3;
// function incCounter() {
//   counter++;
// }

// export {counter , incCounter}