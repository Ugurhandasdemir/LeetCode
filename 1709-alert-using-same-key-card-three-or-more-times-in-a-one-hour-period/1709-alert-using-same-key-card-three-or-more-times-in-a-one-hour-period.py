class Solution(object):
    def alertNames(self, keyName, keyTime):
        def to_minutes(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m

        from collections import defaultdict

        workers = defaultdict(list)

        for i, name in enumerate(keyName):
            workers[name].append(to_minutes(keyTime[i]))

        answer = []

        for name, times in workers.items():
            times.sort()
            for i in range(2, len(times)):
   
                if times[i] - times[i - 2] <= 60:
                    answer.append(name)
                    break  

        return sorted(answer)
