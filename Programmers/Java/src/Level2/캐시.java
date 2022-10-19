package Level2;

import java.util.LinkedList;

public class 캐시 {
    LinkedList<String> cache;

    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        if (cacheSize == 0) return 5 * cities.length;
        cache = new LinkedList<>();

        int count = 0;
        for (String city : cities){
            String cur = city.toLowerCase();
            if (cache.contains(cur)) {
                answer += 1;
                cache.remove(cur);
                cache.addFirst(cur);
            }
            else {
                answer += 5;
                if (count == cacheSize){
                    cache.removeLast();
                    count--;
                }
                cache.addFirst(cur);
                count++;
            }
        }

        return answer;
    }
}