# 0x0F. ES6 Promises

## Learning Objectives

  -  Promises (how, why, and what)
  -  How to use the then, resolve, catch methods
  -  How to use every method of the Promise object
  -  Throw / Try
  -  The await operator
  -  How to use an async function

## Tasks
### [0. Keep every promise you make and only make promises you can keep ](0-promise.js)
Return a Promise using this prototype function getResponseFromAPI()
```
> const response = getResponseFromAPI();
> response
Promise { <pending> }
> response instanceof Promise
true
> 
```

### [1. Don't make a promise...if you know you can't keep it ](./1-promise.js)
Using the prototype below, return a promise. The parameter is a boolean.

`getFullResponseFromAPI(success)`

When the argument is:

   - true
      - resolve the promise by passing an object with 2 attributes:
           - status: 200
           - body: 'Success'
   - false
        - reject the promise with an error object with the message The fake API is not working currently

Try testing it out for yourself
```
> getFullResponseFromAPI(true);
Promise { { status: 200, body: 'Success' } }
>
> getFullResponseFromAPI(false);
Promise {
  <rejected> Error: The fake API is not working currently
    ...

```

### [2. Catch me if you can! ](./2-then.js)
Using the function prototype below

`function handleResponseFromAPI(promise)`
Append three handlers to the function:

   - When the Promise resolves, return an object with the following attributes
       - status: 200
       - body: success
   - When the Promise rejects, return an empty Error object
   - For every resolution, log Got a response from the API to the console

### [3. Handle multiple successful promises](./3-all.js)
In this file, import uploadPhoto and createUser from utils.js

Knowing that the functions in utils.js return promises, use the prototype below to collectively resolve all promises and log body firstName lastName to the console.

`function handleProfileSignup()`

In the event of an error, log Signup system offline to the console

Example:
```
> handleProfileSignup()
Promise { <pending> }
> photo-profile-1 Guillaume Salva
> 
```

### [4. Simple promise ](./4-all-reject.js)
Using the following prototype
```
function signUpUser(firstName, lastName) {
}
```
That returns a resolved promise with this object:
```
{
  firstName: value,
  lastName: value,
}
```
Example:
```
> signUpUser("Bob", "Dylan")
Promise { { firstName: 'Bob', lastName: 'Dylan' } }
```

### [5. Reject the promises](./5-all-reject.js)
Write and export a function named uploadPhoto. It should accept one argument fileName (string). The function should return a Promise rejecting with an Error and the string $fileName cannot be processed
```
export function uploadPhoto(filename) {

}
```
Example:
```
> uploadPhoto("BobDylan.jpg")
Promise {
  <rejected> Error: BobDylan.jpg cannot be processed
...
```

### [6. Handle multiple promises ](./6-all-reject.js)
Import signUpUser from 4-all-reject.js and uploadPhoto from 5-all-reject.js.

Write and export a function named handleProfileSignup. It should accept three arguments firstName (string), lastName (string), and fileName (string). The function should call the two other functions. When the promises are all settled it should return an array with the following structure:
```
[
    {
      status: status_of_the_promise,
      value: value or error returned by the Promise
    },
    ...
  ]
```
Example:
```
> const res = handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg")
>
> res
Promise {
  [
    { status: 'fulfilled', value: [Object] },
    {
      status: 'rejected',
      value: 'Error: bob_dylan.jpg cannot be processed'
    }
  ]
}
>
```

### [7. Load balancer](./7-load_balancer.js)
Write and export a function named loadBalancer. It should accept two arguments chinaDownload (Promise) and USDownload (Promise).

The function should return the value returned by the promise that resolved the first.
```
export default function loadBalancer(chinaDownload, USDownload) {

}
```

Example:
```
> const promiseChina = new Promise(function(resolve, reject) {
        setTimeout(resolve, 100, 'Downloading from China is faster');
    });
> 
> const promiseUSA = new Promise(function(resolve, reject) {
        setTimeout(resolve, 300, 'Downloading from USA is faster');
    });
>
> const value = loadBalancer(promiseChina, promiseUSA);
>
> value
Promise { 'Downloading from China is faster' }
>
```

### [8. Throw error / try catch](./8-try.js)


Write a function named divideFunction that will accept two arguments: numerator (Number) and denominator (Number).

When the denominator argument is equal to 0, the function should throw a new error with the message cannot divide by 0. Otherwise it should return the numerator divided by the denominator.
```
export function divideFunction(numerator, denominator) {

}
```

Example:
```
> divideFunction(10, 2)
5
> divideFunction(10, 0)
Uncaught Error: cannot divide by 0
    at divideFunction (repl:3:11)
>
```

### [9. Throw an error ](./9-try.js)
Write a function named guardrail that will accept one argument mathFunction (Function).

The function should an array named queue. When the function is executed, the value returned by the function should be appended to the queue. If the function throws an error, the error message should be appended to the queue. In every case, the message Guardrail was processed should be added to the queue. Example:
```
[
  1000,
  'Guardrail was processed',
]
```
Example:
```
> const res = guardrail(() => { return divideFunction(10, 5)})
> res
[ 2, 'Guardrail was processed' ]
>
> const res0 = guardrail(() => { return divideFunction(10, 0)})
> res0
[ 'Error: cannot divide by 0', 'Guardrail was processed' ]
> 
```

### [10. Await / Async](./100-await.js)
Import uploadPhoto and createUser from utils.js

Write an async function named asyncUploadUser that will call these two functions and return an object with the following format:
```
{
  photo: response_from_uploadPhoto_function,
  user: response_from_createUser_function,
}
```
If one of the async function fails, return an empty object. Example:
```
{
  photo: null,
  user: null,
}
```
Example:
```
> const value = await asyncUploadUser();
> value
Promise {
  {
    photo: { status: 200, body: 'photo-profile-1' },
    user: { firstName: 'Guillaume', lastName: 'Salva' }
  }
}
>
```