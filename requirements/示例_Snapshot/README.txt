示例为A Snapshot of China's Macroeconomy，形式参照Chad Jones的Country Snapshots，但加入了特色指标和故事部分

文档包括有数据的处理部分、书面报告的生成部分
1. 数据部分采用python代码，注明了数据来源
2. visualization_module为定义的代码包，主要包含有以下函数：

line_chart函数：画年份为间隔的数据折线图，有ticks，可自定义：文件名（必备），ticks（必备），label，线条风格，点的标记）
ine_withouttick：画年份为间隔的数据折线图，无ticks，可自定义：文件名（必备），label，线条风格，点的标记
information函数：可自定义：题目，x轴label，y轴label，包含一些调整（label的位置，去掉边框等）
parallel函数：平行辅助线，可自定义：左右起点，平行线高度
monthly_line函数：画年份为间隔的数据折线图，有ticks，可自定义：文件名（必备），ticks（必备），label，线条风格，点的标记）
ine_withouttick：画月份为间隔的数据折线图，有ticks，可自定义：文件名（必备），label，线条风格，点的标记

3. 书面报告采用markdown生成