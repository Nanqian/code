window.onload = function () {
  // 地区导航栏精灵图
  let nav_local_icon = document.querySelectorAll('.nav-local-icon');
  for (let i = 0; i < nav_local_icon.length; i++) {
    nav_local_icon[i].style.backgroundPositionY = `${-i * 32}px`;
  }
};
