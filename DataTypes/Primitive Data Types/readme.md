## **JavaScript Composite (Non-Primitive) Data Types Course**

### **1. Introduction to Composite Data Types**

Composite data types in JavaScript can store multiple values and are mutable, meaning their contents can be changed. The primary composite data types in JavaScript are:

1. **Object**
2. **Array**
3. **Function**
4. **Date**
5. **RegExp**
6. **Map**
7. **Set**
8. **WeakMap**
9. **WeakSet**

### **2. Object**

**Definition:** Objects are collections of key-value pairs where keys are strings (or Symbols) and values can be of any type.

**Examples:**

```javascript
let person = {
 name: 'Alice',
 age: 30,
 greet: function () {
  return `Hello, my name is ${this.name}`
 },
}
```

**Real-World Usage:**

- **Data storage:** Used to store and manage related data.
- **Configuration settings:** Storing application configuration options.
- **Modeling entities:** Representing real-world entities with properties and methods.

**Common Methods:**

- `Object.keys(obj)`: Returns an array of the object's own enumerable property names.
- `Object.values(obj)`: Returns an array of the object's own enumerable property values.
- `Object.entries(obj)`: Returns an array of the object's own enumerable property `[key, value]` pairs.

```javascript
console.log(Object.keys(person)) // ["name", "age", "greet"]
console.log(Object.values(person)) // ["Alice", 30, function]
console.log(Object.entries(person)) // [["name", "Alice"], ["age", 30], ["greet", function]]
```

### **3. Array**

**Definition:** Arrays are ordered collections of values, where each value is identified by an index.

**Examples:**

```javascript
let numbers = [1, 2, 3, 4, 5]
let mixed = [1, 'two', { three: 3 }, [4]]
```

**Real-World Usage:**

- **Lists and collections:** Managing ordered lists of items.
- **Data manipulation:** Performing operations like sorting, filtering, and mapping.
- **Iteration:** Looping through items for processing or display.

**Common Methods:**

- `push(element)`: Adds an element to the end of an array.
- `pop()`: Removes the last element from an array.
- `shift()`: Removes the first element from an array.
- `unshift(element)`: Adds an element to the beginning of an array.
- `map(callback)`: Creates a new array with the results of calling a function on every element.
- `filter(callback)`: Creates a new array with all elements that pass the test implemented by the provided function.

```javascript
let arr = [1, 2, 3]
arr.push(4) // [1, 2, 3, 4]
arr.pop() // [1, 2, 3]
arr.shift() // [2, 3]
arr.unshift(0) // [0, 2, 3]
let squared = arr.map(x => x * x) // [0, 4, 9]
let even = arr.filter(x => x % 2 === 0) // [2]
```

### **4. Function**

**Definition:** Functions are objects that can be invoked to perform tasks or calculations.

**Examples:**

```javascript
function add(a, b) {
 return a + b
}

const multiply = (a, b) => a * b
```

**Real-World Usage:**

- **Encapsulation:** Grouping related code into reusable functions.
- **Event handling:** Handling user interactions and other events.
- **Callbacks and promises:** Managing asynchronous operations.

**Common Methods:**

- `Function.prototype.call()`: Calls a function with a given `this` value and arguments provided individually.
- `Function.prototype.apply()`: Calls a function with a given `this` value and arguments provided as an array.
- `Function.prototype.bind()`: Creates a new function that, when called, has its `this` keyword set to the provided value.

```javascript
function greet(name) {
 console.log(`Hello, ${name}`)
}

greet.call(null, 'Alice') // "Hello, Alice"
greet.apply(null, ['Bob']) // "Hello, Bob"

const greetAlice = greet.bind(null, 'Alice')
greetAlice() // "Hello, Alice"
```

### **5. Date**

**Definition:** The `Date` object represents dates and times.

**Examples:**

```javascript
let now = new Date()
let birthday = new Date('1990-01-01')
```

**Real-World Usage:**

- **Timestamping:** Recording and manipulating dates and times.
- **Scheduling:** Managing and displaying dates for events or tasks.

**Common Methods:**

- `getFullYear()`: Returns the year of the specified date.
- `getMonth()`: Returns the month of the specified date (0-11).
- `getDate()`: Returns the day of the month of the specified date.
- `getDay()`: Returns the day of the week of the specified date (0-6).

```javascript
let date = new Date()
console.log(date.getFullYear()) // Current year
console.log(date.getMonth()) // Current month (0-11)
console.log(date.getDate()) // Current day of the month
console.log(date.getDay()) // Day of the week (0-6)
```

