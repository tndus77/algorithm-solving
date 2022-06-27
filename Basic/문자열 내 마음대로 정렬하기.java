import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        
        //ArrayList 사용
        ArrayList<String> arr = new ArrayList<>();
        
        //중복 문자열이 있을 수 있으므로 n번째 문자를 기존 문자열 앞에 새로운 문자열을 붙임
        for(int i=0; i<strings.length; i++) {
            arr.add(strings[i].charAt(n) + strings[i]);
        }
        
        //맨 앞에 문자열을 기준(string.charAt(n))으로 오름차순 sort
        Collections.sort(arr);
        
        for(int i=0; i<arr.size(); i++) {
            answer[i] = arr.get(i).substring(1);
        }
        
        return answer;
    }
}