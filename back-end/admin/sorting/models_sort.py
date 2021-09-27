from dataclasses import dataclass


@dataclass
class Sorting(object):
    random_array = []

    @property
    def random_array(self) -> []: return self._random_array

    @random_array.setter
    def random_array(self, random_array): self._random_array = random_array

    def bubble_sort(self):
        arr = self.random_array
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def merge_sort(param: []):
        arr = param
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        low = Sorting.merge_sort(arr[:mid])
        high = Sorting.merge_sort(arr[mid:])
        arr = []
        l = h = 0
        while l < len(low) and h < len(high):
            if low[l] < high[h]:
                arr.append(low[l])
                l += 1
            else:
                arr.append(high[h])
                h += 1
        arr += low[l:]
        arr += high[h:]
        return arr

    @staticmethod
    def quick_sort(param: []):
        arr = param
        if len(arr) < 2:
            return arr
        pivot = len(arr) // 2
        low, mid, high = [], [], []
        for value in arr:
            if value < arr[pivot]:
                low.append(value)
            elif value > arr[pivot]:
                high.append(value)
            else:
                mid.append(value)
        return Sorting.quick_sort(low) + Sorting.quick_sort(mid) + Sorting.quick_sort(high)