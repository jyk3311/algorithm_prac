class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

class Node:
    def __init__(self, val = 0, next =None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Node(val, self.top)
    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = node.next
        return node.val
    def is_empty(self):
        return self.top is None

class Queue:
    def __init__(self):
        self.front = None

    def push(self, val):
        if not self.front:
            self.front = Node(val)
            return

        node = self.front
        while node.next:
            node = node.next

        node.next = Node(val)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front=node.next
        return node.val

    def is_empty(self):
        return self.front is None

"""체이닝 방식의 해시테이블"""

class HashNode:
    #딕셔너리처럼 key와 value가 있고, 다음노드를 담을수 있는 next가 있음
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

    #modular연산(나머지 연산) 10으로 나눈 나머지만 해싱함.
class HashTable:
    def __init__(self):
        #10으로 나눈 나머지만 저장하기 때문에 크기는 10이면 됨
        self.size = 10
        #해시테이블에 10개만큼 빈 공간을 만듬
        self.table = [None] * self.size

    #key값을 받으면 10으로 나누어 나머지 반환하는 함수
    def _hash_function(self, key):
        return key % self.size

    #해시테이블에 해시노드 추가하는 함수
    def put(self, key, value):
        #idx는 해시테이블에 인덱스를 담음
        idx = self._hash_function(key)

        #만약 해시테이블 안에서 idx번째의 공간에 아직 데이터가 없다면 그자리에 넣고 아니면 연결리스트처럼 진행함
        #연결리스트는 위에 참고
        if self.table[idx] is None:
            self.table[idx] = HashNode(key, value)
        else:
            node = self.table[idx]
            while node.next:
                node = node.next
            node.next = HashNode(key,value)

    #key로 값 찾기
    def get(self, key):
        #해시테이블의 몇번째가 idx에 담김
        idx = self._hash_function(key)
        #node라는 빈 변수에 idx번째의 맨처음 값을 넣음
        node = self.table[idx]
        #노드의 값이 None일 때까지
        while node is not None:
            #node의 키랑 찾으려는 key랑 같다면 그 노드의 value를 반환
            #첫번째값이 key값이랑 같을수 있기 때문에 아래 if문이 node = node.next문보다 위에 있어야함.
            if node.key == key:
                return node.value
            node = node.next
        #다 뒤져봤는데도 없다면 -1 반환
        return -1

    #해시테이블에서 key값을 찾아 그 노드를 제거하는 함수
    #제거하는 방법은 제거하려는 노드의 앞뒤로 연결해 고립시키면 제거된것처럼 됨
    def remove(self,key):
        #해시테이블의 몇번째가 idx에 담김
        idx = self._hash_function(key)
        #node라는 빈 변수에 idx번째의 맨처음 값을 넣음(제거하려는 노드가 될 변수)
        node = self.table[idx]
        #제거하려는 노드 앞의 노드
        prev_node = None

        while node:
            if node.key == key:
                #이전 노드가 존재하면
                if prev_node:
                   prev_node.next = node.next
                #이전 노드가 존재하지 않는다면(제거하려는 노드가 처음에 넣은 노드라면)
                else:
                    self.table[idx] = node.next
                return
            prev_node = node
            node = node.next

class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self.items) - 1
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2
    #------------------------ 여기부터 --------------------------------
    #값 추출하는 함수
    def extract(self):
        #힙에 아무것도 없다면 반환값 없음
        if len(self.items) - 1 < 1:
            return None

        #root라는 빈 변수를 만들어 힙의 루트노드를 저장
        root = self.items[1]
        #힙의 마지막 노드를 루트노드에 저장
        self.items[1] = self.items[-1]
        #마지막거를 뽑음
        self.items.pop()
        #힙 정리 함수
        self._percolate_down(1)
        return root

    def _percolate_down(self, cur):
        #biggest는 현재 부모노드를 저장
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        #인덱스 접근이 배열의 크기를 넘어가면 안되기 때문에 앞에 제약을 검.
        #왼쪽 자식노드가 부모노드보다 크면 biggest를 왼쪽 자식으로 바꿈
        if left <= len(self.items) - 1 and self.items[left] > self.items[biggest]:
            biggest = left
        #오른쪽 자식노드가 부모노드보다 크면 biggest를 오른쪽 자식으로 바꿈
        if right <= len(self.items) - 1 and self.items[right] > self.items[biggest]:
            biggest = right
        #왼쪽이나 오른쪽 자식 노드로 바뀐거면, 위의 문장을 다시 실행해야함. 안바뀐거면 힙 정리가 끝난 상태여서 건들지 않아도 됨.
        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)