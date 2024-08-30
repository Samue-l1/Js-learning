function calc1(a, b) {
 var c = a + b
 return c
}

const calc2 = () => {
 return a + b
}

async function calc3(a, b) {
 const result = a + b
 return result
}

function calc4(a, b) {
 const c = a + b
 return c
}

module.exports = {
 calc1,
 calc2,
 calc3,
 calc4,
}
