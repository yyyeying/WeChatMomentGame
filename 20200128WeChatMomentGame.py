# ********************************
# 朋友圈老虎机游戏模拟
# 作者：夜莺夜影
# 2020.01.28
# ********************************

import random
import matplotlib.pyplot as plt


def wechat_game(time):
    bingo_list = [[1, 2, 3, 4, 5, 6],
                  [1, 2, 3, 4, 5],
                  [1, 2, 3, 4],
                  [1, 2, 3],
                  [1, 2],
                  [1]]      # 第一次骰子点数对应的第二次的中奖点数
    prize_list = [0.88, 1.88, 3.88, 8.88, 12.88, 28.88]     # 中奖金额
    str_result = '第' + str(time + 1) + '次 '
    prize = -2.99           # 起始交2.99元
    number_first = random.randint(1, 6)
    number_second = random.randint(1, 6)
    str_result += '点数：' + str(number_first) + ', ' + str(number_second) + '  '
    if number_second in bingo_list[number_first - 1]:
        prize_money = prize_list[number_first - 1]
        str_result += '中奖 ' + str(prize_money)
        prize += prize_money
    else:
        str_result += '未中'
    # print(str_result)
    return prize


if __name__ == "__main__":
    plt.figure(figsize=(20, 10), dpi=72)
    myplot = plt.subplot(111)
    myplot.spines['right'].set_color('none')
    myplot.spines['top'].set_color('none')
    myplot.xaxis.set_ticks_position('bottom')
    myplot.spines['bottom'].set_position(('data', 0))
    myplot.yaxis.set_ticks_position('left')
    myplot.spines['left'].set_position(('data', 0))

    total_players = 10      # 总玩家数
    total_times = 10        # 每个玩家的次数
    time_list = list(range(1, total_times + 1))

    time_positive = 0       # 盈利次数
    time_negative = 0       # 亏损次数
    time_zero = 0           # 不赚不赔次数
    for player in range(total_players):
        total_prize = 0
        total_prize_list = []
        for i in range(total_times):
            total_prize += wechat_game(i)
            total_prize_list.append(total_prize)
            '''
            if total_prize > 0:     # 止盈策略
                # print('玩家' + str(player) + ', ' + str(i+1) + '次')
                break
            '''
        # print('整体盈利：' + str('%.2f' % total_prize))
        plt.plot(time_list, total_prize_list, linewidth=1)
        if total_prize > 0:
            time_positive += 1
        elif total_prize < 0:
            time_negative += 1
        else:
            time_zero += 1
    print('盈利次数：' + str(time_positive))
    print('亏损次数：' + str(time_negative))
    print('不赚不赔次数：' + str(time_zero))

    plt.xlabel('times')
    plt.ylabel('money')
    plt.show()


