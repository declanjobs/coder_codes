class CacheData:

    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.cap = capacity
        self.cache = {}
        self.cache_size = 0

        self.first = CacheData(0,0)
        self.last = CacheData(-1,-1)

        self.first.next = self.last
        self.last.prev = self.first


    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key in self.cache:
            value = self.cache[key].value
            self.remove(self.cache[key])
            self.add(key, value)
            return value
        else:
            return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.cache:
            self.remove(self.cache[key])
            #self.touch(key)
        self.add(key, value)

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del self.cache[node.key]
        self.cache_size -= 1

    def touch(self, k):
        #self.debug()
        node = self.cache[k]
        self.remove(node)
        #self.cache_size -= 1
        self.move_to_first(node)
        #self.debug()

    def move_to_first(self, node):
        #print("move_to_first", node.key)
        #print(self.first.next.key)
        #self.debug()
        node.next = self.first.next
        node.prev = self.first
        self.first.next,  node.next.prev = node, node
        #print(self.first.next.key)
        #self.debug()

    def add(self, k, v):
        t = CacheData(k, v)
        self.move_to_first(t)
        self.cache[k] = t

        #print(self.cache_size, self.cap)
        if self.cache_size >= self.cap:
            to_del = self.last.prev
            #print("del", to_del.key, to_del.prev.key)
            self.remove(self.last.prev)

        self.cache_size += 1

        #self.debug()
        #print(self.cache, self.cache_size)


    def debug(self):

        p = ""

        t = self.first
        i = 0

        while t:
            p += str(t.key)
            p += "->"
            t = t.next

            if i > 5:
                break

            i += 1

        print(p)

        return

        p = ""

        t = self.last
        i = 0

        while t:
            p += str(t.key)
            p += "->"
            t = t.prev

            if i > 5:
                break

            i += 1

        print(p)






