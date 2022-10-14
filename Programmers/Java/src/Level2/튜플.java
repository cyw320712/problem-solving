package Level2;

import java.util.*;

public class 튜플 {
    public int[] solution(String s) {
        int[] answer = {};
        List<String> set = new ArrayList<>();
        HashMap<Integer, Integer> count = new HashMap<>();

        int startIndex = 0, endIndex = 0;
        int maxsIndex = 0, maxeIndex = 0, maxLength = 0;
        for (int i = 1; i < s.length() - 1; i++) {
            if (s.charAt(i) == '{') startIndex = i+1;
            if (s.charAt(i) == '}') endIndex = i;
            if (startIndex != 0 && endIndex != 0){
                int[] temp = Arrays.stream(s.substring(startIndex, endIndex).split(","))
                        .mapToInt(Integer::parseInt)
                        .toArray();
                for (int k : temp) {
                    if (!count.containsKey(k)) count.put(k, 0);
                    count.put(k, count.get(k)+1);
                }
                startIndex = 0;
                endIndex = 0;
            }
        }

        List<Map.Entry<Integer, Integer>> entryList = new ArrayList(count.entrySet());
        entryList.sort(Map.Entry.comparingByValue());

        answer = new int[entryList.size()];

        for (int i = 0; i < answer.length; i++){
            answer[i] = entryList.get(answer.length - 1 - i).getKey();
        }

        return answer;
    }
}