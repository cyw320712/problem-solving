package Level2;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class 뉴스클러스터링 {
    public int solution(String str1, String str2) {
        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();

        HashMap<String, Integer> count1 = new HashMap<>();
        HashMap<String, Integer> count2 = new HashMap<>();
        HashSet<String> str1Set = new HashSet<>();
        HashSet<String> str2Set = new HashSet<>();

        extractElapsedSet(str1, count1, str1Set);
        extractElapsedSet(str2, count2, str2Set);

        Set<String> temp = new HashSet<>(str1Set);
        temp.retainAll(str2Set);
        int share = 0;
        for (String s : temp) {
            share += Math.min(count1.getOrDefault(s, 0), count2.getOrDefault(s, 0));
        }

        temp = new HashSet<>(str1Set);
        temp.addAll(str2Set);
        int total = 0;
        for (String s : temp) {
            total += Math.max(count1.getOrDefault(s, 0), count2.getOrDefault(s, 0));
        }

        if (total == 0) return 65536;
        return share * 65536 / total;
    }

    private void extractElapsedSet(String str1, HashMap<String, Integer> count1, HashSet<String> str1Set) {
        for (int i = 0; i < str1.length() - 1; i++){
            String temp = str1.substring(i, i + 2);
            if(Character.isAlphabetic(temp.charAt(0)) //알파벳이면 추가
                    && Character.isAlphabetic(temp.charAt(1))){
                if (!count1.containsKey(temp)){
                    count1.put(temp, 0);
                }
                count1.put(temp, count1.get(temp)+1);
                str1Set.add(temp);
            }
        }
    }
}