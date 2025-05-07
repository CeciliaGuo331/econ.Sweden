#================== 1_GDP.py ==================
# 本程序绘制了中国GDP相关变量1960-2023年变量的折线图
# 数据来源World Bank：https://data.worldbank.org

#===========================================
# 配置环境、导入可视化模块和数据处理模块
from visualization_module import*
import numpy as np

# 定义要显示的x轴刻度标签（字符串格式，对应CSV中的年份）
ticks = [str(year) for year in range(1960, 2023, 10)]
xlim = [1960, 2023]



# ================== 图一：GDP总量增长率 ==================

# 读取CSV文件
file_y1 = 'GDP_total.csv'  # 左侧Y轴数据文件
file_y2 = 'GDP_growth_rate.csv'  # 右侧Y轴数据文件

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
y1 = [i/1000000000000 for i in y1]
line1, = ax1.plot(x1, y1, color='blue', label='China\'s GDP', 
                  linestyle='-', linewidth=1)
ax1.set_xlabel('YEAR', fontproperties='KaiTi', fontsize=8)
ax1.set_ylabel('GDP (trillions of dollars)', fontproperties='KaiTi', color='blue', fontsize=8)
ax1.tick_params(axis='y', labelcolor='blue', labelsize=6)


# 右侧Y轴（次坐标轴）
ax2 = ax1.twinx()
line2, = ax2.plot(x2, y2, color='red', label='China\'s annual GDP growth rate', 
                  linestyle='--', linewidth=1)
ax2.set_ylabel('Annual GDP growth rate (%)', fontproperties='KaiTi', color='red', fontsize=8)
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

plt.title('Figure1:China\'s GDP growth', fontproperties='KaiTi', fontsize=8, pad=8)
plt.tight_layout()  # 自动调整布局

# 保存
plt.savefig('Fig1_GDP_total.png', dpi=400, bbox_inches='tight')
plt.show()


# ================== 图二：GDP里储蓄、投资占比 ==================

the_title='Figure2:China\'s gross savings'
x_label='YEAR'
y_label='%'
line_chart('saving_rate.csv',ticks,'Gross savings (% of GDP)','-','')
line_withouttick('investment.csv','investment of GDP (% of GDP)','-','')
information(the_title,x_label,y_label)
plt.xlim(xlim[0],xlim[1])
plt.savefig('Fig2_Gross_savings.png', dpi=1000)#Save the picture
plt.show()


# ================== 图三：GDP里进出口占比 ==================

the_title='Figure3:China\'s import and export'
x_label='YEAR'
y_label='%'
line_chart('import.csv',ticks,'Imports of goods and services (% of GDP)','-','')
line_withouttick('export.csv','Exports of goods and services (% of GDP)','-','')
information(the_title,x_label,y_label)
plt.xlim(xlim[0],xlim[1])
plt.savefig('Fig3_import_and_export', dpi=1000)#Save the picture
plt.show()

# ================== 图四：GDP里消费占比 ==================
the_title='Figure4:China\'s consumption'
x_label='YEAR'
y_label='%'
line_chart('final_consumption_expenditure.csv',ticks,'Final consumption of GDP (% of GDP)','-','')
line_withouttick('government_consumption.csv','government consumption of GDP (% of GDP)','-','')
line_withouttick('household_consumption.csv','household consumption of GDP (% of GDP)','-','')
information(the_title,x_label,y_label)
plt.xlim(xlim[0],xlim[1])
plt.savefig('Fig4_consumption.png', dpi=1000)#Save the picture
plt.show()

