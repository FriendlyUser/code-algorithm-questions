import 'dart:collection';
permuteAndPrint(String prefix, String str) {
  int n = str.length;
  if (n == 0) {
    print(prefix + ' ');
  } else {
    for (int i = 0; i < n; i++) {
      permuteAndPrint(prefix + str.charAt(i),
        str.substring(i + 1, n) + str.substring(0, i));
    }
  }
}

permuteAndStore(String str) {
  permutations =  new HashSet();
  int n = str.length;

  if (n == 0) {
    permutations.add(prefix);
  } else {
    for (int i = 0; i < n; i++) {
      permutations.addAll(permuteAndStore(prefix + str.charAt(i),
        str.substring(i + 1, n) + str.substring(0, i)));
    }
  }

  return permutations;
}
