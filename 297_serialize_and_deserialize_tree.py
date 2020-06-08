
'''
Create two functions. One that serializes a tree
and one that deserialize a tree.

Serialize: Given a binary tree, serialize it.
BFS, log the values of the nodes as we traverse
through the tree.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "(val: {} | .left: {} | .right: {})".format(self.val, self.left, self.right)


class Codec:

    def serialize(self, root):
        if not root:
            return "[None]"

        ans = []
        q = [root]
        counter = 1

        while q and counter > 0:
            node = q.pop()

            if node:
                counter -= 1
                ans.append(node.val)
                q = [node.right, node.left] + q

                if node.right:
                    counter += 1

                if node.left:
                    counter += 1

            elif not node:
                ans.append(None)
                q = [None, None] + q

        return "{}".format(ans)




    def serialize_1(self, root): # Does not work

        if not root:
            return "[None]"

        # return variable of type string
        serial = []

        q = [root]

        while q:
            node = q.pop()

            if node:
                serial.append(node.val)

                q = [node.right, node.left] + q

            elif not node:
                serial.append(None)

        while serial[-1] == None:
            serial.pop()

        print("serialize")
        print("{}".format(serial))

        return "{}".format(serial)

    def deserialize_1(self, data): # Does not work
        # given a string, return the tree
        a = data[1:-1]
        a.replace(' ','')
        a = a.split(',')

        for i in range(len(a)):
            if a[i] == 'null':
                a[i] = None

            else:
                a[i] = int(a[i])

        if a == []:
            return None

        print(a)

        d = {}

        for i in range(len(a)):
            if a[i] != None:

                try:
                    if d[i]:
                        p = ''

                except:
                    d[i] = TreeNode(a[i])

                l = i*2+1
                r = i*2+2

                if l < len(a):
                    if a[l] != None:
                        d[l] = TreeNode(a[l])
                        d[i].left = d[l]

                if r < len(a):
                    if a[r] != None:
                        d[r] = TreeNode(a[r])
                        d[i].right = d[r]

        return d[0]


    def deserialize(self, data):
        if data == "[None]":
            return None

        print("[input] {}".format(data))
        #print(data)

        # given a string, return the tree
        a = data[1:-1]
        a.replace(' ','')


        a = a.split(', ')

        # print(a)

        for i in range(len(a)):
            if a[i] == 'None':
                a[i] = None

            else:
                a[i] = int(a[i])

        if a == []:
            return None

        print("[post cleaning] {}".format(a))

        vals = a


        if len(vals) == 0:
            self.tree = None

        else:
            ans = TreeNode(vals[0])
            nodes = [[0,ans]]

            while nodes != []:

                index = nodes[-1][0] + 1
                node = nodes[-1][1]

                if index*2-1 <= len(vals)-1:
                    if vals[index*2-1] != None:
                        node.left = TreeNode(vals[index*2-1])
                        nodes.insert(0,[index*2-1,node.left])

                if index*2 <= len(vals)-1:
                    if vals[index*2+1-1] != None:
                        node.right = TreeNode(vals[index*2+1-1])
                        nodes.insert(0,[index*2+1-1,node.right])

                nodes.pop()

        return ans


if __name__ == '__main__':
    s = Codec()

    root = TreeNode(5)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(2)
    d = TreeNode(4)
    e = TreeNode(3)
    f = TreeNode(1)

    root.left = a
    root.right = b

    b.left = c
    b.right = d

    c.left = e
    c.right = f

    r = s.serialize(root)

    print(r)

    print(str(root) == str(s.deserialize(r)))
