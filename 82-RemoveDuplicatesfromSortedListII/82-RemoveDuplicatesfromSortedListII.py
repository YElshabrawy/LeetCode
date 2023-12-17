        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
        prev = dummy
        curr = head
        dummy = ListNode(0)
        dummy.next = head
            return head
        if not head or not head.next:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
[
