// returns a boolean if all the elements in the array exist within the set.
export default function hasValuesFromArray(set, array) {
  return array.every((val) => set.has(val));
}
/* console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1]))
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [10]))
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1, 10])) */
