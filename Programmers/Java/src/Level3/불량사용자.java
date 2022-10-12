package Level3;

import java.util.*;
import java.util.regex.*;

class Solution {
    HashSet<HashSet<String>> result;
    ArrayList<ArrayList<String>> banList;

    public int solution(String[] user_id, String[] banned_id) {
        result = new HashSet<>();
        banList = new ArrayList<>();

        for (String ban : banned_id) {
            ArrayList<String> matchedIdList = matching(user_id, ban);
            banList.add(matchedIdList);
        }

        backtrack(0, new HashSet<String>());

        return result.size();
    }

    private ArrayList<String> matching(String[] user_id, String ban) {
        ArrayList<String> temp = new ArrayList<>();

        String banPattern = ban.replace('*', '.');
        Pattern pattern = Pattern.compile(banPattern);

        for (String id : user_id){
            Matcher matcher = pattern.matcher(id);

            if (matcher.matches()){
                temp.add(id);
            }
        }

        return temp;
    }

    private void backtrack(int cur, HashSet<String> tuple){
        if (banList.size() == cur){
            result.add(new HashSet<>(tuple));
            return;
        }

        List<String> curIdList = banList.get(cur);

        for (String userId : curIdList) {
            if (!tuple.contains(userId)){
                tuple.add(userId);
                backtrack(cur + 1, tuple);
                tuple.remove(userId);
            }
        }
    }
}