def sort(arr:list):
    len = len(list);
    
    for i in range(len - 1):
        for j in range(len - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
    
    return arr;