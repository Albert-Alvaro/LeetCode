import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        List<Integer> L1=new ArrayList<Integer>();
        List<Integer> L2=new ArrayList<Integer>();
        List<Integer> L3=new ArrayList<Integer>();
        List<Integer> L4=new ArrayList<Integer>();
        List<Integer> numbers=new ArrayList<Integer>();

        ListNode current = l1;
        while (current != null) {
            L1.add(current.val);
            current = current.next;
        }
        ListNode current1 = l2;
        while (current1 != null) {
            L2.add(current1.val);
            current1 = current1.next;
        }

        for (int i = 1; i <= L1.size(); i++) {
            L3.add(L1.get(L1.size()-i));
        }
        for (int i = 1; i <= L2.size(); i++) {
            L4.add(L2.get(L2.size()-i));
        }

        String str = L3.stream().map(Object::toString).collect(Collectors.joining(""));
        String str1 = L4.stream().map(Object::toString).collect(Collectors.joining(""));
        int result = Integer.parseInt(str) + Integer.parseInt(str1);

        while (result > 0) {
            numbers.add(result % 10);
            result /= 10;
        }

        if (numbers == null || numbers.isEmpty()) {
            return new ListNode(0);
        }

        ListNode l3 = new ListNode(numbers.get(0));
        ListNode current4 = l3;

        for (int i = 1; i < numbers.size(); i++) {
            current4.next = new ListNode(numbers.get(i));
            current4 = current4.next;
        }
        return l3;
    }
}

class ListNode {
 int val;
 ListNode next;
 ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}