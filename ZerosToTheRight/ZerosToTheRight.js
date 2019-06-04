const zerosToRight = arr => {
  let output = [];
  let numZeros = [];

  for (i = 0; i < arr.length - 1; i++) {
    if (arr[i] !== 0) {
      output.push(arr[i]);
    } else {
      numZeros.push(0);
    }
  }
  if (numZeros.length > 0) {
    output = output.concat(numZeros);
  }
  return output;
};

console.log(zerosToRight([0, 2, 0, 4, 0, 6, 7, 8]));
