import java.io.*;
import java.util.*;

public class priorityQueue {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    PriorityQueue maxQueue = new PriorityQueue<>(Collections.reverseOrder());
    PriorityQueue minQueue = new PriorityQueue<>();
    
    int t = Integer.parseInt(st.nextToken());
    
    for(int i=0; i<t; i++) {
      int num = Integer.parseInt(br.readLine());
      for(int j=0; j<num; j++) {
        st = new StringTokenizer(br.readLine());
        String prev = st.nextToken();
        int next = Integer.parseInt(st.nextToken());

        switch(prev) {
          case "I" : 
            maxQueue.add(next); 
            minQueue.add(next);
            break;
          case "D" : 
            if(maxQueue.isEmpty()) continue;
            else if(next == 1) { //최댓값 빼기
              minQueue.remove(maxQueue.poll());
            } else { //최솟값 빼기
              maxQueue.remove(minQueue.poll());
            }
            break;
        }
      }
      if(maxQueue.isEmpty()) System.out.println("EMPTY");
      else System.out.print(maxQueue.poll() + " " + minQueue.poll());
    }

  }
}
