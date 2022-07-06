/*
 * 1. 아이디어
 * - 우선순위 큐로 스코빌 지수를 구한 후 k 이상 되게 만듬
 * 2. 시간복잡도
 * 
 * 3. 자료구조
 * - 우선순위 큐
 */

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        //큐에 저장
        for(int scovilles: scoville) {
            heap.offer(scovilles);
        }

        //스코빌 지수 구하기
        while(heap.size() > 1 && heap.peek() <= K) {
            int a = heap.poll();
            int b = heap.poll();

            int result = a + (b*2);
            heap.offer(result);
            answer++;
        }
        return answer;
    }
}