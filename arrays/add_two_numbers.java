// problem link: https://leetcode.com/problems/add-two-numbers
// Difficulty: Medium

public class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val; }
  ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
  public ListNode addTwoNumbers(final ListNode l1, final ListNode l2) {
    ListNode head = new ListNode(0); // pointer to the head of the returned linked list. It's impossible to create a ListNode that is null;
    ListNode result = head; // current pointer of the result linked list;
    ListNode a = l1; // pointers to the linked list constants parameters;
    ListNode b = l2;
    int carry = 0; // carry of the sum
    int temp = 0; // total sum value

    while (a != null || b != null) {
      temp += carry; // adding carry to the sum;

      // adds the value in l1 and change to the next node;
      if (a != null) {
        temp += a.val;
        a = a.next;
      }
      // adds the value in l1 and change to the next node;
      if (b != null) {
        temp += b.val;
        b = b.next;
      }

      // checks if the sum created a carry value;
      if (temp > 9){
        carry = temp / 10;
        result.next = new ListNode(temp - 10);
      }
      else {
        carry = 0;
        result.next = new ListNode(temp);
      }
      temp = 0; // zero the temp sum;
      result = result.next; // change to the next node of the returned linked list;
    }

    // checks if are remaining items to sum;
    temp += carry;
    if (a != null) {
      temp += a.val;
      a = a.next;
    }
    if (b != null) {
      temp += b.val;
      b = b.next;
    }
    if (temp > 9){
      carry = temp / 10;
      result.next = new ListNode(temp - 10);
      result.next.next = new ListNode(carry);
    }
    else if (temp != 0) {
      carry = 0;
      result.next = new ListNode(temp);
    }
    
    head = head.next; // skipping the first node, beacause its value is 0;
    return head;
  }
}