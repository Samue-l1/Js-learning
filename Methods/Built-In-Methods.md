### JavaScript Built-In Methods: An In-Depth Guide

JavaScript is a versatile and powerful language, known for its ability to manipulate data and perform various tasks efficiently. A significant part of this efficiency comes from its built-in methods. These methods are predefined functions that perform specific tasks, and they are associated with different data types such as strings, arrays, objects, numbers, and more. Understanding these built-in methods is crucial for writing clean, efficient, and maintainable code.

Below is an in-depth look at JavaScript's built-in methods, their usage, and common use cases.

---

### 1. **String Methods**

String methods allow manipulation of text data. Strings are immutable in JavaScript, meaning any operation on a string creates a new string rather than altering the original.

#### **Common String Methods:**

- **`length`**: Returns the length of the string.

  ```javascript
  let str = 'Hello World!'
  console.log(str.length) // Output: 12
  ```

- **`toUpperCase()`**: Converts the entire string to uppercase.

  ```javascript
  let str = 'hello'
  console.log(str.toUpperCase()) // Output: "HELLO"
  ```

- **`toLowerCase()`**: Converts the entire string to lowercase.

  ```javascript
  let str = 'HELLO'
  console.log(str.toLowerCase()) // Output: "hello"
  ```

- **`includes()`**: Checks if a string contains a specified value.

  ```javascript
  let str = 'Hello World!'
  console.log(str.includes('World')) // Output: true
  ```

- **`slice()`**: Extracts a section of a string and returns it as a new string.

  ```javascript
  let str = 'Hello World!'
  console.log(str.slice(0, 5)) // Output: "Hello"
  ```

- **`substring()`**: Similar to `slice()`, but does not accept negative indices.

  ```javascript
  let str = 'Hello World!'
  console.log(str.substring(0, 5)) // Output: "Hello"
  ```

- **`replace()`**: Replaces a specified value with another value in a string.
  ```javascript
  let str = 'Hello World!'
  console.log(str.replace('World', 'JavaScript')) // Output: "Hello JavaScript!"
  ```

#### **Use Cases:**

- **Formatting User Input**: Convert user input to lowercase for consistent storage.
- **Searching within Text**: Check if a keyword exists within a user’s comment or a string.

### 2. **Array Methods**

Arrays are used to store multiple values in a single variable. JavaScript provides various methods to manipulate arrays.

#### **Common Array Methods:**

- **`length`**: Returns the number of elements in an array.

  ```javascript
  let arr = [1, 2, 3, 4]
  console.log(arr.length) // Output: 4
  ```

- **`push()`**: Adds new items to the end of an array.

  ```javascript
  let arr = [1, 2, 3]
  arr.push(4)
  console.log(arr) // Output: [1, 2, 3, 4]
  ```

- **`pop()`**: Removes the last element from an array.

  ```javascript
  let arr = [1, 2, 3]
  arr.pop()
  console.log(arr) // Output: [1, 2]
  ```

- **`shift()`**: Removes the first element from an array.

  ```javascript
  let arr = [1, 2, 3]
  arr.shift()
  console.log(arr) // Output: [2, 3]
  ```

- **`unshift()`**: Adds new items to the beginning of an array.

  ```javascript
  let arr = [2, 3]
  arr.unshift(1)
  console.log(arr) // Output: [1, 2, 3]
  ```

- **`map()`**: Creates a new array by calling a function on every element of the original array.

  ```javascript
  let arr = [1, 2, 3]
  let doubled = arr.map(x => x * 2)
  console.log(doubled) // Output: [2, 4, 6]
  ```

- **`filter()`**: Creates a new array with elements that pass the test implemented by the provided function.

  ```javascript
  let arr = [1, 2, 3, 4]
  let evens = arr.filter(x => x % 2 === 0)
  console.log(evens) // Output: [2, 4]
  ```

