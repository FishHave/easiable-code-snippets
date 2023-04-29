func sort(arr int[]) int[] {
	len := len(arr);

    for i := 0; i < len - 1; i++ {
        for j := 0; j < len - 1 - i; j++ {
            if arr[j] > arr[j + 1] {
                var temp := arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
        }
    }

    return arr;
} 