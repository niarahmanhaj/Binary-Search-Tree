class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key 

class BST: 
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else: 
                self._insert(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
        else:
            return

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.val == key:
            return True
        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._get_min(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        return node

    def _get_min(self, node):
        if node.left is None:
            return node
        return self._get_min(node.left)

    def pre_order(self):
        self._pre_order(self.root)
        print()

    def _pre_order(self, node):
        if node is not None:
            print(node.val, end=" ")
            self._pre_order(node.left)
            self._pre_order(node.right)

    def in_order(self):
        self._in_order(self.root)
        print()

    def _in_order(self, node):
        if node is not None:
            self._in_order(node.left)
            print(node.val, end=" ")
            self._in_order(node.right)

    def post_order(self):
        self._post_order(self.root)
        print()

    def _post_order(self, node):
        if node is not None:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.val, end=" ")

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('        ' * level + '└── ' + str(node.val))
            self.print_tree(node.left, level + 1)

if __name__ == "__main__":
    pohon = BST()
    
    data_insert = [40, 25, 3, 65, 12, 30, 60, 85, 7, 15]
    print(f"1. Meng-insert data: {data_insert}")
    for nilai in data_insert:
        pohon.insert(nilai)
        
    print("\n--- Struktur BST Setelah di-Insert ---")
    pohon.print_tree(pohon.root)
    
    print("\n2. Melakukan Pencarian (Search):")
    print(f"   Apakah 1 ditemukan? -> {pohon.search(1)}")
    print(f"   Apakah 85 ditemukan? -> {pohon.search(85)}")
    
    print("\n3. View Pre-order :", end=" ")
    pohon.pre_order()
    
    print("4. View In-order  :", end=" ")
    pohon.in_order()
    
    print("5. View Post-order:", end=" ")
    pohon.post_order()
    
    print("\n6. Menghapus data (Delete): 3")
    pohon.delete(3)
    
    print("\n--- Struktur BST Setelah Angka 3 Dihapus ---")
    pohon.print_tree(pohon.root)
