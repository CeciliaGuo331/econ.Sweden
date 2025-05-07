#================== 4_Population.py ==================
# 本程序绘制了中国人口相关变量1960-2023年变量的折线图
# 数据来源World Bank：https://data.worldbank.org

#===========================================
# 配置环境、导入可视化模块和数据处理模块
from visualization_module import*
import numpy as np

# 定义要显示的x轴刻度标签（字符串格式，对应CSV中的年份）
ticks = [str(year) for year in range(1960, 2023, 10)]
xlim = [1960, 2023]

# ================== 图一：中国人口增长率 ==================

# CSV文件路径（需替换为实际路径）
file_y1 = 'Population_total.csv'  # 左侧Y轴数据文件
file_y2 = 'Population_growth_rate.csv'  # 右侧Y轴数据文件


# 读取数据
# 读取左侧Y轴数据
x1, y1, tick_locations1 = read_data(file_y1, ticks)
# 读取右侧Y轴数据
x2, y2, tick_locations2 = read_data(file_y2, ticks)

# 合并x轴刻度位置（取并集并排序）
tick_locations = sorted(list(set(tick_locations1 + tick_locations2)))

# 绘图设置
plt.figure(num=1, figsize=(4, 3), dpi=400)

# 左侧Y轴（主坐标轴）
ax1 = plt.gca()
y1 = [i/100000000 for i in y1]
line1, = ax1.plot(x1, y1, color='blue', label='China\'s total population', 
                  linestyle='-', linewidth=1)
ax1.set_xlabel('YEAR', fontproperties='KaiTi', fontsize=8)
ax1.set_ylabel('Total population (billion)', fontproperties='KaiTi', color='blue', fontsize=8)
ax1.tick_params(axis='y', labelcolor='blue', labelsize=6)


# 右侧Y轴（次坐标轴）
ax2 = ax1.twinx()
line2, = ax2.plot(x2, y2, color='red', label='China\'s population growth rate', 
                  linestyle='--', linewidth=1)
ax2.set_ylabel('Population annual growth rate', fontproperties='KaiTi', color='red', fontsize=8)
ax2.tick_params(axis='y', labelcolor='red', labelsize=6)

# 坐标轴刻度与范围
ax1.set_xticks(tick_locations)
ax1.set_xticklabels(ticks, fontproperties='KaiTi', rotation=45, fontsize= 6)  # 标签旋转45度防重叠
ax1.set_xlim(xlim[0],xlim[1])  # 动态调整x轴范围

# 图例与标题
lines = [line1, line2]
labels = [line.get_label() for line in lines]
plt.legend(lines, labels, prop={'family': 'KaiTi', 'size': 6},
           edgecolor='w', framealpha=0.8)

plt.title('Figure10:Population growth in China (1960-2023)', fontproperties='KaiTi', fontsize=8, pad=8)
plt.tight_layout()  # 自动调整布局

# 保存与显示
plt.savefig('Fig1_Population_total.png', dpi=400, bbox_inches='tight')
plt.show()


# ================== 图二：中国人口老龄化 ==================


the_title='Figure11:China\'s Proportion of Population Over 65'
x_label='YEAR'
y_label='%'
line_chart('ages_above_65.csv',ticks,'Population ages 65 and above (%)','-','')
information(the_title,x_label,y_label)
plt.xlim(xlim[0],xlim[1])
plt.savefig('Fig2_Aging_trend.png', dpi=1000)#Save the picture
plt.show()

# ================== 图三：中国城乡人口 ==================


the_title='Figure12:China\'s rural and urban population share'
x_label='YEAR'
y_label='%'
line_chart('Rural_population_share.csv',ticks,'Rural population share (%)','-','')
line_withouttick('Urban_population_share.csv','Urban population share (%)','-','')
information(the_title,x_label,y_label)
plt.xlim(xlim[0],xlim[1])
plt.savefig('Fig3_population_share.png', dpi=1000)#Save the picture
plt.show()