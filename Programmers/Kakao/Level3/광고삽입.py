def solution(play_time, adv_time, logs):
    totalTime = strToSecond(play_time)
    adTime = strToSecond(adv_time)

    dp = [0] * (totalTime + 1)
    for log in logs:
        startTime = strToSecond(log.split("-")[0])
        endTime = strToSecond(log.split("-")[1])
        dp[startTime] += 1
        dp[endTime] -= 1

    for i in range(1, totalTime + 1):
        dp[i] += dp[i-1]
    
    max_count, max_time = sum(dp[:adTime]), 0
    count = max_count

    for i in range(1, totalTime - adTime + 1):
        count = count - dp[i-1] + dp[i-1 + adTime]

        if count > max_count:
            max_count = count
            max_time = i

    return secondToStr(max_time)

def strToSecond(time):
    stamp = time.split(':')
    return int(stamp[0])*3600+int(stamp[1])*60+int(stamp[2])

def secondToStr(time):
    hours = time // 3600
    mins = (time % 3600) // 60
    secs = time % 60
    return '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))