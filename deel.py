import numpy as np
import matplotlib.pyplot as plt

ma = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
      '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
      'C': 12, 'D': 13, 'E': 14, 'F': 15}

f = open("20191114-1.txt", "r")
s = f.readlines()
vs = []
vs_t = []

rs = []
rs_t = []

cs = []
cs_t = []

ps = []
ps_t = []

fs = []
fs_t = []

rc = []
rc_t = []

cc = []
cc_t = []

pc = []
pc_t = []

fc = []
fc_t = []

print(s[2].strip())  # 打印第一个数据
rtime0 = s[1][12:24]
print(rtime0)  # 起始时间str
time0 = int(rtime0[0:2]) * 3600 + int(rtime0[3:5]) * 60 + float(rtime0[6:])
print(time0)  # 起始时间s

for i in range(len(s)):
    if s[i][0] == '[':
        temp = s[i]
        rtime = temp[12:24]
        time = int(rtime[0:2]) * 3600 + int(rtime[3:5]) * 60 + float(rtime[6:]) - time0
        data = s[i + 1]
        for j in range(0, len(data) - 9, 3):
            if (data[j:j + 8] == '01 03 02'):
                mb = data[j + 9:j + 11] + data[j + 12:j + 14]
                tab = 0
                for k in mb:
                    tab = tab * 16 + ma[k]
                trs = str(time) + '	' + str(tab)
                rs.append(trs)
            if (data[j:j + 8] == '02 03 02'):
                mb = data[j + 9:j + 11] + data[j + 12:j + 14]
                tab = 0
                for k in mb:
                    tab = tab * 16 + ma[k]
                crs = str(time) + '	' + str(tab)
                cs.append(crs)
            if (data[j:j + 8] == '03 03 02'):
                mb = data[j + 9:j + 11] + data[j + 12:j + 14]
                tab = 0
                for k in mb:
                    tab = tab * 16 + ma[k]
                prs = str(time) + '	' + str(tab)
                ps.append(prs)
            if (data[j:j + 8] == '04 03 02'):
                mb = data[j + 9:j + 11] + data[j + 12:j + 14]
                tab = 0
                for k in mb:
                    tab = tab * 16 + ma[k]
                hrs = str(time) + '	' + str(tab)
                fs.append(hrs)
            if (data[j:j + 8] == '05 03 1C'):
                mvs = data[j + 54:j + 56]
                tab = 0
                for k in mvs:
                    tab = tab * 16 + ma[k]
                tab = (tab * 256 - 32768) / 1000
                if (tab < -32.0):
                    tab = 0
                if (tab > 32.0):
                    tab = 0
                vvs = str(time) + '	' + str(tab)
                vs.append(vvs)
            if (data[j:j + 8] == '06 03 02'):
                # rcc=data[j+9:j+11]+data[j+12:j+14]
                # tab=0
                # for k in rcc:
                #     tab=tab*16+ma[k]
                # tab=tab*70*1.2/32767
                # trc=str(time)+'	'+str(tab)
                # rc.append(trc)
                # ccc=data[j+15:j+17]+data[j+18:j+20]
                # tab=0
                # for k in ccc:
                #     tab=tab*16+ma[k]
                # tab=tab*70*1.2/32767
                # tcc=str(time)+'	'+str(tab)
                # cc.append(tcc)
                # pcc=data[j+21:j+23]+data[j+24:j+26]
                # tab=0
                # for k in pcc:
                #     tab=tab*16+ma[k]
                # tab=tab*70*1.2/32767
                # tpc=str(time)+'	'+str(tab)
                # pc.append(tpc)
                # fcc=data[j+27:j+29]+data[j+30:j+32]
                # tab=0
                # for k in fcc:
                #     tab=tab*16+ma[k]
                # tab=tab*70*1.2/32767
                # tfc=str(time)+'	'+str(tab)
                # fc.append(tfc)

                # 回实验室以后单独测试了单电机的电流数据
                # 第一次实验： 2500rpm，测试倾斜度对电流的影响
                # 第二次实验： 3000rpm，测试稳态电流数据
                pcc = data[j + 9:j + 11] + data[j + 12:j + 14]
                tab = 0
                for k in pcc:
                    tab = tab * 16 + ma[k]
                tab = tab * 70 * 1.2 / 32767
                tpc = str(time) + '	' + str(tab)
                if (len(pc) == 0 or tab != pc[-1]):
                    pc_t.append(time)
                    pc.append(tab)
# print(vs)
# print(cs)
# print(ps)
# print(fs)
# print(rc)
# print(cc)
# print(pc)
# print(fc)

# with open("d_rs.txt","w") as g:
# 	for i in rs:
# 		g.writelines(i)
# 		g.writelines('\n')
# with open("d_cs.txt","w") as g:
# 	for i in cs:
# 		g.writelines(i)
# 		g.writelines('\n')
# with open("d_ps.txt","w") as g:
# 	for i in ps:
# 		g.writelines(i)
# 		g.writelines('\n')
# with open("d_fs.txt","w") as g:
# 	for i in fs:
# 		g.writelines(i)
# 		g.writelines('\n')
# with open("d_rc.txt","w") as g:
# 	for i in rc:
# 		g.writelines(i)
# 		g.writelines('\n')
# with open("d_cc.txt","w") as g:
# 	for i in cc:
# 		g.writelines(i)
# 		g.writelines('\n')
with open("d_pc.txt", "w") as g:
    for i in range(len(pc)):
        g.writelines(str(pc[i]))
        g.writelines('\n')
