class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length - 1];
        int min = arr[0]; //첫번째 숫자를 가장 작은 값을 잡기
        
        if (arr.length <= 1) {
            int[] answer2 = { -1 };
            return answer2;
        }

        //최솟값 찾기
        for(int i = 0; i < arr.length; i++) {
            min = Math.min(min, arr[i]);
        }
        
        int index = 0;
        for(int i=0; i<arr.length; i++) {
            if(min == arr[i]) { //arr[i]가 작은 수 일때
                continue;
            } else { //arr[i]가 작은 수가 아닐 때
                answer[index] = arr[i];
                index++;
            }
        }
        return answer;
    }
}