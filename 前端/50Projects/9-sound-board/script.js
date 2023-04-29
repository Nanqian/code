window.onload = () => {
  const soundList = document.querySelectorAll('audio');
  soundList.forEach((sound) => {
    let btn = document.createElement('button');
    btn.innerHTML = sound.innerHTML;
    btn.addEventListener('click', () => {
      soundList.forEach(function (sound) {
        sound.pause();
        sound.currentTime = 0;
      });
      sound.play();
    });
    document.body.append(btn);
  });
};
