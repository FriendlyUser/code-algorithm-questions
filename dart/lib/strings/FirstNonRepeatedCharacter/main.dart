// @nodoc
import 'dart:collection';
import './strings.dart';
// @nodoc
void main() {
  String text = "My high school, the Illinois Mathematics and Science Academy, "
            + "showed me that anything is possible and that you're never too young to think big. "
            + "At 15, I worked as a computer programmer at the Fermi National Accelerator Laboratory, "
            + "or Fermilab. After graduating, I attended Stanford for a degree in economics and "
            + "computer science.";
  String first = '';
  try {
    first = firstNonRepeatedCharacterV1(text);
    // first should be ' in you're
  } on FormatException { 
      print('Cannot divide by zero'); 
   } 
   finally { 
      print('Finally block executed' + first); 
   } 
}