# with open("d_fc.txt","w") as g:
# 	for i in fc:
# 		g.writelines(i)
# 		g.writelines('\n')
# with open("d_vs.txt","w") as g:
#     for i in vs:
#         g.writelines(i)
#         g.writelines('\n')

# plt.figure(figsize=(10,5), dpi=200)
# pc_arr = np.asarray(pc)
# pc_t_arr = np.asarray(pc_t)
# f = np.polyfit(pc_t_arr,pc_arr,3)
# p = np.poly1d(f)
# yvals = p(pc_t_arr)
# plt.plot(pc_t, pc, color = 'blue')
# plt.plot(pc_t, yvals, color = 'red')
#
# plt.plot(pc_t[0], yvals[0], marker='o', color = 'red')
# annotation1 = plt.annotate("(%3.1fs,%3.1fA)" %(pc_t[0],yvals[0]), xy=(pc_t[0],yvals[0]), xytext=(35, 10), textcoords='offset points', weight='heavy', color='red',
#              bbox=dict(boxstyle='round,pad=0.5', fc='yellow', ec='k', lw=1, alpha=0.5))
# plt.plot(pc_t[-1], yvals[yvals.size-1], marker='o', color = 'red')
# annotation2 = plt.annotate("(%3.1fs,%3.1fA)" %(pc_t[-1],yvals[yvals.size-1]), xy=(pc_t[-1],yvals[yvals.size-1]), xytext=(-50, 60), textcoords='offset points', weight='heavy', color='red',
#              bbox=dict(boxstyle='round,pad=0.5', fc='yellow', ec='k', lw=1, alpha=0.5))
#
# plt.title('Current-time figure')
# plt.xlabel('time /s')
# plt.ylabel('current /A')
# plt.show()


def Show(y_t, y):
    # 参数为一个list

    fig = plt.figure(figsize=(10,5), dpi=200)

    y_arr = np.asarray(y)
    y_t_arr = np.asarray(y_t)
    f = np.polyfit(y_t_arr, y_arr, 3)
    p = np.poly1d(f)
    yvals = p(y_t_arr)
    plt.plot(y_t, y, color='blue')
    plt.plot(y_t, yvals, color='red')

    plt.plot(y_t[0], yvals[0], marker='o', color='red')
    annotation1 = plt.annotate("(%3.1fs,%3.1fA)" % (y_t[0], yvals[0]), xy=(y_t[0], yvals[0]), xytext=(35, 10),
                               textcoords='offset points', weight='heavy', color='red',
                               bbox=dict(boxstyle='round,pad=0.5', fc='yellow', ec='k', lw=1, alpha=0.5))
    plt.plot(y_t[-1], yvals[yvals.size - 1], marker='o', color='red')
    annotation2 = plt.annotate("(%3.1fs,%3.1fA)" % (y_t[-1], yvals[yvals.size - 1]),
                               xy=(y_t[-1], yvals[yvals.size - 1]), xytext=(-50, 60), textcoords='offset points',
                               weight='heavy', color='red',
                               bbox=dict(boxstyle='round,pad=0.5', fc='yellow', ec='k', lw=1, alpha=0.5))

    # len_y = len(yvals)
    # # x = range(len_y)
    # x = y_t
    # _y = [yvals[-1]] * len_y
    #
    # # ax1 = fig.add_subplot(1, 1, 1)
    # # ax1 = plt.plot(x, y, color='blue')
    #
    # # line_x = plt.plot(x, _y, color='skyblue')[0]
    # # line_y = plt.axvline(x=len_y - 1, color='skyblue')
    #
    # # ax1.set_title('aaa')
    #
    # line_x = plt.plot(x, _y, color='skyblue')[0]
    # line_y = plt.axvline(x=len_y - 1, color='skyblue')
    #
    # # 标签
    # text0 = plt.text(len_y - 1, y[-1], str(y[-1]), fontsize=10)
    #
    # def scroll(event):
    #     axtemp = event.inaxes
    #     x_min, x_max = axtemp.get_xlim()
    #     fanwei_x = (x_max - x_min) / 10
    #     if event.button == 'up':
    #         axtemp.set(xlim=(x_min + fanwei_x, x_max - fanwei_x))
    #     elif event.button == 'down':
    #         axtemp.set(xlim=(x_min - fanwei_x, x_max + fanwei_x))
    #     fig.canvas.draw_idle()
    #
    # # 这个函数实时更新图片的显示内容
    # def motion(event):
    #     try:
    #         temp_motion = y[int(np.round(event.xdata))]
    #         for i in range(len_y):
    #             _y[i] = temp_motion
    #         line_x.set_ydata(_y)
    #         line_y.set_xdata(event.xdata)
    #         ######
    #         text0.set_position((event.xdata, temp_motion))
    #         text0.set_text(str(temp_motion))
    #
    #         fig.canvas.draw_idle()  # 绘图动作实时反映在图像上
    #     except:
    #         pass
    #
    # fig.canvas.mpl_connect('scroll_event', scroll)
    # fig.canvas.mpl_connect('motion_notify_event', motion)

    plt.title('Current-time figure')
    plt.xlabel('time /s')
    plt.ylabel('current /A')
    plt.show()

Show(pc_t, pc)