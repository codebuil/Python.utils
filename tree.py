class TreeNode:
    def __init__(self, label):
        self.label = label
        self.items = []
        self.nodes = []

    def additem(self, label):
        self.items.append(label)

    def referenceit(self, node):
        self.nodes.append(node)

    def report(self, depth=0, stack=None):
        if stack is None:
            stack = []

        if depth == 0:
            print(self.label)
            stack.append(self.label)
        else:
            stack.append(self.label)

        for i in range(len(stack)):
            print("    ", end='')

        print(self.label)

        for node in self.nodes:
            node.report(depth + 1, stack)

        stack.pop()

def main():
    root = TreeNode("Root")
    x86 = TreeNode("X86")
    arm6 = TreeNode("Arm6")
    arm7 = TreeNode("Arm7")
    arm8 = TreeNode("Arm8")
    arm6.referenceit(arm7)
    arm6.referenceit(arm8)
    x86.referenceit(TreeNode("8086"))
    x86.referenceit(TreeNode("80186"))
    x86.referenceit(TreeNode("80286"))
    x86.referenceit(TreeNode("80386"))
    x86.referenceit(TreeNode("80486"))
    root.referenceit(x86)
    root.referenceit(arm6)
    root.report()


print("\x1bc\x1b[43;30m")

main()

