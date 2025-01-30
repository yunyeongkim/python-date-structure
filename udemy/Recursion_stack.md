# Binary Search Tree: delete_node(28) 스택 분석

## 1. 트리 구조 (삭제 전)

```
        47
       /  \
     21    76
    / \   /  \
  18  28 52  82
      /  \
    25   29
```

---

## 2. delete_node(28) 함수 호출 스택 (Push 과정)

### (1) delete_node(28) 호출

```
1. delete_node(28)
   -> call -> __delete_node(self.root[47] , value[28])
```

- 루트 노드 `47`에서 `28`을 찾아야 함.
    
- `__delete_node(47, 28)` 호출.
    

---

### (2) __delete_node(47, 28) 실행

```
### current_node : 47 / value: 28
2. __delete_node (47 , 28)
if value[28] < current_node.value[47]:  
    current_node[47].left[21] = __delete_node(current_node[47].left[21], value[28])
    -> call -> __delete_node(21 , 28)
```

- `28`이 `47`보다 작으므로 **왼쪽 서브트리 탐색**.
    
- `__delete_node(21, 28)` 호출.
    

---

### (3) __delete_node(21, 28) 실행

```
### current_node : 21 / value : 28
3. __delete_node(21, 28)
elif value[28] > current_node.value[21]:  
    current_node[21].right[28] = __delete_node(current_node[21].right[28], value[28])
```

- `28`이 `21`보다 크므로 **오른쪽 서브트리 탐색**.
    
- `__delete_node(28, 28)` 호출.
    

---

### (4) __delete_node(28, 28) 실행

```
4. __delete_node(28,28)
sub_tree_min = self.min_value(current_node.right[29]) # -> 29
current_node.value = sub_tree_min  # 28 → 29
current_node.right = __delete_node(current_node.right, sub_tree_min)
   -> called __delete_node(29, 29)
```

- **삭제할 노드** `**28**` **발견!**
    
- 왼쪽, 오른쪽 자식이 모두 존재하므로 **오른쪽 서브트리의 최소값(29)으로 대체**.
    
- **즉,** `**28**` **→** `**29**`**로 변경됨**.
    
- 이제 **원래** `**29**` **위치의 노드를 삭제해야 하므로** `**__delete_node(29, 29)**` **호출**.
    

---

### (5) __delete_node(29, 29) 실행

```
5. __delete_node(29,29)
return current_node : -> __delete_node(current_node.right, sub_tree_min)
    call -> __delete_node(None, 29)
```

- `29`을 삭제해야 하지만, `29`는 **자식이 없는 노드**이므로 단순히 `None`을 반환.
    
- `__delete_node(None, 29)` 호출.
    

---

### (6) __delete_node(None, 29) 실행

```
### current_node = None / value= 29
6.__delete_node(None,29)
if current_node == None:
    return None
```

- `None` 노드가 입력되었으므로 `None`을 반환.
    

---

## 3. 스택에서 함수가 반환되는 과정 (Pop)

### (5) __delete_node(None, 29) 반환

```
5 called, __delete_node(None,29)
return None.
```

- `29`를 삭제한 결과 `**None**` **반환**.
    

---

### (4) __delete_node(28, 28) 반환

```
4 called, __delete_node(28,28)
current_node.right = __delete_node(28,28) : None
return current_node [29] ✅ (28 → 29로 변경됨)
```

- `current_node.right = None` (즉, 원래 `29` 위치 삭제됨).
    
- **최종적으로** `**28 → 29**`**가 되며,** `**29**`**를 반환**.
    

---

### (3) __delete_node(21, 28) 반환

```
3 called, __delete_node(21, 28)
current_node[21].right = __delete_node(21, 28) : 29
return current_node [21]
```

- `current_node[21].right = 29` (즉, `28`이 `29`로 대체됨).
    
- 최종적으로 `21` 반환.
    

---

### (2) __delete_node(47, 28) 반환

```
2 called,  __delete_node (47 , 28)
current_node[47].left = returned [21] ✅
return current_node [47]
```

- `current_node[47].left = 21` (왼쪽 서브트리가 변하지 않음).
    
- 최종적으로 `47` 반환.
    

---

## 4. 최종 트리 구조 (28 → 29로 변경됨)

```
        47
       /  \
     21    76
    / \   /  \
  18  29 52  82
     /
   25
```

✅ **28이 삭제되고, 29로 대체됨**.  
✅ **Stack이 올바르게 Pop되면서 트리가 수정됨**.