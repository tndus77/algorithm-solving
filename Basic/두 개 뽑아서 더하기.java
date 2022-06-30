import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        //HashSet 사용 -> 중복된 값 허용 x, 순서 보장x
        ArrayList<Integer> list = new ArrayList<Integer>();

        for(int i=0; i<numbers.length; i++) {
            for(int j=i+1; j<numbers.length; j++) {
                int sum = numbers[i] + numbers[j];
                //중복된 숫자가 없으면 리스트에 넣어주기!
                if(!list.contains(sum)) {
                    list.add(sum);
                }
            }
        }
        
        int[] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++) {
            answer[i] = list.get(i);
        }

        //오름차순 정렬
        Arrays.sort(answer);

        return answer;
    }
}