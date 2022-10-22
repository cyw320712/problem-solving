package Medium;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }

class Solution {
    int carry;

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int cur_val = considerCarry(l1.val + l2.val);
        ListNode result = new ListNode(cur_val);
        ListNode curNode = result;

        l1 = l1.next;
        l2 = l2.next;

        while (l1 != null && l2 != null) {
            cur_val = considerCarry(l1.val + l2.val + carry);

            ListNode nextNode = new ListNode(cur_val);
            curNode.next = nextNode;
            curNode = curNode.next;
            l1 = l1.next;
            l2 = l2.next;
        }


        while (l1 != null) {
            cur_val = considerCarry(l1.val + carry);

            ListNode nextNode = new ListNode(cur_val);
            curNode.next = nextNode;

            curNode = curNode.next;
            l1 = l1.next;
        }
        while (l2 != null) {
            cur_val = considerCarry(l2.val + carry);

            ListNode nextNode = new ListNode(cur_val);
            curNode.next = nextNode;

            curNode = curNode.next;
            l2 = l2.next;
        }

        if (carry != 0) {
            ListNode nextNode = new ListNode(carry);
            curNode.next = nextNode;
        }
        return result;
    }

    private int considerCarry(int val) {
        carry = 0;
        if (val >= 10) {
            carry = 1;
            val -= 10;
        }

        return val;
    }
}

public class add_two_numbers {
}
