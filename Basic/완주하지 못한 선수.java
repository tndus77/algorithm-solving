import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        for(int i=0; i<completion.length; i++) {
            if(!completion[i].equals(participant[i])) {
                //완주하지 못한 사람
               return participant[i];
            }
        }
        //완주하지 못한 사람이 마지막에 있으면
        return participant[participant.length - 1];
    }
}