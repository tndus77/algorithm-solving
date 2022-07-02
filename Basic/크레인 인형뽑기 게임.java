import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> s = new Stack<Integer>();
        
        for(int j=0; j<moves.length; j++) {
            //인형이 있다면 행의 갯수가 계속 변함
            for(int i=0; i<board.length; i++) {
                if(board[i][moves[j]-1] != 0) {
                    //스택이 비있다면 인형 넣기
                    if(s.isEmpty()) {
                        s.push(board[i][moves[j]-1]);
                    } else { //비어있지 않으면
                        if(s.peek() == board[i][moves[j]-1]) {//뽑은 인형과 바구니에 담겨있던 인형이 같은 지 비교 후 같으면
                            s.pop();
                            answer += 2;
                        }
                        else {
                            s.push(board[i][moves[j]-1]);
                        }
                    }
                     //인형을 빼냈으므로 인형이 없음을 표시
                    board[i][moves[j]-1] = 0;
                    break;
                }
            }
        }
            
        return answer;
    }
}