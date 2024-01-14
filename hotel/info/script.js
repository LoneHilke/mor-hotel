//modalshow
let current = 1;
(playPauseBool = true), (interval = null);

const changemodals = () => {
  const modalList = document.querySelectorAll(".modal img");

  const modal = Array.from(modalList);

  if (current > modal.length) {
    current = 1;
  } else if (current === 0) {
    current = modal.length;
  }

  console.log(current);

  modals.forEach((modal) => {
    if (modal.classList[0].split("-")[1] * 1 === current) {
      modal.style.cssText = "visibility: visible; opacity: 1";
    } else {
      modal.style.cssText = "visibility: hidden; opacity: 0";
    }
  });

  const controls = document.querySelectorAll(".controls a");

  controls.forEach((control) => {
    if (control.classList[0].split("-")[1] * 1 === current) {
      control.style.cssText = "background-color: #aaa";
    } else {
      control.style.cssText = "background-color: #444";
    }
  });
};
