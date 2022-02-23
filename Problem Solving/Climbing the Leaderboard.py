import bisect


def climbingLeaderboard(ranked, player):
    rank = list(set(ranked))
    rank.sort()
    player.sort()
    resp = ""
    x = len(rank)+1

    for item in player:
        if resp != "":
            resp += "\n"
        resp += f"{x - bisect.bisect(rank, item)}"
    return resp


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)
