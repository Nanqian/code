window.onload = () => {
  const steps = document.querySelectorAll('.step');
  const prev = document.getElementById('prev');
  const next = document.getElementById('next');
  const progress = document.querySelector('.progress');
  let flag = 1;
  prev.disabled = true;
  mark();

  prev.onclick = () => {
    flag--;
    mark();
    isDisabled();
  };
  next.onclick = () => {
    flag++;
    mark();
    isDisabled();
  };

  function isDisabled() {
    if (flag === 1) {
      prev.disabled = true;
    } else if (flag === 4) {
      next.disabled = true;
    } else {
      prev.disabled = false;
      next.disabled = false;
    }
  }
  function mark() {
    for (let i = 0; i < steps.length; i++) {
      steps[i].classList.remove('active');
    }
    for (let i = 0; i < flag; i++) {
      steps[i].classList.add('active');
    }
    //进度条 —— 我的方案
    // progress.style.width = `${steps[flag - 1].offsetLeft}px`;

    //进度条 —— github方案
    const actives = document.querySelectorAll('.active');
    progress.style.width =
      ((actives.length - 1) / (steps.length - 1)) * 100 + '%';
  }
};
