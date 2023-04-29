const sentence = document.getElementById('sentence');
const author = document.getElementById('author');
const btn = document.querySelector('.btn');

document.ready = getSentence();
btn.addEventListener('click', function () {
  getSentence();
});

// 从一言api获取语句  并显示出来
async function getSentence() {
  const config = {
    encode: 'json',
    charset: 'utf - 8',
  };

  let res = await fetch('https://v1.hitokoto.cn/', config);
  let data = await res.json();
  sentence.innerHTML = data.hitokoto;
  if (data.from_who != null) {
    author.innerHTML = `—— ${data.from_who}`;
  } else {
    author.innerHTML = `—— ${data.from}`;
  }


  // let res = fetch('https://v1.hitokoto.cn/', config);
  // res
  //   .then((response) => response.json())
  //   .then((data) => {
  //     sentence.innerHTML = data.hitokoto;
  //     if (data.from_who != null) {
  //       author.innerHTML = `—— ${data.from_who}`;
  //     } else {
  //       author.innerHTML = `—— ${data.from}`;
  //     }
  //   });
};
