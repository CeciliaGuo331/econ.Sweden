# 1980-2023年中国财政收支
from visualization_module import*
ticks=[str(x)for x in range(1980,2023,10)]
the_title='Figure15:China’s fiscal revenue and expenditure'
x_label='YEAR'
y_label=''
line_chart('fiscal expend.csv',ticks,'fiscal expenditure','-','')
line_withouttick('fiscal revenue.csv','fiscal revenue','-','')
information(the_title,x_label,y_label)
#plt.ylim(-10,30)
plt.xlim(1980,2023)
picture_name='China’s fiscal revenue and expenditure'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()


#1980-2011年中国政府预算外收支
from visualization_module import*
ticks=[str(x)for x in range(1980,2011,5)]
the_title='Figure16:China’s Extra budgetary income and expenditure'
x_label='YEAR'
y_label=''
line_chart('Extra budgetary income.csv',ticks,'Extra budgetary income','-','')
line_withouttick('Extra budgetary expenditure.csv','Extra budgetary expenditure','-','')
information(the_title,x_label,y_label)
#plt.ylim(-10,30)
plt.xlim(1980,2011)
picture_name='China’s Extra budgetary income and expenditure'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()

#2012-2023年中国地方政府债务余额
from visualization_module import*
ticks=[str(x)for x in range(2012,2024,1)]
the_title='Figure18:Balance of China’s local government debt'
x_label='YEAR'
y_label=''
line_chart('debt.csv',ticks,'Balance of China’s local government debt','-','')
information(the_title,x_label,y_label)
#plt.ylim(-10,30)
plt.xlim(2012,2024)
picture_name='Balance of China’s local government debt'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()

#2011-2023年中国政府财政自给率和土地财政依赖度
from visualization_module import*
ticks=[str(x)for x in range(2011,2024,1)]
the_title='Figure17:China’s self-sufficiency rate and dependence on land finance'
x_label='YEAR'
y_label='%'
line_chart('fiscal self rate.csv',ticks,'Fiscal self-sufficiency rate','-','')
line_withouttick('land dependence.csv','Land fiscal dependence','-','')
information(the_title,x_label,y_label)
#plt.ylim(-10,30)
plt.xlim(2011,2023)
picture_name='China’s self-sufficiency rate and dependence on land finance'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()

#2011-2023年中国东中西部财政自给率
from visualization_module import*
ticks=[str(x)for x in range(2011,2024,1)]
the_title='Figure20:China’s regional fiscal self-sufficiency rate'
x_label='YEAR'
y_label='%'
line_chart('east fiscal self rate.csv',ticks,'East','-','')
line_withouttick('center fiscal self rate.csv','Center','-','')
line_withouttick('west fiscal self rate.csv','West','-','')
information(the_title,x_label,y_label)
plt.ylim(20,80)
plt.xlim(2011,2023)
picture_name='China’s regional fiscal self-sufficiency rate'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()

#2011-2023年中国东中西部土地财政依赖度
from visualization_module import*
ticks=[str(x)for x in range(2011,2024,1)]
the_title='Figure21:China’s regional Land fiscal dependence'
x_label='YEAR'
y_label='%'
line_chart('east land dependence.csv',ticks,'East','-','')
line_withouttick('center land dependence.csv','Center','-','')
line_withouttick('west land dependence.csv','West','-','')
information(the_title,x_label,y_label)
plt.axhline(y=30, color='r', linestyle='--')
plt.ylim(10,60)
plt.xlim(2011,2023)
picture_name='China’s regional Land fiscal dependence'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()


'''
#2022年江苏省各地级市显性债务和隐性债务占比
from visualization_module import*
ticks=[str(x)for x in range(1,14,1)]
the_title='Proportion of explicit and implicit debt in various cities in Jiangsu Province in 2022'
x_label='region'
y_label='%'
line_chart('implicit debt.csv',ticks,'Implicit debt','-','')
line_withouttick('explicit debt.csv','Explicit debt','-','')
information(the_title,x_label,y_label)
#plt.ylim(10,60)
plt.xlim(1,14)
picture_name='Proportion of explicit and implicit debt in various cities in Jiangsu Province in 2022'
plt.savefig(picture_name, dpi=1000)#Save the picture
plt.show()
'''


#2022年江苏省各地级市显性债务和隐性债务占比
from visualization_module import*

# 横坐标标签映射
city_names = [
    '苏州市', '南京市', '无锡市', '南通市', '常州市',
    '徐州市', '扬州市', '盐城市', '泰州市', '镇江市',
    '淮安市', '宿迁市', '连云港市'
]

ticks = list(range(1, 14))  # 生成1-13的数字坐标
#the_title = 'Figure18:Proportion of explicit and implicit debt in Jiangsu Province in 2022'
the_title = '''Figure19:Proportion of explicit and implicit debt 
in Jiangsu Province in 2022'''

x_label = 'region'
y_label = '%'

line_chart('implicit debt.csv', [str(x) for x in ticks], 'Implicit debt', '-', '')
line_withouttick('explicit debt.csv', 'Explicit debt', '-', '')
information(the_title, x_label, y_label)

# 关键修改：设置自定义横坐标标签
plt.xticks(
    ticks=ticks,             # 坐标位置1-13
    labels=city_names,       # 对应的中文标签
    rotation=45,             # 标签旋转45度防重叠
    ha='right',              # 标签右对齐
    fontproperties='SimHei'  # 指定中文字体（根据你的系统字体调整）
)

plt.xlim(1, 14)
plt.tight_layout()  # 自动调整布局防止标签被截断
picture_name = 'Proportion of explicit and implicit debt in Jiangsu Province in 2022'
plt.savefig(picture_name, dpi=1000)
plt.show()