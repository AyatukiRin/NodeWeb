# Vue-Note

## **Vue Computed and the Methods**

Computed property always create Getter/Setter function for itself. **Computed properties are cached based on their reactive dependencies**. This means as long as **data** have not changed, multiple access to the properties function will immediately return the **<u>Previously</u>** computed result without having to run the setter in that function. In comparison, a method invocation will **always** run the function whenever a re-render happens.

```javascript
let test = new Vue({
    data: {
        param: 1
    },
    methods: {
        foo1: function () {
            return Date.now()
        }
    },
    computed: {
        foo2: function () {
            // It will be Getter only
            return this.param
        },
        foo3: {
            get: function () {
                return this.param
            },
            set: function (num) {
                this.param = num
            }
        },
        foo4: function () {
            // It will always show the previous data seted before
            return Date.now()
        }
    }
})
test.foo1		// => Date.now
test.foo4		// => Previous Date.now
test.foo2		// => 1
test.foo3 = 2	// => set param = 2
test.foo3		// => 2
```

## Add responsive data after create a instance of Vue

Use $set method to set a responsive data after create a instance of Vue. But it is not recommend behavior. Just let the every data you will use into the initialize of Vue instance.

## Front-end Template Framwork:

It hava serval template framwork for the Front-end develop. Just see the document address below and try to memorize how it works.

[Document of Mystanche.js](http://mustache.github.io/)

## V-model

## Just known V-model is the simplify way of the children component to pass the data or

sync the data by the props from the parents.

```javascript
<conditionInput v-model="inputValue" />
// Same as below
<input :value="inputValue" @input="inputValue = $event.target.value" />
```

## Local Component Register

Use `Vue.component("componentName", { /* ... */ })` to register the global component.

To register a local component, **notice that the component only available in the vue instance which you register component in it**.

- Use `components` API to register  a local component in Vue instance.

  ```javascript
  let vm = new Vue({
      // ...
      components: {
          componentName: {
              // component property
          }
      }
  })
  ```



## Provide and inject from parent to child

Pass the **static variable** which type is String and remember that the Provide/inject binding are **NOT reactive**.

>  Note: the `provide` and `inject` bindings are NOT reactive. This is intentional. However, if you pass down an observed object, properties on that object do remain reactive.

```javascript
let parent = {
    // provide should be a object or a function return a object
    provide() {
        return {
            parentData: 'Data from parent'
        }
    }
}

let child = {
    // inJect can be a Array or a Object that can have two property from and default.
    Arrayinject: ['parentData']
    Objectinject: {
    	// the from property is the key (string or Symbol) to search for in available injections, and the default property is used as fallback value
    	CustomName: {
			from: "parentData",
    		default: "Default Data" 
		}
	}
}
```



## KeepAlive with Dynamic Components

## Slot

- Named Slot
- SlotProps
- Fall Back Slot Content

## How to fix “Avoid mutating a prop directly” in Vue

Always keep in mind that the  Vue is  **one-way data binding** from parent to child used the prop. And the child emit the event to the parent to change the data.

```javascript
ParentComponent = {
	data: {
		parentData: "parentData"
	}
}

ChildComponent = {
	props: [value],
	computed: {
		childData: {
			get() {
				return this.value
			},
			set(newValue) {
				this.$emit("input", newValue)
			}
		}
	}
}

<parent>
	<chid v-model="parentData"></child>
</parent>
```

## Vue.$watch

### Official Documentation (2.x)

> vm.$watch( exp/Fn, callback, [options])
>
> - Arguments:
>
> 	- {string | Function } expOrFn
>
> 	- {Function | Object } callback
>
> 	- {Object } [ options ]
>
> 		- {boolean } deep 
>
> 			> **To also detect nested value changes inside Objects, Note that you don't need to do so to listen for Array mutations.**
> 			>
> 			> **Notice: Only watch deep one layer**
>
> 		- {boolean } immediate
>
> 			> **Immediate fired the callback function with the current value of the expression.**
>
> - Returns: {Function} unwatch
>
> 	> **To stop firing the callback:**
> 	>
> 	> ```javascript
> 	> var unwatch = vm.$watch("someValue", callback)
> 	> // later, teardown the watcher
> 	> unwatch()
> 	> ```
> 	>
> 	> 

### [Watch the children component reference](https://stackoverflow.com/questions/39035498/vuejs-watch-refs/45011980)

```javascript
const Counter = {
  data: () => ({
    i: 0
  }),
  template: `<fieldset>
    <p>Counter</p>
    <code>i = {{ i }}</code>
    <button @click="i += 1"> Add One </button>
  </fieldset>`
}

const App = {
  components: { Counter },
  mounted () {
    this.$watch(
    	() => {
    		return this.$refs.counter.i
    	},
      (val) => {
        alert('App $watch $refs.counter.i: ' + val)
      }
    )
  },
  template: `<fieldset>
    <p>App</p>
    <counter ref="counter" />
  </fieldset>`
}

new Vue({
	el: '#app',
	render: h => h(App)
})
```



## What is Vue.$attrs

> - **Type:**	{ [ key : string ] : string }
>
> - **Read only**
>
> - **Details:**
    >
    > 	Contains parent-scope attribute bindings (except for `class` and `style`) that are not recognized (and extracted) as props. When a component doesn’t have any declared props, this essentially contains all parent-scope bindings (except for `class` and `style`), and can be passed down to an inner component via `v-bind="$attrs"` - useful when creating higher-order components.

##  [Programmatic Event Listeners](https://vuejs.org/v2/guide/components-edge-cases.html#Programmatic-Event-Listeners)

## Non-Attribute property

>  Note that `inheritAttrs: false` option does **not** affect `style` and `class` bindings.

## Option/Misc: Model

## [Accessing Child Component Instances & Child Elements](https://vuejs.org/v2/guide/components-edge-cases.html#Accessing-Child-Component-Instances-amp-Child-Elements)

Vm.$refs.focus()

## [Filters](https://vuejs.org/v2/guide/filters.html)
