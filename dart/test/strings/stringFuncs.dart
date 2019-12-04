import "package:test/test.dart";
import "../../lib/strings/CheckIfStringContainsDigits/strings.dart";
void main() {
  num num1 = tryParse('23');
  print(num1);
  assert(num1 == 23);


  num notNum = tryParse('*xs');
  assert(notNum == null);
}