### **6. RegExp**

**Definition:** The `RegExp` object represents a regular expression, used for pattern matching within strings.

**Examples:**

```javascript
let regex = /hello/i // Case-insensitive search for "hello"
let testString = 'Hello, world!'
console.log(regex.test(testString)) // true
```

**Real-World Usage:**

- **Validation:** Checking if strings match a particular format (e.g., email addresses).
- **Search and replace:** Finding and replacing text in strings.

**Common Methods:**

- `RegExp.prototype.test()`: Tests if a pattern exists in a string.
- `RegExp.prototype.exec()`: Executes a search for a match and returns the result.

```javascript
let pattern = /(\d+)/
let str = 'There are 123 apples'
let result = pattern.exec(str)
console.log(result[0]) // "123"
console.log(result[1]) // "123"
```

### **7. Map**

**Definition:** A `Map` object holds key-value pairs where both keys and values can be of any type. The keys are ordered.

**Examples:**

```javascript
let map = new Map()
map.set('name', 'Alice')
map.set(1, 'One')
```

**Real-World Usage:**

- **Associative arrays:** Storing and retrieving data with unique keys.
- **Ordering:** Maintaining the order of key-value pairs.

**Common Methods:**

- `Map.prototype.set(key, value)`: Adds or updates an element with a specified key and value.
- `Map.prototype.get(key)`: Returns the value associated with the key.
- `Map.prototype.has(key)`: Returns a boolean indicating whether the map contains the specified key.
- `Map.prototype.delete(key)`: Removes the specified key and its associated value.

```javascript
let map = new Map()
map.set('name', 'Alice')
console.log(map.get('name')) // "Alice"
console.log(map.has('name')) // true
map.delete('name')
console.log(map.has('name')) // false
```

### **8. Set**

**Definition:** A `Set` object lets you store unique values of any type, whether primitive values or object references.

**Examples:**

```javascript
let set = new Set()
set.add(1)
set.add('hello')
set.add(1) // Duplicate value, will be ignored
```

**Real-World Usage:**

- **Unique collections:** Ensuring that elements are unique in a collection.
- **Data validation:** Removing duplicate values from arrays.

**Common Methods:**

- `Set.prototype.add(value)`: Adds a new value to the set.
- `Set.prototype.has(value)`: Checks if a value exists in the set.
- `Set.prototype.delete(value)`: Removes a value from the set.

```javascript
let set = new Set([1, 2, 3])
set.add(4)
console.log(set.has(3)) // true
set.delete(2)
console.log(set.has(2)) // false
```

### **9. WeakMap**

**Definition:** A `WeakMap` is a collection of key-value pairs where keys are objects and values can be of any type. The references to keys are weak, meaning the garbage collector can remove entries if there are no other references to the key.

**Examples:**

```javascript
let weakMap = new WeakMap()
let obj = {}
weakMap.set(obj, 'value')
console.log(weakMap.get(obj)) // "value"
```

**Real-World Usage:**

- **Private data:** Storing private data associated with objects.
- **Memory management:** Automatically cleaning up memory when objects are garbage collected.

**Common Methods:**

- `WeakMap.prototype.set(key, value)`: Adds or updates a key-value pair.
- `WeakMap.prototype.get(key)`: Returns the value associated with the key.
- `WeakMap.prototype.has(key)`: Returns a boolean indicating if the key exists.

```javascript
let weakMap = new Weak()

Map()
let key = {}
weakMap.set(key, 'value')
console.log(weakMap.get(key)) // "value"
```

### **10. WeakSet**

**Definition:** A `WeakSet` is a collection of objects where the references to the objects are weak, meaning that if there are no other references to an object, it can be garbage collected.

**Examples:**

```javascript
let weakSet = new WeakSet()
let obj = {}
weakSet.add(obj)
console.log(weakSet.has(obj)) // true
```

**Real-World Usage:**

- **Tracking objects:** Keeping track of objects without preventing their garbage collection.
- **Non-intrusive storage:** Storing metadata about objects.

**Common Methods:**

- `WeakSet.prototype.add(value)`: Adds an object to the set.
- `WeakSet.prototype.has(value)`: Checks if an object exists in the set.

```javascript
let weakSet = new WeakSet()
let obj = {}
weakSet.add(obj)
console.log(weakSet.has(obj)) // true
```

### **Conclusion**

Composite data types in JavaScript provide powerful ways to manage and manipulate collections of values. Understanding how to use each type effectively will enhance your ability to write efficient and maintainable code. By mastering these data types, you'll be able to handle a wide range of programming tasks and design complex applications.