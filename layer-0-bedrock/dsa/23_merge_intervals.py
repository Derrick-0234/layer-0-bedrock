from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    out = [intervals[0]]
    for s, e in intervals[1:]:
        last = out[-1]
        if s <= last[1]:
            last[1] = max(last[1], e)
        else:
            out.append([s, e])
    return out
if __name__ == "__main__":
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    print("ok")
