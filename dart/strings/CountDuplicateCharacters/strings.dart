import 'dart:collection';
import 'dart:core';
// HashMap<String, Number> 
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
      // result.update(ch, (e) => e + 1, ifAbsent:  () => 1);
  }
  return result;
}
/* public static Map<Character, Integer> countDuplicateCharactersV1(String str) {

  if (str == null || str.isEmpty()) {
      // or throw IllegalArgumentException
      return new Map();
  }

  Map<Character, Integer> result = new HashMap<>();                
  HashMap map1 = new HashMap<int, String>();
  // or use for(char ch: str.toCharArray()) { ... }
  for (int i = 0; i < str.length(); i++) {
      char ch = str.charAt(i);

      result.compute(ch, (k, v) -> (v == null) ? 1 : ++v);
  }

  return result;
} */
