'''
Ok so how could we do this?

iterate through the ll once, create a list
then have a left, right points on the list,
create a new list based upon that.

Since everything is in a list, we can totally
destroy the previous associations.

if not head: return None

[1,2,3,4]

l = 0
r = len(arr)-1
ans = None

itr = True

# while l < r

if ans == None:
    ans = arr[l]
    node = ans
    l += 1
    continue

if itr:
    node.next = arr[l]
    node = node.next
    l += 1
    # Use left

elif not itr:
    node.next = arr[r]
    r -= 1
    # Use right

itr = not itr

# 1 Convert ll to arr[ListNode]
# 2 Use arr to reorder the nodes

'''


class ListNode(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def reorderList(self, head):

        if not head: return head

        arr = []
        node = head

        # 1 Populate arr
        while node:
            arr.append(node)
            node = node.next

        # 2 Use arr to re-order the nodes

        ans = None
        l = 0
        r = len(arr)-1
        itr = True

        while l <= r: # Vary length of ll
            if ans == None:
                ans = arr[l]
                node = ans
                l += 1

            elif itr:
                node.next = arr[l]
                node = node.next
                l += 1

            elif not itr:
                node.next = arr[r]
                node = node.next
                r -= 1

            itr = not itr

        return ans
