## **JavaScript Primitive Data Types Course**

### **1. Introduction to Primitive Data Types**

In JavaScript, primitive data types are the most basic types of data. They are immutable and represent single values. JavaScript has 7 primitive data types:

1. **String**
2. **Number**
3. **BigInt**
4. **Boolean**
5. **undefined**
6. **null**
7. **Symbol** (introduced in ES6)

### **2. String**

**Definition:** A string is a sequence of characters enclosed in quotes.

**Examples:**

```javascript
let str1 = 'Hello, World!'
let str2 = 'JavaScript'
let str3 = `Template literals can contain ${str2}`
```

**Real-World Usage:**

- **Displaying text:** Strings are used to display messages, labels, or any text on a webpage or application.
- **User input:** Capturing and processing user input from forms or prompts.
- **Data processing:** Manipulating and formatting data (e.g., parsing JSON).

**Common Methods:**

- `length`: Returns the number of characters in a string.
- `toUpperCase()`: Converts all characters to uppercase.
- `toLowerCase()`: Converts all characters to lowercase.
- `substring(start, end)`: Returns a part of the string between the start and end indexes.

```javascript
let example = 'Hello'
console.log(example.length) // 5
console.log(example.toUpperCase()) // "HELLO"
console.log(example.substring(1, 4)) // "ell"
```

### **3. Number**

**Definition:** Represents both integer and floating-point numbers.

**Examples:**

```javascript
let integer = 42
let float = 3.14
let negative = -7
```

**Real-World Usage:**

- **Calculations:** Performing arithmetic operations.
- **Storing values:** Handling quantities, measurements, or any numerical data.

**Common Methods:**

- `toFixed(digits)`: Formats a number using fixed-point notation.
- `toPrecision(precision)`: Formats a number to a specified precision.

```javascript
let num = 3.14159
console.log(num.toFixed(2)) // "3.14"
console.log(num.toPrecision(4)) // "3.142"
```

### **4. BigInt**

**Definition:** An arbitrary-precision integer type that can represent numbers larger than `Number`.

**Examples:**

```javascript
let bigInt1 = 9007199254740991n // Maximum safe integer
let bigInt2 = 1234567890123456789012345678901234567890n
```

**Real-World Usage:**

- **Large numbers:** Useful for scenarios requiring high precision, such as cryptographic operations or financial calculations.

**Common Operations:**

- Basic arithmetic operations (addition, subtraction, multiplication, division) with BigInt types.

```javascript
let big1 = 123456789012345678901234567890n
let big2 = 987654321098765432109876543210n
console.log(big1 + big2) // 1111111111111111111111111111000n
```

### **5. Boolean**

**Definition:** Represents a logical entity and can have one of two values: `true` or `false`.

**Examples:**

```javascript
let isTrue = true
let isFalse = false
```

**Real-World Usage:**

- **Conditional statements:** Used in `if` statements and loops to control the flow of code.
- **Flags:** Indicating whether certain conditions are met or not.

**Common Usage:**

```javascript
let age = 18
let isAdult = age >= 18 // true
```

### **6. undefined**

**Definition:** Represents a variable that has been declared but has not yet been assigned a value.

**Examples:**

```javascript
let x
console.log(x) // undefined
```

**Real-World Usage:**

- **Checking variables:** To check if a variable has been assigned a value or not.
- **Function returns:** Functions that don’t return a value explicitly return `undefined`.

**Common Usage:**

```javascript
function greet(name) {
 if (name === undefined) {
  return 'Hello, guest!'
 }
 return `Hello, ${name}!`
}
```

### **7. null**

**Definition:** Represents the intentional absence of any object value and is a falsy value.

**Examples:**

```javascript
let emptyValue = null
```

**Real-World Usage:**

- **Resetting variables:** Used to explicitly clear a variable's value or indicate the absence of an object.
- **Default values:** Often used as a default value for variables or function parameters.

**Common Usage:**

```javascript
let user = null // Initially no user
user = { name: 'Alice' } // Now there is a user
```

### **8. Symbol**

**Definition:** Represents a unique and immutable value primarily used as object property keys.

**Examples:**

```javascript
const sym1 = Symbol('description')
const sym2 = Symbol('description')
console.log(sym1 === sym2) // false
```

**Real-World Usage:**

- **Unique property keys:** Ensuring property keys are unique to avoid conflicts in objects.
- **Metadata:** Useful for creating unique identifiers.

**Common Usage:**

```javascript
const uniqueKey = Symbol('unique')
let obj = {
 [uniqueKey]: 'value',
}
console.log(obj[uniqueKey]) // "value"
```

### **Conclusion**

Understanding JavaScript's primitive data types is fundamental for effective programming. Each type has its use cases and characteristics that affect how you handle and manipulate data. By mastering these types, you’ll be well-equipped to write more robust and efficient JavaScript code.