- **`reduce()`**: Executes a reducer function on each element of the array, resulting in a single output value.

  ```javascript
  let arr = [1, 2, 3, 4]
  let sum = arr.reduce((acc, val) => acc + val, 0)
  console.log(sum) // Output: 10
  ```

- **`find()`**: Returns the first element that satisfies the provided testing function.
  ```javascript
  let arr = [1, 2, 3, 4]
  let firstEven = arr.find(x => x % 2 === 0)
  console.log(firstEven) // Output: 2
  ```

#### **Use Cases:**

- **Data Transformation**: Use `map()` to transform an array of objects into a different format.
- **Filtering Data**: Use `filter()` to create a subset of an array based on certain conditions.
- **Summarizing Data**: Use `reduce()` to calculate the total or average of numerical data.

### 3. **Object Methods**

Objects are used to store collections of data in the form of key-value pairs. JavaScript provides several methods to interact with objects.

#### **Common Object Methods:**

- **`Object.keys()`**: Returns an array of the object's own enumerable property names.

  ```javascript
  let obj = { name: 'John', age: 30 }
  console.log(Object.keys(obj)) // Output: ["name", "age"]
  ```

- **`Object.values()`**: Returns an array of the object's own enumerable property values.

  ```javascript
  let obj = { name: 'John', age: 30 }
  console.log(Object.values(obj)) // Output: ["John", 30]
  ```

- **`Object.entries()`**: Returns an array of the object's own enumerable property key-value pairs.

  ```javascript
  let obj = { name: 'John', age: 30 }
  console.log(Object.entries(obj)) // Output: [["name", "John"], ["age", 30]]
  ```

- **`Object.assign()`**: Copies all enumerable own properties from one or more source objects to a target object.

  ```javascript
  let obj1 = { a: 1 }
  let obj2 = { b: 2 }
  let combined = Object.assign({}, obj1, obj2)
  console.log(combined) // Output: { a: 1, b: 2 }
  ```

- **`hasOwnProperty()`**: Returns a boolean indicating whether the object has the specified property.
  ```javascript
  let obj = { name: 'John' }
  console.log(obj.hasOwnProperty('name')) // Output: true
  ```

#### **Use Cases:**

- **Merging Objects**: Use `Object.assign()` to combine multiple objects into one.
- **Iterating Over Properties**: Use `Object.entries()` to loop through an object’s properties and values.

### 4. **Number Methods**

JavaScript provides methods to work with numbers, offering functionality for mathematical calculations, conversions, and more.

#### **Common Number Methods:**

- **`toFixed()`**: Formats a number using fixed-point notation.

  ```javascript
  let num = 5.56789
  console.log(num.toFixed(2)) // Output: "5.57"
  ```

- **`toString()`**: Converts a number to a string.

  ```javascript
  let num = 123
  console.log(num.toString()) // Output: "123"
  ```

- **`parseInt()`**: Parses a string and returns an integer.

  ```javascript
  let numStr = '100'
  console.log(parseInt(numStr)) // Output: 100
  ```

- **`parseFloat()`**: Parses a string and returns a floating-point number.
  ```javascript
  let numStr = '3.14'
  console.log(parseFloat(numStr)) // Output: 3.14
  ```

#### **Use Cases:**

- **Formatting Prices**: Use `toFixed()` to format prices to two decimal places.
- **Parsing User Input**: Use `parseInt()` or `parseFloat()` to convert string input into numbers.

### 5. **Math Methods**

The `Math` object contains various methods for performing mathematical operations.

#### **Common Math Methods:**

- **`Math.random()`**: Returns a pseudo-random number between 0 (inclusive) and 1 (exclusive).

  ```javascript
  console.log(Math.random()) // Output: A random number between 0 and 1
  ```

- **`Math.floor()`**: Rounds a number down to the nearest integer.

  ```javascript
  console.log(Math.floor(5.95)) // Output: 5
  ```

- **`Math.ceil()`**: Rounds a number up to the nearest

integer.

```javascript
console.log(Math.ceil(5.05)) // Output: 6
```

