const items = document.querySelectorAll('.item span');


const twitter = new Item(items[0], 12000);
const youtube = new Item(items[1], 5000);
const facebook = new Item(items[2]);

twitter.show();
youtube.show();
facebook.show(7777);



function Item(node, fans = 0) {
  this.node = node;
  this.fans = fans;
  this.show = function (fans = this.fans) {
    let timer = setInterval(() => {
      let f = Number(this.node.innerHTML);
      let step = Math.ceil((fans - f) / 10);
      if (f >= fans) {
        clearInterval(timer);
        return;
      }
      f += step;
      this.node.innerHTML = f;
    }, 20)
  }
}





// const twitter = items[0];
// const youtube = items[1];
// const facebook = items[2];

// const fansNum = {
//   twitter: 12000,
//   youtube: 5000,
//   facebook: 7777,
// }

// function show(item, target) {
//   let timer = setInterval(function () {
//     let f = Number(item.innerHTML);
//     let step = Math.ceil((target - f) / 10);
//     if (f >= target) {
//       clearInterval(timer);
//       return;
//     }
//     f += step;
//     item.innerHTML = f;
//   }, 20)
// }

// show(twitter, fansNum.twitter);
// show(youtube, fansNum.youtube);
// show(facebook, fansNum.facebook);