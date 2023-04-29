[toc]



### 创建

#### document.write

#### innerHTML

#### createElement

### 增

#### appendChild

#### insertBefore

### 删

#### removeChild

### 改

#### 修改元素属性

src, href, title 等

#### 修改普通元素的内容

innerHTML, innerText

#### 修改表单元素

value, type, disabled等

#### 修改元素样式

style, className, classList

### 查

#### DOM提供的API方法(不推荐)

getElementById、getElementByTagName、

#### H5提供的方法

querySelector、querySelectorAll

#### 利用节点操作获取元素

父（parentNode）、子（childern、firstElementChild）、兄（previousElementSibiling、nextElementSibiling）

### 属性操作

主要针对自定义属性

1. setAttribute：设置dom的属性值
2. getAttribute：得到dom的属性值
3. removeAttribute：移除属性

### 事件操作

给元素注册事件，采取 事件源.事件类型 = 事件处理程序

| 鼠标事件    | 触发条件     |
| ----------- | ------------ |
| onclick     | 鼠标点击左键 |
| onmouseover | 鼠标经过     |
| onmouseout  | 鼠标离开     |
| onfocus     | 获得鼠标焦点 |
| onblur      | 失去鼠标焦点 |
| onmousemove | 鼠标移动     |
| onmouseup   | 鼠标弹起     |
| onmousedown | 鼠标按下     |

