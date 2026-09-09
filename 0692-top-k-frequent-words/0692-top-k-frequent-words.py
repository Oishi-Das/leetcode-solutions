class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        class Item:
            def __init__(self, word):
                self.word = word

            def __lt__(self, other):
                if freq[self.word] == freq[other.word]:
                    return self.word > other.word
                return freq[self.word] < freq[other.word]

        heap = []

        for word in freq:
            heapq.heappush(heap, Item(word))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(heapq.heappop(heap).word)

        return result[::-1]
        

        