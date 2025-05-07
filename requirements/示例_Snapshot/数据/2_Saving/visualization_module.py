import matplotlib.pyplot as plt
import csv
def line_chart(filename,ticks,the_label='',the_linestyle='-',the_marker=''):#line chart with ticks
	with open (filename,'r') as fo1:
		rd1=csv.reader(fo1)
		hd1=next(rd1)#Skip the title line
		tick_locations1=[]#The tag list
		x1=[]
		y1=[]
		for row in rd1:
			if str(row[0]) in ticks:
				tick_locations1.append(int(row[0]))#If the year equals the year of the tag, it is added to the tag list
			try:
				y1.append(float(row[1]))
				x1.append(int(row[0]))
			except ValueError:
				pass
	plt.plot(x1,y1,linewidth=2.0,label=the_label,linestyle=the_linestyle,marker=the_marker)
	plt.xticks(tick_locations1,ticks,fontproperties='KaiTi')#The x axis labels
	plt.legend(edgecolor='w')#The legend with the border removed
	plt.xlim(x1[0],x1[-1])
	
def line_withouttick(filename,the_label='',the_linestyle='-',the_marker=''):#line chart without ticks
	with open (filename,'r') as fo1:
		rd1=csv.reader(fo1)
		hd1=next(rd1)#Skip the title line
		tick_locations1=[]#The tag list
		x1=[]
		y1=[]
		for row in rd1:
			try:
				y1.append(float(row[1]))
				x1.append(int(row[0]))
			except ValueError:
				pass
	plt.plot(x1,y1,linewidth=2.0,label=the_label,linestyle=the_linestyle,marker=the_marker)
	plt.legend(edgecolor='w')#The legend with the border removed


def information(the_title,x_label,y_label):#title/labels
	plt.xlabel(x_label,size=7,x=1)
	plt.ylabel(y_label,size=7,y=1.05,rotation=0)
	ax = plt.gca()
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')#Remove the right and top borders
	plt.title(the_title,size=13)

def read_data(filename, ticks):
    """读取CSV文件，提取x和y数据，并生成x轴刻度位置"""
    
    with open(filename, 'r') as fo1:
        rd1 = csv.reader(fo1)
        hd1 = next(rd1)  # 跳过标题行
        tick_locations1 = []  # 标签列表
        x1 = []
        y1 = []
        for row in rd1:
            if str(row[0]) in ticks:
                tick_locations1.append(int(row[0]))  # 如果年份等于标签年份，则添加到标签列表
            try:
                y1.append(float(row[1]))
                x1.append(int(row[0]))
            except ValueError:
                pass
    return x1, y1, tick_locations1