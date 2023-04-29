[toc]

# 属性书写顺序

### 布局定位属性

```
display/ podition/ float/ clear/ visibility/ overflow
```

### 自身属性

```
width/ height/ margin/ padding/ border/ background
```

### 文本属性

```
color/ font/ text-decoration/ text-align/ vertical-align/ white-space/ break-word
```

### 其他属性

```
content/ cursor/ border-radius/ box-shadow/ text-shadow/ background:linear-gradient...
```



# display&visibility

## display

​    `display` 属性规定是否/如何显示元素。

​    每个 HTML 元素都有一个默认的 display 值，具体取决于它的元素类型。

> 行内元素的一些例子：
>
> - *<span>*
> - *<a>*
> - *<img>*
> - *<input>*
> - *<button>*


> 块级元素的一些例子：
>
> - *<div>*
> - *<h1> - <h6>*
> - *<ul>, <li>*
> - *<p>*
> - *<form>*
> - *<table>*
> - *<header>*
> - *<footer>*
> - *<section>*

### display:none

​    **元素不显示**，类似于删除的效果，不占据空间

### display:inline

​    **行内元素（inline element）**

1. 多个元素占一行

2. 不可以设置宽高

   tips：尽管img是行内元素，但同时它也是**置换元素**，置换元素一般内置框高属性，因此可以设置其框高。

### display:block

​    **块级元素（block element）**

1. 自己占一行
2. 可以设置宽高

### display:inline-block

​    **行内块元素**

1. 多个元素占一行
2. 可以设置宽高



## visibility

​    指定元素是否应该可见

### visibility:visible

​    **元素可见**

### visibility:hidden

​    **元素隐藏**，但还占据空间



# CSS定位

## position

### position:static

​    **默认属性**，此时 top, right, bottom, left 和 z-index 属性无效。

### position:relative

​    **相对定位**，元素相对于其正常位置进行定位，位置偏移后实际空间还保留在原位，其他元素不会占用。

### position:absolute

​    **绝对定位**，会将元素移出正常的文档流，其他元素可以占据它原本的位置，而它可以覆盖在别的元素上方。绝对定位元素相对于*最近的非 `static` 父元素*定位（父元素设定了position，transform或perspective）。以父元素的padding为边界计算偏移。

### position:fixed

​    **固定定位**，与绝对定位相似，但包含元素为当前浏览器窗口。

### position:sticky

​    **粘性定位**，粘性元素根据滚动位置在相对（`relative`）和固定（`fixed`）之间切换。起先它会被相对定位，直到在窗口中到达给定的位置 - 然后将其固定在那个位置。

### tips：

1. 当只设置`position:absolute`,不设置 left，right，top，bottom时，元素的位置，还是在原来的位置。

2. absolute和fixed这种脱离正常文档流的定位方式会把元素的宽高设置成内容的宽高，即用`letft:0;和right:0;`可以使元素的宽充满父元素，高同理。
3. 对于absolute和fixed定位的固定尺寸（设置了width和height属性值）元素，如果设置了top和left属性，那么设置bottom和right值就没有作用了，应该是top和left优先级高，否则同时写了浏览器怎么知道按照谁定位。
4. 对于absolute和fixed定位的元素，如果设置了top、left、bottom、right的值后对应的margin属性以及后float属性都会失效
5. 块元素如果设置了float属性或者是absolute、fixed定位，那么vertical-align属性不再起作用。













#### 常用命名推荐

| ClassName              | 含义                                     |
| ---------------------- | ---------------------------------------- |
| about                  | 关于                                     |
| account                | 账户                                     |
| arrow                  | 箭头图标                                 |
| article                | 文章                                     |
| aside                  | 边栏                                     |
| audio                  | 音频                                     |
| avatar                 | 头像                                     |
| bg,background          | 背景                                     |
| bar                    | 栏（工具类）                             |
| branding               | 品牌化                                   |
| crumb,breadcrumbs      | 面包屑                                   |
| btn,button             | 按钮                                     |
| caption                | 标题，说明                               |
| category               | 分类                                     |
| chart                  | 图表                                     |
| clearfix               | 清除浮动                                 |
| close                  | 关闭                                     |
| col,column             | 列                                       |
| comment                | 评论                                     |
| community              | 社区                                     |
| container              | 容器                                     |
| content                | 内容                                     |
| copyright              | 版权                                     |
| current                | 当前态，选中态                           |
| default                | 默认                                     |
| description            | 描述                                     |
| details                | 细节                                     |
| disabled               | 不可用                                   |
| entry                  | 文章，博文                               |
| error                  | 错误                                     |
| even                   | 偶数，常用于多行列表或表格中             |
| fail                   | 失败（提示）                             |
| feature                | 专题                                     |
| fewer                  | 收起                                     |
| field                  | 用于表单的输入区域                       |
| figure                 | 图                                       |
| filter                 | 筛选                                     |
| first                  | 第一个，常用于列表中                     |
| footer                 | 页脚                                     |
| forum                  | 论坛                                     |
| gallery                | 画廊                                     |
| group                  | 模块，清除浮动                           |
| header                 | 页头                                     |
| help                   | 帮助                                     |
| hide                   | 隐藏                                     |
| hightlight             | 高亮                                     |
| home                   | 主页                                     |
| icon                   | 图标                                     |
| info,information       | 信息                                     |
| last                   | 最后一个，常用于列表中                   |
| links                  | 链接                                     |
| login                  | 登录                                     |
| logout                 | 退出                                     |
| logo                   | 标志                                     |
| main                   | 主体                                     |
| menu                   | 菜单                                     |
| meta                   | 作者、更新时间等信息栏，一般位于标题之下 |
| module                 | 模块                                     |
| more                   | 更多（展开）                             |
| msg,message            | 消息                                     |
| nav,navigation         | 导航                                     |
| next                   | 下一页                                   |
| nub                    | 小块                                     |
| odd                    | 奇数，常用于多行列表或表格中             |
| off                    | 鼠标离开                                 |
| on                     | 鼠标移过                                 |
| output                 | 输出                                     |
| pagination             | 分页                                     |
| pop,popup              | 弹窗                                     |
| preview                | 预览                                     |
| previous               | 上一页                                   |
| primary                | 主要                                     |
| progress               | 进度条                                   |
| promotion              | 促销                                     |
| rcommd,recommendations | 推荐                                     |
| reg,register           | 注册                                     |
| save                   | 保存                                     |
| search                 | 搜索                                     |
| secondary              | 次要                                     |
| section                | 区块                                     |
| selected               | 已选                                     |
| share                  | 分享                                     |
| show                   | 显示                                     |
| sidebar                | 边栏，侧栏                               |
| slide                  | 幻灯片，图片切换                         |
| sort                   | 排序                                     |
| sub                    | 次级的，子级的                           |
| submit                 | 提交                                     |
| subscribe              | 订阅                                     |
| subtitle               | 副标题                                   |
| success                | 成功（提示）                             |
| summary                | 摘要                                     |
| tab                    | 标签页                                   |
| table                  | 表格                                     |
| txt,text               | 文本                                     |
| thumbnail              | 缩略图                                   |
| time                   | 时间                                     |
| tips                   | 提示                                     |
| title                  | 标题                                     |
| video                  | 视频                                     |
| wrap                   | 容器，包，一般用于最外层                 |
| wrapper                | 容器，包，一般用于最外层                 |