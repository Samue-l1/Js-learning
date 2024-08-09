### Data Types in JavaScript: A Comprehensive Guide with Examples

In JavaScript, data types are the essential building blocks of any program. Understanding them is crucial for writing efficient and error-free code. JavaScript is a loosely-typed language, meaning you don't need to specify the data type of a variable when declaring it. However, knowing the different data types available and how to use them effectively is key to mastering JavaScript.

#### 1. **Primitive Data Types**

Primitive data types are the most basic types in JavaScript. They include:

- **Number**
- **String**
- **Boolean**
- **Null**
- **Undefined**
- **Symbol** (introduced in ES6)
- **BigInt** (introduced in ES11)

Let's explore each of these with examples.

##### a. **Number**

The `Number` type is used for representing both integers and floating-point numbers.

```javascript
let age = 25 // Integer
let pi = 3.14159 // Floating-point number
let negative = -42 // Negative number
```

JavaScript also has special numeric values like `Infinity`, `-Infinity`, and `NaN` (Not-a-Number).

```javascript
let infinite = Infinity // Positive infinity
let notANumber = 'abc' / 2 // NaN
```

##### b. **String**

Strings are sequences of characters used for representing text.

```javascript
let name = 'John Doe'
let greeting = 'Hello, World!'
let multiline = `This is
a multiline
string.`
```

Strings can be enclosed in single quotes, double quotes, or backticks (for template literals).

##### c. **Boolean**

The Boolean type has only two possible values: `true` and `false`.

```javascript
let isJavaScriptFun = true
let isRaining = false
```

Booleans are often used in conditional statements.

##### d. **Null**

The `null` type represents the intentional absence of any object value.

```javascript
let emptyValue = null
```

##### e. **Undefined**

A variable that has been declared but not yet assigned a value has the type `undefined`.

```javascript
let notAssigned
console.log(notAssigned) // undefined
```

##### f. **Symbol**

Symbols are unique and immutable data types used to create unique identifiers for objects.

```javascript
let uniqueId = Symbol('id')
```

##### g. **BigInt**

BigInt is used for representing integers with arbitrary precision, larger than the `Number` type can safely handle.

```javascript
let bigNumber = 1234567890123456789012345678901234567890n
```

#### 2. **Composite (Non-Primitive) Data Types**

Composite data types can hold collections of values or more complex entities. These include:

- **Object**
- **Array**
- **Function**

##### a. **Object**

Objects are used to store collections of data and more complex entities. An object is created using curly braces `{}` and contains key-value pairs.

```javascript
let person = {
 firstName: 'John',
 lastName: 'Doe',
 age: 30,
 isEmployed: true,
}
```

Properties in an object can be accessed using dot notation or bracket notation.

```javascript
console.log(person.firstName) // John
console.log(person['age']) // 30
```

##### b. **Array**

Arrays are ordered collections of values, which can be of any data type.

```javascript
let colors = ['red', 'green', 'blue']
let mixedArray = [42, 'hello', true, null]
```

Array elements are accessed using their index, starting from 0.

```javascript
console.log(colors[0]) // red
```

##### c. **Function**

Functions are reusable blocks of code that can be executed whenever they are invoked. They are also a type of object.

```javascript
function greet(name) {
 return `Hello, ${name}!`
}

console.log(greet('Alice')) // Hello, Alice!
```

#### 3. **Type Coercion**

JavaScript automatically converts data from one type to another when necessary. This process is called type coercion.

```javascript
console.log('5' - 2) // 3 (String "5" is coerced to Number 5)
console.log('5' + 2) // "52" (Number 2 is coerced to String "2")
```

#### 4. **Checking Data Types**

You can check the data type of a variable using the `typeof` operator.

```javascript
let value = 42
console.log(typeof value) // "number"

value = 'Hello'
console.log(typeof value) // "string"
```

#### 5. **Conclusion**

Understanding JavaScript data types is foundational for effective programming. By knowing how to work with different types and handle type coercion, you can avoid common pitfalls and write cleaner, more reliable code. Whether dealing with numbers, strings, booleans, or complex objects, a solid grasp of these concepts will serve you well in your JavaScript journey.
