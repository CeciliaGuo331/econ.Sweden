#================== 5_Housing.py ==================
# 本程序绘制了中国房价相关变量2000-2024年变量的折线图
# 数据来源World Bank：https://data.worldbank.org

#===========================================
# 配置环境、导入可视化模块和数据处理模块
from visualization_module import*
import numpy as np


# ================== 图一：房价销售额 ==================

# 定义要显示的x轴刻度标签（字符串格式，对应CSV中的年份）
ticks = [str(year) for year in range(1990, 2024, 5)]
xlim = [1990, 2024]

# 读取CSV文件
file_y1 = 'Housing_sales.csv'  # 左侧Y轴数据文件
file_y2 = 'Housing_area.csv'  # 右侧Y轴数据文件

# 读取数据
# 读取左侧Y轴数据
x1, y1, tick_locations1 = read_data(file_y1, ticks)
# 读取右侧Y轴数据
x2, y2, tick_locations2 = read_data(file_y2, ticks)

# 合并x轴刻度位置（取并集并排序）
tick_locations = sorted(list(set(tick_locations1 + tick_locations2)))

# ================== 绘图设置 ==================
plt.figure(num=1, figsize=(4, 3), dpi=400)

# 左侧Y轴（主坐标轴）
ax1 = plt.gca()
y1 = np.array(y1)/1000000
line1, = ax1.plot(x1, y1, color='blue', label='Commercial Housing Sales Revenue ', 
                  linestyle='-', linewidth=1)
ax1.set_xlabel('YEAR', fontproperties='KaiTi', fontsize=8)
ax1.set_ylabel('Housing Revenue (10^12 CNY)', fontproperties='KaiTi', color='blue', fontsize=8)
ax1.tick_params(axis='y', labelcolor='blue', labelsize=6)


# 右侧Y轴（次坐标轴）
ax2 = ax1.twinx()
y2 = np.array(y2)/1000000
line2, = ax2.plot(x2, y2, color='red', label='Commercial Housing Construction Area', 
                  linestyle='--', linewidth=1)
ax2.set_ylabel('Construction Area (10^9 m^2)', fontproperties='KaiTi', color='red', fontsize=8)
ax2.tick_params(axis='y', labelcolor='red', labelsize=6)

# 调整坐标轴刻度与范围
ax1.set_xticks(tick_locations)
ax1.set_xticklabels(ticks, fontproperties='KaiTi', rotation=45, fontsize= 6)  # 标签旋转45度防重叠
ax1.set_xlim(xlim[0],xlim[1])  # 动态调整x轴范围

# 图例与标题
lines = [line1, line2]
labels = [line.get_label() for line in lines]
plt.legend(lines, labels, prop={'family': 'KaiTi', 'size': 6},
           edgecolor='w', framealpha=0.8)

plt.title('Figure13:China\'s Housing Market', fontproperties='KaiTi', fontsize=8, pad=8)
plt.tight_layout()  # 自动调整布局

# 保存
plt.savefig('Fig1_Housing_total.png', dpi=400, bbox_inches='tight')
plt.show()


# ================== 图二：中国房价趋势 ==================

# 定义要显示的x轴刻度标签（字符串格式，对应CSV中的年份）
ticks = [str(year) for year in range(2010, 2025, 2)]
xlim = [2010, 2024]

the_title='Figure14:China\'s Housing Price growth rate'
x_label='YEAR'
y_label='%'
line_chart('Housing_price.csv',ticks,'Domestic Market','-','')
line_withouttick('Housing_price_1st_tier.csv','1st Tier City','-','')
line_withouttick('Housing_price_2nd_tier.csv','2nd Tier City','-','')
line_withouttick('Housing_price_3rd_tier.csv','3rd Tier City','-','')
information(the_title,x_label,y_label)
plt.xlim(xlim[0],xlim[1])
plt.savefig('Fig2_Housing_price.png', dpi=1000)#Save the picture
plt.show()




