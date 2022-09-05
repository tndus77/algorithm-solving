import java.io.*;
import java.util.*;
/*
 * 1. 아이디어
 * 뒤집기 -> 스택 사용
 * 
 * 2. 시간복잡도
 * 
 */

public class word_reverse {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine();
    //뒤집은 문자를 넣어줄 stack
    Stack<Character> stack = new Stack<>();
    boolean isOutSide = true;

    for(int i=0; i<s.length(); i++) {
      if(s.charAt(i) == '<') {
        //태그 안
        isOutSide = false;
        //이전꺼 모두 빼주기
        while(!stack.isEmpty()) {
          System.out.print(stack.pop());
        }
        System.out.print(s.charAt(i));
      } 
      else if (s.charAt(i) == '>') {
          //태그 밖
          isOutSide = true;
          System.out.print(s.charAt(i));
      } 
      else if (isOutSide){ //태그 밖 1. 공백 o, 2. 공백 x
        if(s.charAt(i) == ' ') {
          while(!stack.isEmpty()){
            System.out.print(stack.pop());
          }
          //공백 띄워주고 
          System.out.print(s.charAt(i));
        } 
        else { 
          stack.push(s.charAt(i));
        }
      }
      else { //태그 안
        System.out.print(s.charAt(i));
        
      }
    }
    while(!stack.isEmpty()) {
      System.out.print(stack.pop());
    }
  }
}
