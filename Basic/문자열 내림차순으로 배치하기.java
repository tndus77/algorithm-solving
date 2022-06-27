import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        //각 문자를 잘라서 배열에 넣어주기
        String[] str = s.split("");
        
        //오름차순으로 정렬
        Arrays.sort(str, Collections.reverseOrder());
        
        for(int i=0; i<str.length; i++) {
            answer += str[i];
        }
        
        return answer;
    }
}