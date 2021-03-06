function merge(leftA, rightA) {
    var results = [],
        leftIndex = 0,
        rightIndex = 0;
    while (leftIndex < leftA.length && rightIndex < rightA.length) {
        if (leftA[leftIndex] < rightA[rightIndex]) {
            results.push(leftA[leftIndex++]);
        } else {
            results.push(rightA[rightIndex++]);
        }
    }
    var leftRemains = leftA.slice(leftIndex),
        rightRemains = rightA.slice(rightIndex);

    // add remaining to resultant array
    return results.concat(leftRemains).concat(rightRemains);
}

 function mergeSort(array) {

 if(array.length <2){
   return array; 
 }

 var midpoint = Math.floor(array.length)/2);
 var leftArray = array.slice(0, midpoint);
 var rightArray = array.slice(midpoint);

 return merge(mergeSort(leftArray), mergeSort(rightArray));
}
