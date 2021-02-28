class Node:
    def __init__(self, name, permission='N'):
        self.name = name
        self.permission = permission
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def add_path(self, inp):
        split_inp = inp.split(' ')
        pm = split_inp[0]
        pt = list(filter(lambda i: i, split_inp[1].split('/')))
        if len(pt) == 1 and not self.root:
            self.root = Node(pt[0], pm)
            return
        if len(pt) == 1 and self.root:
            self.root.permission = pm
            return
        if not self.root:
            self.root = Node(pt[0])
            cur = self.root
            for p in pt[1:-1]:
                cnode = Node(p)
                cur.children.append(cnode)
                cur = cnode
            enode = Node(pt[-1], pm)
            cur.children.append(enode)

        elif self.root:
            pass
        else:
            pass

