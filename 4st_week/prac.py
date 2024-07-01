#버블 정렬
#중간에 다 정렬돼도 끝날때까지 반복
def bubblesort(arr):
    for i in range(len(arr) - 1):
        # 이미 구한 최댓값은 범위에서 제외
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

#선택 정렬
def selectionsort(arr):
    for i in range(len(arr) - 1):
        min = i
        # min에 제일 작은 값의 인덱스를 저장 후, 처음 요소와 같지 않으면 교환
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        if min != i:
            arr[min],arr[i] = arr[i],arr[min]
    return arr

def insertionsort(arr):
    #맨 앞에거는 안해도 되기 때문에 인덱스가 0이 아닌 1부터 시작, 끝까지 해야함
    for i in range(1, len(arr)):
        #뒤에서부터 비교하면서 와야하기 때문에 뒤에서부터 -1씩 더하는 range씀
        for j in range(i,0,-1):
            #앞에게 뒤에거보다 크면 위치 바꿈
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr

#기준을 잡고 그 값보다 작으면 앞에 밀어 넣는 형식의 알고리즘
def quicksort(arr, start, end):
    #pivot보다 작은구간은 문제 없지만, pivot보다 큰 구간은 마지막에서 start보다 end가 커져 에러나기때문에
    #어차피 정렬 다 된것이므로 마지막꺼는 반환 안해도 됨
    if start > end:
        return

    i = start-1
    #끝에 있는 요소를 기준으로 잡음
    pivot = arr[end]
    #시작부터 끝보다 1작을때까지(끝에 요소는 pivot)
    for j in range(start, end):
        #j는 현재 보고있는 곳, i는 pivot보다 작은것들이 들어갈 공간들
        #현재 보고있는 것이 기준(pivot)보다 작다면 왼쪽 시작점부터 차근차근 채움
        #i의 초기 값이 정렬하려는 공간의 시작점이므로 i+1의 의미가 왼쪽 처음부터 차근차근 넣겠다는 얘기
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    #pivot을 큰거와 작은거 사이에 넣음(i까지는 작은게 들어가있음)
    arr[i+1], arr[end] = arr[end], arr[i+1]

    #pivot보다 작은것들은 정렬이 안되어있으니
    #start를 처음으로 end를 i로 (pivot은 i+1에 위치해있으니까) 재귀함수를 불러 작은것들이 다 정렬되게 함
    quicksort(arr, start, i)
    #pivot보다 큰것들도 정렬이 안되어있으니
    #큰것들은 pivot보다 다 오른쪽에 있는것이므로 start를 i+2(pivot은 i+1에 위치해있으니까)
    #end를 끝으로 재귀함수를 불러 큰것들이 다 정렬되게 함
    quicksort(arr, i + 2, end)

    return arr

#두 정렬된 배열을 받고
def merge(arr1, arr2):
	#새 배열에 정렬해서 리턴
    result = []
    i = j = 0
    #두 배열 비교하면서 작은거 먼저 result에 append한 후 다음 요소로 넘김
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
	#요소 끝까지 비교 안했으면 나머지 넣음(어차피 정렬된 배열이라 append만 하면 됨)
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

	#마찬가지
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

def mergesort(lst):
    #데이터를 낱개로 나눠버리면 정렬할것도 없이 하나라 이미 정렬되어있다고 간주
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    #가운데를 기준으로 왼쪽과 오른쪽 정렬하기
    L = lst[:mid]
    R = lst[mid:]
    return merge(mergesort(L), mergesort(R))


class BinaryMinHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    # 들어온 노드 루트노드로 보내는 함수
    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    # 힙 트리 유지시키는 함수
    def _percolate_down(self, cur):
        smallest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        # 왼쪽이든 오른쪽이든 자식노드가 부모노드보다 작다면 스위치
        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            # 반복
            self._percolate_down(smallest)

    # 노드 넣는 함수
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    # 제일 작은 값 추출 (부모노드)
    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root

def heapsort(lst):
    # 최소 힙 인스턴스 만들고
    minheap = BinaryMinHeap()

    # 요소들 다 넣어준 다음
    for elem in lst:
        minheap.insert(elem)

    # extract하면 항상 루트노드에 최솟값이 들어가기 때문에 뽑은것들 계속 result에 append하면 됨
    return [minheap.extract() for _ in range(len(lst))]