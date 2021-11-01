# Node.js Note

## **What is Node.js**

According to the Node.js official document.
Node.js is A open-source and cross-platform
**JavaScript runtime environment**. It runs by
the **V8 engine** which is the core of Google Chrome
and outside the browser.

## Different between the exports and module.exports
> ***Whatever you do just keep in mind that module.exports
and NOT exports will be returned from your module when
you're requiring that module from somewhere else.***
- Exports is the reference of the object of the module.exports.

  ```javascript
  module = {}
  module.exports = {}
  exports = module.exports
  exports.a = "hello"
  console.log(module.exports, exports) 	
  // { a: 'hello' } { a: 'hello' }
  exports = "world"
  console.log(module.exports, exports) 	
  // { a: 'hello' } world
  ```

  ```javascript
  module.exports.a = function () {}
  console.log(module.exports, exports)
  // { a: [Function (anonymous)] } 
  // { a: [Function (anonymous)] }
  exports.b = function () {}
  console.log(module.exports, exports)
  // { a: [Function (anonymous)], b: [Function (anonymous)] } 
  // { a: [Function (anonymous)], b: [Function (anonymous)] }
  exports = function () {}
  console.log(module.exports, exports)
  // { a: [Function (anonymous)], b: [Function (anonymous)] } 
  // [Function: exports]
  ```
