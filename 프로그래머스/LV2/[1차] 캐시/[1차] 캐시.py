def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in cities:
        i = i.lower()
        if cacheSize != 0:
            if i in cache:
                cache.remove(i)
                cache.append(i)
                answer +=1
            else:
                answer += 5
                if cache == []:
                    cache.append(i)
                else:
                    if len(cache) == cacheSize:
                        cache.remove(cache[0])
                        cache.append(i)
                    else:
                        cache.append(i)
        else:
            answer += 5
    return answer
