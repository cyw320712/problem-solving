package Medium;

public class longest_palindromic_substring {
    public String longestPalindrome(String s) {
        int start, end;
        int max = 0, ms = 0, me = 0;

        if (s.length() < 2) return s;

        for (start = 0; start < s.length(); start++) {
            for (end = start+1; end <= s.length(); end++){
                if (max < end - start){
                    if (checkPalindrome(s.substring(start, end))){
                        ms = start;
                        me = end;
                        max = me - ms;
                    }
                }
            }
        }

        return s.substring(ms, me);
    }

    private boolean checkPalindrome(String target){
        int length = target.length() - 1;

        for (int i = 0; i < target.length() / 2; i++) {
            if (target.charAt(i) != target.charAt(length - i))
                return false;
        }

        return true;
    }
}
