# P5R

### 女神异闻录5皇家版小工具

![image](https://github.com/zh1u18/p5r/assets/100653846/f6780136-f240-4c73-8159-0c215341f8a6)

## Usage

### main.ipynb 中包含
- 查询反向合成表
- 查询技能
- 查询任意种族，等级面具
- 指定等级范围查询一步能合成的面具
- 查询成本最低合成路径⭐⭐⭐

```
# 查询成本最低合成路径

start = '阿努比斯'  # 设置合成起点
end = '大僧正'      # 设置合成终点
head_num = 10       # 设置显示个数（按合成成本升序）
max_depth = 3       # 设置搜索最大深度

routes = search_route(start, end, max_depth=max_depth)
for idx, route in enumerate(routes):
    if idx < head_num:
        print(route[0], '=', route[1])
    else:
        break

[output]:

阿努比斯 + 杰克灯笼 -> 鬼 + 鞍马天狗 -> 大僧正 = 34539.0
阿努比斯 + 猫妖精 -> 鬼 + 鞍马天狗 -> 大僧正 = 34854.0
阿努比斯 + 亚森 -> 闪电鸟 + 猫妖 -> 大僧正 = 35226.0
阿努比斯 + 奇魂 -> 安德拉斯 + 睡魔 -> 大僧正 = 35250.0
阿努比斯 + 杰克霜精 -> 罗刹 + 毕舍遮 -> 大僧正 = 36003.0
阿努比斯 + 背负怪 -> 闪电鸟 + 猫妖 -> 大僧正 = 36087.0
阿努比斯 + 埃力格 -> 伊西丝 + 水鬼 -> 大僧正 = 36372.0
阿努比斯 + 亚森 -> 闪电鸟 + 欧特鲁斯 -> 大僧正 = 36762.0
阿努比斯 + 皮克希 -> 欧特鲁斯 + 闪电鸟 -> 大僧正 = 36831.0
阿努比斯 + 埃力格 -> 伊西丝 + 金鬼 -> 大僧正 = 36855.0
```
<br/>
另附上二体处刑合成表及宝魔升降级表：
<br/><br/>
<img width="841" alt="二体处刑" src="https://github.com/zh1u18/p5r/assets/100653846/0ad46c89-ba5a-4c59-8ba8-d67ebd52dfff">
<br/><br/>
<img width="841" alt="宝魔升降" src="https://github.com/zh1u18/p5r/assets/100653846/ee0010a5-895d-44b3-b9be-fab793858f0f">
<br/><br/>

数据来源：女神转生Wiki https://wiki.biligame.com/persona/%E4%BA%BA%E6%A0%BC%E9%9D%A2%E5%85%B7
