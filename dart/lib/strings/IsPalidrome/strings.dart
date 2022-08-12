import 'dart:core';
// returns the first non repeated character or throws an error
isPalidrome(String str1) {
  if (str == null || str.isEmpty) {
      // or throw IllegalArgumentException
      throw new FormatException("Cannot Parse A Blank String");
  }

  var isValid = true;
  for (int i = 0; i < str1.length; i++) {
      String ch = str1[i];
      if (str1[str1.length-1-i] !== str1[i]) {
        return false;
      }
  }
  return isValid;
  throw new FormatException("No Non Repeating Character Found");
}
