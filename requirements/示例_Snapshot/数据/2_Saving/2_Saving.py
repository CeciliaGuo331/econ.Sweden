#================== 2_Saving.py ==================
# 本程序绘制了中国储蓄率和其他国家横向对比等相关变量1970-2023年变量的折线图
# 数据来源World Bank：hhtps://data.worldbank.org

#===========================================
# 配置环境、导入可视化模块和数据处理模块
from visualization_module import*
import numpy as np

# 定义要显示的x轴刻度标签（字符串格式，对应CSV中的年份）
ticks = [str(year) for year in range(1970, 2023, 10)]



# ================== 图一： 国家储蓄率对比 ==================
the_title='Figure5:Savings rates of China and developed countries'
x_label='YEAR'
y_label='PERCENT'
line_chart('China.csv',ticks,'China','-','^')
line_withouttick('Korea.csv','Korea','-','^')
line_withouttick('Japan.csv','Japan','-','D')
line_withouttick('France.csv','France','-','o')
line_withouttick('United States.csv','United States','-','s')
line_withouttick('United Kindom.csv','United Kindom','-','*')
information(the_title,x_label,y_label)
plt.ylim(0,60)
plt.xlim(1970,2023)
picture_name='Fig1_Developed_countries'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()


# ================== 图二： BRICS国家储蓄率对比 ==================

the_title='Figure6:Savings rates of BRICS'
x_label='YEAR'
y_label='PERCENT'
line_chart('China.csv',ticks,'China','-','^')
line_withouttick('Russian Federation.csv','Russian Federation','-','^')
line_withouttick('India.csv','India','-','D')
line_withouttick('Brazil.csv','Brazil','-','o')
information(the_title,x_label,y_label)
plt.ylim(0,60)
plt.xlim(1975,2023)
picture_name='Fig2_BRICS'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()