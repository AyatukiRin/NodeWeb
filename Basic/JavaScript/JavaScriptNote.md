# JavaScript

## Property access error

> Note: If access a Object have any undefined property it will return undefined. But access the property of **undefined** or **null**, it will return TypeError. To fix that:

```javascript
// Ugly Way
const obj = Object.create(Object.prototype)
if (obj) {
    if (obj.propretyA) {
        console.log(obj.propertyA.propertyB)
    }
}

// Simple Way
console.log(obj && obj.propertyA && obj.propertyA.propertyB)

// ES2020
console.log(obj?.propertyA?.propertyB)
```

## ProtoType Chain And Inheritance

> **Note: **Although the ES2015 have provide the `class` to make a oop like Feature, but it just a syntactical sugar base on JavaScript **ProtoType Chain**.

### Constructor Function

### Inheritance

- Object.create

	 ```javascript
	 var o = {
		 a: 2,
		 m: function() {
			 return this.a + 1;
		 }
	 };
	 
	 console.log(o.m()); // 3
	 // When calling o.m in this case, 'this' refers to o
	 
	 var p = Object.create(o);
	 // p is an object that inherits from o
	 
	 p.a = 4; // creates a property 'a' on p
	 console.log(p.m()); // 5
	 // when p.m is called, 'this' refers to p.
	 // So when p inherits the function m of o,
	 // 'this.a' means p.a, the property 'a' of p
	 
	```

### Prototype

- Function.prototype.call()
	```javascript
		function ProtolTypeCall() {
			const slicedArray = [].slice.call(arguments, 0, 3)
			console.log(slicedArray)
		}
		ProtolTypeCall(1,2,3,4,5,6,7,8,9)
		// [1,2,3]
	```
- Object.setPrototypeOf (obj, prototype)

## [Regular expressions](https://regex101.com/)

## Array.prototype.entries

Just same as the Python method: **enumerate**

```python
# Python
for key, value in enumerate({a:1}):
	print(key, value)
```

```javascript
// JavaScript
for (const [key, value] of Object.entries({a: 1})) {
    console.log(`${key}: ${value}`)
}
```

## Reference Object

- Object.assign ( targetObject, SourceObject1, SourceObject2......)  **[Shadow Copy]**

	**Notice:** This method of protocol type Object is like a iterator that make the target Object's prop which has same
	name as the source object and make its value equal the source Object's props value.

	> It will cause that if the first layer of the targetObject have the Object type properties (**Array is Object too **)then which will be the source Object's reference that can sync the value between each other.

	**Always Remember that the Object is reference of Object**

	```javascript
	// It's werid if copy all code below it will only show the final result that the target Object already changed.
	
			let a = {referenceObj : {}}
			let b = {referenceObjProp : {test: 1}, CopyProp:1}
	
			// In browser type the code below by order
			Object.assign(a,b)
			console.log(a) // {referenceProp: {test : 1}, CopyProp: 1}
			a.referenceProp.test = 2
			console.log(a) // {referenceProp: {test: 2}, CopyProp: 1}
			console.log(b) // {referenceProp: {test: 2}, CopyProp: 1}
			a.CopyProp = 2 // Here will be a copy
			console.log(a) // {referenceProp: {test: 2}, CopyProp: 2}
			console.log(b) // {referenceProp: {test: 2}, CopyProp: 1}
			
	```

- https://stackoverflow.com/questions/122102/what-is-the-most-efficient-way-to-deep-clone-an-object-in-javascript

Notice All the JavaScript Object is the reference of the proto type. As the code below.

```javascript
let a = {a: 1}	// same as let a = new Object(a,1)
```

## MutationObserver

Create a MutationObserver for the DOM to watch the DOM's mutation. (i.e. the Api for the MutaionObserver can custom the
config of the Object watch)

```html

<div class="bg-danger" id="app">
    <p id="test">test</p>
</div>

<script>
    let target = document.getElementById("app")
    let config = {
        childList: true,
        attributes: true
    }
    let observer = new MutationObserver(function (MutationList) {
        for (const mutationRecord of MutationList) {
            if (mutationRecord.type === "childList") {
                console.log("The childList you Observed have been changed")
            }
            if (mutationRecord.type === "attributes") {
                console.log("The attributes you Observed have been changed")
            }
            console.log(mutationRecord)
        }
    })
    observer.observe(target, config)

    document.getElementById("test").addEventListener('click', (event) => {
        target.append("Append", document.createElement('p'))
        target.className = "bg-primary"
    })
</script>
```

