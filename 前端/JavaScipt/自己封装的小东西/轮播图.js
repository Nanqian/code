window.onload = function () {
  let focusBox = document.querySelector('.focus');
  let arrow_l = focusBox.querySelector('.arrow-l');
  let arrow_r = focusBox.querySelector('.arrow-r');
  let list = focusBox.querySelector('ul');
  let circle = focusBox.querySelector('ol');
  let focusWidth = list.children[0].offsetWidth;
  //鼠标移入显示箭头和小圆圈
  focusBox.addEventListener('mouseenter', function () {
    arrow_l.style.display = 'block';
    arrow_r.style.display = 'block';
    clearInterval(autoChange);
    autoChange = null;
  });
  //鼠标移出隐藏箭头和小圆圈
  focusBox.addEventListener('mouseleave', function () {
    arrow_l.style.display = 'none';
    arrow_r.style.display = 'none';
    autoChange = setInterval(function () {
      arrow_r.click();
    }, 3000);
  });

  //动态创建小圆圈数量
  for (let i = 0; i < list.children.length; i++) {
    let dot = document.createElement('li');
    circle.appendChild(dot);
  }
  //点击小圆圈跳转相应的图片
  for (let i = 0; i < circle.children.length; i++) {
    circle.children[i].onclick = function () {
      animate(list, -focusWidth * i);
      for (let i = 0; i < circle.children.length; i++) {
        circle.children[i].classList.remove('current');
      }
      this.classList.add('current');
    };
  }

  //利用动画函数animate()实现图片移动
  let clickTimes = 0;
  circle.children[0].classList.add('current');
  //无缝衔接轮播
  let firstClone = list.children[0].cloneNode(true);
  list.appendChild(firstClone);
  //点击右箭头,滚动下一张图
  arrow_r.addEventListener('click', function () {
    change('right');
  });
  //点击左箭头,滚动上一张图
  arrow_l.addEventListener('click', function () {
    change('left');
  });
  //滚动函数（添加节流阀）
  let flag = true;
  function change(arrow) {
    if (flag) {
      flag = false;
      clickTimes = getFocusLeft() / -focusWidth;
      if (arrow == 'right') {
        clickTimes++;
      } else if (arrow == 'left') {
        clickTimes--;
      }
      if (clickTimes == list.children.length) {
        list.style.left = 0;
        clickTimes = 1;
      } else if (clickTimes === -1) {
        list.style.left = -focusWidth * (list.children.length - 1) + 'px';
        clickTimes = list.children.length - 2;
      }
      //当前小圆圈动态变化
      animate(list, -focusWidth * clickTimes, function () {
        flag = true;
      });
      for (let i = 0; i < circle.children.length; i++) {
        circle.children[i].classList.remove('current');
      }
      if (clickTimes == 4) {
        circle.children[0].classList.add('current');
      } else {
        circle.children[clickTimes].classList.add('current');
      }
    }
  }

  //自动播放
  let autoChange = setInterval(function () {
    arrow_r.click();
  }, 3000);

  function getFocusLeft() {
    return list.style.left.replace('px', 0) / 10;
  }
};
