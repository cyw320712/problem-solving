package Level2;

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    boolean[] visited;
    public long solution(String expression) {
        long answer = 0;

        Set<Character> operators = getOperators(expression);
        visited = new boolean[operators.size()];
        List<String> priorities = makeOperatorPriorities(operators.stream().collect(Collectors.toList()));
        answer = extractResult(expression, priorities);

        return Math.abs(answer);
    }

    private long extractResult(String expression, List<String> priorities) {
        long max = 0;

        for (String priority : priorities) {
            long result = calForPriority(priority, expression);

            max = Math.max(max, result);
        }

        return max;
    }

    private long calForPriority(String priority, String expression) {
        StringBuilder post = new StringBuilder();
        List<Long> operandList = new LinkedList<>();
        List<String> operatorList = new LinkedList<>();

        for (int i = 0; i < expression.length(); i++) {
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-' || expression.charAt(i) == '*') {
                operandList.add(Long.parseLong(post.toString()));
                post = new StringBuilder();
                operatorList.add(String.valueOf(expression.charAt(i)));
            } else
                post.append(expression.charAt(i));
        }

        operandList.add(Long.parseLong(post.toString()));

        for (int i = 0; i < 3; i++) {
            String nowOperator = String.valueOf(priority.charAt(i));

            while(operatorList.size() != 0){
                int index = operatorList.indexOf(nowOperator);

                if(index == -1)
                    break;
                else{
                    switch (nowOperator) {
                        case "+" -> operandList.add(index, operandList.get(index) + operandList.get(index + 1));
                        case "-" -> operandList.add(index, operandList.get(index) - operandList.get(index + 1));
                        case "*" -> operandList.add(index, operandList.get(index) * operandList.get(index + 1));
                    }

                    operandList.remove(index + 1);
                    operandList.remove(index + 1);

                    operatorList.remove(index);
                }
            }
        }

        return Math.abs(operandList.get(0));
    }

    private Set<Character> getOperators(String expression) {
        Set<Character> operators = new HashSet<>();
        for (int i = 0; i < expression.length(); i++){
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-' || expression.charAt(i) == '*')
                operators.add(expression.charAt(i));
        }
        return operators;
    }

    private List<String> makeOperatorPriorities(List<Character> operators) {
        List<String> result = new ArrayList<>();
        backTrack("", result, operators);
        return result;
    }

    private void backTrack(String priority, List<String> result, List<Character> operators) {
        if (priority.length() == operators.size()){
            result.add(priority);
            return;
        }

        for (int i = 0; i < operators.size(); i++){
            if (!visited[i]){
                visited[i] = true;
                backTrack(priority + operators.get(i).toString(), result, operators);
                visited[i] = false;
            }
        }
    }
}

public class 수식최대화{
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.println(s.solution("50*6-3*2"));
    }
}