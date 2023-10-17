class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int sum = brown + yellow;
        
        for (int height=3; height<=brown; height++) {
            if (sum % height == 0) {
                int weight = sum / height;
            
                if ((height - 2) * (weight - 2) == yellow) {
                    answer[1] = weight;
                    answer[0] = height;
                }   
            }
        }
        return answer;
    }
}