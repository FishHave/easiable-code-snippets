def sort(arr:list):
    len = len(list);
    
    for i in range(len):
        for j in range(len - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
    
    return arr;