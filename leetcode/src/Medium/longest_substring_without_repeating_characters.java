package Medium;

class Solutions {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        int[] ascii;

        for (int i = 0; i< s.length(); i++) {
            int endIndex = i;
            ascii = new int[128];

            while (endIndex < s.length()) {
                char cur = s.charAt(endIndex);

                if (ascii[cur] != 1) {
                    ascii[cur] = 1;
                    endIndex ++;
                }
                else {
                    break;
                }
            }

            result = Math.max(result, endIndex - i);
        }

        return result;
    }
}

public class longest_substring_without_repeating_characters {

    public static void main (String[] args) {
        Solutions s = new Solutions();
        System.out.println(s.lengthOfLongestSubstring("abcabcaaa"));
    }
}
