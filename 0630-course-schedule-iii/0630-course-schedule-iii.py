class Solution:
    def scheduleCourse(self, courses):
        import heapq

        courses.sort(key=lambda c: c[1])
        heap = []
        time = 0

        for duration, last_day in courses:
            heapq.heappush(heap, -duration)
            time += duration
            if time > last_day:
                time += heapq.heappop(heap)

        return len(heap)