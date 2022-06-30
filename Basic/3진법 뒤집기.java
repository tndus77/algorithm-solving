//원래 생각한 풀이
import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        ArrayList<Integer> list = new ArrayList<Integer>();

        // 10진법 -> 3진법
        while(n > 0) {
            list.add(n % 3); //45 -> 0021
            n /= 3;
        }

        // 3진법 -> 10진법
        int cnt = 1;
        for(int i=list.size()-1; i>=0; i--) {
            answer += list.get(i) * cnt;
            cnt *= 3;
        }
        return answer;
    }
}

//새로 알게 된 풀이 -> 문자열 사용
class Solution2 {
    public int solution(int n) {
        String ans = "";

        while(n != 0) {
            ans += n % 3;
            n /= 3;
        }

        return Integer.parseInt(ans, 3);
    }
}