## Destructuring assignment

The **destructuring assignment** syntax is a JavaScript expression that makes it possible to unpack values from arrays,
or properties from objects, into distinct variables.

```javascript
let a, b, rest;
[a, b] = [10, 20];

console.log(a);
// expected output: 10

console.log(b);
// expected output: 20

[a, b, ...rest] = [10, 20, 30, 40, 50];

console.log(rest);
// expected output: Array [30,40,50]

const testObj = {
    Key1: "KEY1",
    Key2: "KEY2",
    Key3: "KEY3",
    Key4: "KEY4",
}

const {Key3, ...testObjWIthoutKey3} = testObj

console.log(Key3, testObjWIthoutKey3)
// KEY3 { Key1: 'KEY1', Key2: 'KEY2', Key4: 'KEY4' }
```

### Spread syntax

**Note: **Spread syntax is same as Object.assign that if use both of that to compact a object type variable which have
the object prop, it will be reference to another variable.

```javascript
let obj1 = {objLikeProp: {prop: "prop"}, prop2: "prop2"}
let obj2 = Object.assign({}, obj1)

console.log(obj2)
// {objLikeProp: {prop: "prop"}, prop2: "prop2"}

obj2.objLikeProp.prop = "Change the value in objectProp from Object"

console.log(obj2)
// {objLikeProp: {prop: "change.."}, prop2: "prop2"}

console.log(obj1)
// {objLikeProp: {prop: "change.."}, prop2: "prop2"}

=== === === === === === === === === === === === === === ===
let
obj3 = {...obj1} // Same as Object.assign
```

## Async/Await

Keep in mind that the asynchronous function will be add to the Event queue and waiting for the main thread to finished.
And if the asynchronous function have included another function it will be show the feature like below. **(
DataStructure)**

```javascript
// First Queue
setTimeout(() => {
    console.log("Queue First")

    // Third Queue
    setTimeout(() => {
        console.log("Queue Third")
    }, 0)
}, 0)

// Second Queue
setTimeout(() => {
    console.log("Queue Second")
}, 0)

// Queue First
// Queue Second
// Queue Third

```

### Async Function

> **Description:**
>
> Async functions can contain **0** or **More** <u>await</u> expressions. Await expressions make promise-returning functions behave as though they're synchronous by suspending execution until the **returned promise is fulfilled or rejected.** The resolved value of the promise is treated as the return value of the await  expression Use of `async` and `await` enables the use of ordinary `try/catch` blocks around asynchronous code.
>
> **Notice:**
>
> - The `await` keyword is only valid inside async functions within regular JavaScript code. If you use it outside of an async function's body, you will get a `SyntaxError`.
>
> 	**`await` can be used on its own with JavaScript Modules**.
>
> - The purpose of `async/await` is to simplify the syntax necessary to consume promise-based APIs. The behavior of `async/await` is simliar to combining generators and promises.
>
> Async functions **always return a promise.** If the return value of an async function is not explicitly a promise, **it will be implicitly wrapped in a promise.**

```javascript
function resolveAfter2Second() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("2 Second passed, and function return resloved.")
        }, 2000)
    })
}

async function asyncFunc() {
    console.log("You call the async function.");

    const response = await resolveAfter2Second()
    console.log(response)

    console.log("End the Async Function!")

    // return "reslove msg" // Implicitly wrapped to Promise.reslove("reslove msg")
    return Promise.reject("Oh!Error!")
}

asyncFunc()
    .then(resolvedMsg => {
        console.log(resolvedMsg)
    })
    .catch(ErrorMsg => {
        console.log(ErrorMsg)
    })
    .finally( ()=> {
        console.log("asyncFunc's returned promise have done.")
    })

```



Function execution order of `async`





## Web API

- File Download

	```javascript
	function download(content, fileName, contentType) {
			var a = document.createElement("a");
			var file = new Blob([content], {type: contentType});
			a.href = URL.createObjectURL(file);
			a.download = fileName;
			a.click();
	}
	download(jsonData, 'json.txt', 'text/plain');	
	```

- Blob (Binary Large Object)

- FileSystemHandle
