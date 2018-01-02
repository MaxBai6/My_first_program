### My_first_program

>闲暇时间希望把一些有趣的设计写上来

联系方式：
familybjp@gmail.com



#### 安装

```
pip install git+https://github.com/MaxBai6/My_first_program.git
```
#### 安装要求
```
numpy>=1.9.2
```
#### 更新

还没弄更新，可以在C:\python\Lib\site-packages\中找到这个包，删除，然后按照安装步骤重新下最新版本。（估计暂时没人会下我的包第二次:(）

#### 使用简介

```
import My_first_program
x=My_first_program.add_two(2)

result：x=4
```
```
import My_first_program.api as mfpa
b=mfpa.add_one(2)
```


#### 现有功能

- add_two(x)

  返回x+2
- r2_table(x1,x2,table1,table2,month_name,data_name1,data_name2)

  用于分析滞后时间数据与另一数据（价格）的线性相关性。例如：可以用来测量滞后的GDP数据和股市的相关性。
  返回corr和R方与滞后时间的关系表。
  
  ![image](https://github.com/MaxBai6/My_first_program/blob/master/%E5%9B%BE.PNG）
  
