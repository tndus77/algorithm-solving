import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] str = new String[numbers.length];
        
        //int배열 String배열로 변환
        for(int i=0; i<numbers.length; i++) {
            str[i] = String.valueOf(numbers[i]);
        }
        
        //내림차순
        Arrays.sort(str, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return ((o2 + o1).compareTo(o1 + o2));
            }
        });
        
        //0만 여러개 있는 배열의 경우 하나의 0만 리턴
        if(str[0].equals("0")) {
            return "0";
        }
        
        for(int i=0; i<str.length; i++) {
            answer += str[i];
        }
        
        return answer;
    }
}