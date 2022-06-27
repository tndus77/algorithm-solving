import java.util.*;

class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        
        
        for(int i=0; i<arr.length; i++) {
            if(i == 0) {
                arrayList.add(arr[0]);
            }
            else if(arr[i-1] != arr[i]) {
                arrayList.add(arr[i]);
            }
        }
        
        //만든 리스트를 answer에 집어 넣기 위해서는 for문 필요
        answer = new int[arrayList.size()];
        for(int i=0; i<arrayList.size(); i++) {
            answer[i] = arrayList.get(i);
        }
         

        return answer;
    }
}