- **`Math.max()`**: Returns the largest of the zero or more numbers given as input.

  ```javascript
  console.log(Math.max(1, 2, 3)) // Output: 3
  ```

- **`Math.min()`**: Returns the smallest of the zero or more numbers given as input.
  ```javascript
  console.log(Math.min(1, 2, 3)) // Output: 1
  ```

#### **Use Cases:**

- **Generating Random Values**: Use `Math.random()` for generating random numbers, e.g., in a lottery application.
- **Rounding Numbers**: Use `Math.floor()` and `Math.ceil()` for rounding numbers in financial calculations.

### 6. **Date Methods**

JavaScript provides a `Date` object to work with dates and times. It offers various methods to handle date and time operations.

#### **Common Date Methods:**

- **`Date()`**: Returns the current date and time.

  ```javascript
  let now = new Date()
  console.log(now) // Output: Current date and time
  ```

- **`getFullYear()`**: Returns the year of the specified date.

  ```javascript
  let now = new Date()
  console.log(now.getFullYear()) // Output: Current year
  ```

- **`getMonth()`**: Returns the month of the specified date (0-11).

  ```javascript
  let now = new Date()
  console.log(now.getMonth()) // Output: Current month (0-11)
  ```

- **`getDate()`**: Returns the day of the month of the specified date (1-31).

  ```javascript
  let now = new Date()
  console.log(now.getDate()) // Output: Current day of the month
  ```

- **`getDay()`**: Returns the day of the week of the specified date (0-6).

  ```javascript
  let now = new Date()
  console.log(now.getDay()) // Output: Current day of the week (0-6)
  ```

- **`getTime()`**: Returns the number of milliseconds since January 1, 1970, 00:00:00 UTC.

  ```javascript
  let now = new Date()
  console.log(now.getTime()) // Output: Milliseconds since January 1, 1970
  ```

- **`setDate()`**: Sets the day of the month for a specified date.
  ```javascript
  let now = new Date()
  now.setDate(15)
  console.log(now) // Output: The date set to the 15th of the current month
  ```

#### **Use Cases:**

- **Displaying Current Date and Time**: Use `Date()` to show the current date and time in an application.
- **Date Calculations**: Use `getTime()` to perform calculations based on timestamps.

### 7. **Promise Methods**

Promises are used for handling asynchronous operations in JavaScript. The `Promise` object represents a value that may be available now, or in the future, or never.

#### **Common Promise Methods:**

- **`then()`**: Attaches callbacks for the resolution and/or rejection of the Promise.

  ```javascript
  let promise = new Promise((resolve, reject) => {
   setTimeout(() => resolve('Done'), 1000)
  })

  promise.then(result => console.log(result)) // Output: "Done" after 1 second
  ```

- **`catch()`**: Attaches a callback for only the rejection of the Promise.

  ```javascript
  let promise = new Promise((resolve, reject) => {
   setTimeout(() => reject('Error'), 1000)
  })

  promise.catch(error => console.log(error)) // Output: "Error" after 1 second
  ```

- **`finally()`**: Attaches a callback that will be called regardless of the promise's outcome (resolved or rejected).

  ```javascript
  let promise = new Promise((resolve, reject) => {
   setTimeout(() => resolve('Done'), 1000)
  })

  promise.finally(() => console.log('Operation completed')) // Output: "Operation completed" after 1 second
  ```

#### **Use Cases:**

- **Asynchronous Operations**: Use `Promise` methods to handle operations like fetching data from an API or reading files.

### Conclusion

JavaScript's built-in methods are essential tools that make coding more efficient and effective. By understanding and mastering these methods, developers can write cleaner code, solve problems more quickly, and implement features with greater ease.

These methods cover a wide range of use cases, from manipulating strings and arrays to working with objects, numbers, dates, and promises. Familiarizing yourself with these methods and knowing when and how to use them is a crucial step in becoming a proficient JavaScript developer.
