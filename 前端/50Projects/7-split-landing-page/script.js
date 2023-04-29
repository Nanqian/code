const splits = document.querySelectorAll('.split');

for (let i = 0; i < splits.length; i++) {
  splits[i].addEventListener('mouseenter', function () {
    this.style.flex = '3';
  });
  splits[i].addEventListener('mouseleave', function () {
    this.style.flex = '1';
  });
}
