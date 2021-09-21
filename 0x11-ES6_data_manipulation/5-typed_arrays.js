// returns a new ArrayBuffer with an Int8 value at a specific position.
export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const array = new Int8Array(buffer, 0, length);
  if (position >= 0 && position < length) array[position] = value;
  else throw Error('Position outside range');
  return buffer;
}

/* console.log(createInt8TypedArray(10, 2, 89));
createInt8TypedArray(10, 12, 89); */
