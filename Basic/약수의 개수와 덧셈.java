import java.util.*;

//내가 생각한 풀이
class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        
        for(int i=left; i<=right; i++) {
            //약수의 갯수 변수 선언과 구하기
            //for문 들어오자마자 cnt 초기화
            int cnt = 0;
            for(int j=1; j<=i; j++) {
                if(i % j == 0) { //약수
                    cnt++;
                }
            }
            if(cnt % 2 == 0) { //약수의 갯수가 짝수면
                answer += i;
            } else {                    
                answer -= i;
            }
        }
        return answer;
    }
}

//새로운 풀이
class Solution2 {
    public int solution(int left, int right) {
        int answer = 0;
        
        for(int i=left; i<=right; i++) {
            //제곱수인 경우 약수의 개수가 홀수
            if(i % Math.sqrt(i) == 0 ) {
                answer -= i;
            } else { //제곱수가 아닌 경우의 약수의 개수가 짝수
                answer += i;
            }
        }
        return answer;
    }
}
