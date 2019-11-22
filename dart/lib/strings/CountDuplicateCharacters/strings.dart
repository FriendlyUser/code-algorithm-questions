import 'dart:collection';
import 'dart:core';
countDuplicateCharactersV1(String str) {
  if (str == null || str.isEmpty) {
      // or throw IllegalArgumentException
      return new Map();
  }

  // HashMap<String, Integer> result = new HashMap<>();                
  HashMap result = new HashMap<String, int>();
  for (int i = 0; i < str.length; i++) {
      String ch = str[i];
      int tempValue = result[ch];
      result.update(ch, (e) => ++tempValue, ifAbsent: () => 1);
  }
  return result;
}
