import 'dart:core';
// returns the first non repeated character or throws an error
firstNonRepeatedCharacterV1(String str) {
  if (str == null || str.isEmpty) {
      // or throw IllegalArgumentException
      throw new FormatException("Cannot Parse A Blank String");
  }

  for (int i = 0; i < str.length; i++) {
      String ch = str[i];
      int count = 0;
      for (int j = 0; j < str.length; j++) {
          if (ch == str[j] && i != j) {
              count++;
              break;
          }
      }

      if (count == 0) {
          return ch;
      }
  }
  throw new FormatException("No Non Repeating Character Found");
}
