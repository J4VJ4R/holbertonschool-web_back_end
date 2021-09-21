/* Returns an updated map for all items with initial quantity at 1.
entry of the map where the quantity is 1, update the quantity to 100. */
// import groceriesList from './9-groceries_list';
export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    for (const i of map.entries()) {
      if (i[1] === 1) map.set(i[0], 100);
    }
    return map;
  } throw Error('Cannot process');
}

/* const map = groceriesList();
console.log(updateUniqueItems(map))
console.log(map)
console.log(updateUniqueItems("alo"))
 */
