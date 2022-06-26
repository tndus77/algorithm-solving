class Solution {
    boolean solution(String s) {
        boolean answer = true;

        //소문자 변환   
        String[] arr = s.toLowerCase().split("");
        int pCount = 0;
        int yCount = 0;

        for(int i=0; i<arr.length; i++) {
            if(arr[i].equals("p")) {
                pCount++;
            } else if(arr[i].equals("y")) {
                yCount++;
            } else {
                continue;
            }
        }
        
        //p와 y 갯수 비교
        if(pCount == yCount) {
            answer = true;
        } else {
            answer = false;
        }
        
        return answer;
    }
}