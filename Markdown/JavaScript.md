[toc]

*[MDN](https://developer.mozilla.org/zh-CN/)*

## 数组

### 检测是否为数组

1. **instanceof**  运算符

   `arr instanceof Array` 返回true/false

2. **isArray** 方法

   `Array.isArray(arr)` 返回true/false

### 添加数组元素

1. **push()** 方法 //在数组后面添加新元素
   1. 参数直接写要添加的元素
   2. 返回值为新数组长度
2. **unshift()** 方法 //在数组前面添加新元素
   1. 用法与push()相同

### 删除数组元素

1. **pop()** 方法 //删除数组的最后一个元素	
   1. 没有参数，直接使用
   2. 返回值是删除的那个元素
2. **shift()** 方法 //删除数组的第一个元素
   1. 用法与pop()相同

### 数组排序

1. **reverse()** 方法 //颠倒数组中元素的顺序

2. [**sort()**](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) 方法 //对数组的元素进行排序

   1. 按逐个字符的Unicode 位点进行排序

   2. arr.sort([compareFunction(a, b)])

      ```javascript
      compareFunction(a, b) 
      //小于 0 ，a 排 b 前
      //等于 0 ，a, b相对位置不变
      //大于 0 ，b 排 a 前
      function(a,b){
        return a - b;  //升序排列
        return b - a;  //降序排列
      }
      ```

### 数组索引

1. **indexOf(要查找的元素,[开始查找的位置])** 方法 //从前向后查找
   1. 返回首个被找到的元素的索引号
   2. 如果不存在则返回 -1
2. **lastIndexOf()** 方法 //从后向前查找
   1. 返回首个被找到的元素的索引号
   2. 如果不存在则返回 -1

### 数组转换为字符串

1. **toString()** 方法
2. **join(分隔符)** 方法 //可以自定义分隔符

### 数组连接、截取、删除

1. **concat()** 方法 //连接两个或多个数组，返回连接后的新数组
2. **slice(begin[, end]])** 方法 //返回截取项目的新数组
   1. begin和end是索引号
   2. 返回的数组包括begin不包括end

3. **splice(始索引,数量)** 方法 //删除原数组某一片段，返回被删除的片段组成的新数组，这个方法会改变原数组

## 字符串对象

### 根据位置返回字符

1. **charAt(index)** 方法 
2. **charCodeAt(index)** 方法 //返回ASCⅡ值
3. **str[index]**  //H5新增

### 截取字符串

**substring（indexStart[, indexEnd]）**此方法返回一个字符串在开始索引到结束索引之间的一个子集，或从开始索引直到字符串的末尾的一个子集。

### 替换字符

**replace('被替换的字符','替换为的字符')** 方法

### 字符转换为数组

**split('分隔符')** 方法



## 数据类型内存分配

### 简单类型

​		又叫基本数据类型或==值类型==

​	在存储时变量中存储的是值本身，因此叫做值类型

​		sting, number, boolean, undefined, null

​			null特殊：typeof显示的是object 空对象（bug）



​	简单数据类型传参直接传值，如b是a的形参，修改b的值后a不受影响



### 复杂类型

​		又叫==引用类型==

​	在内存变量中存储的仅仅是地址，地址再指向存储的复杂类型（故为引用）

​		通过new关键字创建的对象（系统对象、自定义对象），如Object、Array、Date等



​	引用类型传参传的是地址，而地址指向同一对象，故对形参的修改会直接修改对象
