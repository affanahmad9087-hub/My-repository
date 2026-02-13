const shadow = document.querySelector('.cursor-shadow');

document.addEventListener('mousemove', (e) => {
  // Get the X and Y coordinates of the mouse
  const x = e.clientX;
  const y = e.clientY;

  // Move the shadow to those coordinates
  shadow.style.left = x + 'px';
  shadow.style.top = y + 'px';
});