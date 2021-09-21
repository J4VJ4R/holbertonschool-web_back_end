// returns a string of all the set values that start with a specific string (startString).
export default function cleanSet(set, startString) {
  let string = '';
  if (typeof (startString) === 'string' && startString !== '') {
    set.forEach((val) => {
      if (val.includes(startString)) string = string.concat(`-${val.replace(startString, '')}`);
    });
    string = string.substring(1);
  }
  return string;
}
/*
console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), 'bon'));
console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), ''));
console.log(cleanSet(new Set(['id-test', 'id-chicken', 'id-user', 'id-id-']), 'id-'));
console.log(cleanSet(new Set(['id-test', 'id-chicken', 'id-user', 'id-id-']), ''));
console.log(cleanSet(new Set(['id-test', 'id-chicken', 'id-user', 'id-id-']), [])); */
