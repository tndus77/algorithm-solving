package 정렬;
import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;

        Arrays.sort(citations);
        
        for(int i=0; i<citations.length; i++) {
            int h = citations.length - i; //5 - 0 // h는 5

            if(citations[i] >= h) {
                answer = h;
                break;
            }

        }
        return answer;
    }
}