namespace Algorithms;
public class Strings
{

    // take a string in the constructor
    public static bool isPalidrome(string text) {
        // loop through string
        bool isMatch = true;
        for (var i = 0; i < text.Length; i++) {
            if (text[i] != text[text.Length -1 -i]) {
                isMatch = false;
                break;
            }
        }
        return isMatch;
    }
}
