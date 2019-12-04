import 'dart:collection';
import 'dart:core';
  
// see https://stackoverflow.com/questions/56304347/dart-check-string-has-only-valid-characters
String _getRestrictedCharacters(String string){
  // const allowedCharacters = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""";
  const allowedCharacters = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ""";
  Set<String> restricted = Set();
  final split = string.split('');
  split.forEach((c) {
    if (!allowedCharacters.contains(c)) {
      restricted.add(c);
    }
  });
  if (restricted.isEmpty){
    return null;
  } else {
    return restricted.join("");
  }
}
  
// Assuming ASCII characters
bool isVowel(String ch)
{
  // not consonant
  return !isConsonant(ch);
}
// Function to check for consonant 
bool isConsonant(String ch) 
{ 
    // To handle lower case 
    ch = ch.toUpperCase(); 
  
    return !(ch == 'A' || ch == 'E' ||  
            ch == 'I' || ch == 'O' ||  
            ch == 'U'); 
} 
  
int totalConsonants(String str) 
{ 
    int count = 0; 
    for (int i = 0; i < str.length; i++)  
  
        // To check is character is Consonant 
        if (isConsonant(str[i])) 
            ++count; 
    return count; 
}

int totalVowels(String str) 
{ 
    int count = 0; 
    for (int i = 0; i < str.length; i++)  
  
        // To check is character is Consonant 
        if (!isConsonant(str[i])) 
            ++count; 
    return count; 
}
