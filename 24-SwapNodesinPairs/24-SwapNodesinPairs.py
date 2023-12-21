        prev = None
        curr = head
        while curr and curr.next:
            curr.next = tmp.next
        adv = head.next
            tmp = curr.next
            if prev:
            curr = curr.next

                prev.next = tmp
            tmp.next = curr
            prev = curr
        return adv or head
[
