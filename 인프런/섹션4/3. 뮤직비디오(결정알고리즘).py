n, m = map(int, input().split())
song_len = list(map(int, input().split()))
maxx = max(song_len)

lt = 1
rt = sum(song_len)
ret = 0

def count(dvd_size):
    cnt = 1
    sum = 0

    for song in song_len:
        if sum + song <= dvd_size:
            sum += song
        else:
            cnt += 1
            sum = song
    return cnt

while lt <= rt:
    mid = (lt + rt) // 2
    dvd_cnt = count(mid)
    
    if mid >= maxx and dvd_cnt <= m:
        ret = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(ret)
            
