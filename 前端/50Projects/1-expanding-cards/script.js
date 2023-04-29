window.onload = () => {
  const allBox = document.querySelectorAll('.box');

  for (let i = 0; i < allBox.length; i++) {
    allBox[i].onclick = function () {
      for (let i = 0; i < allBox.length; i++) {
        allBox[i].classList.remove('current');
      }
      this.classList.add('current');
    };
  }
};
