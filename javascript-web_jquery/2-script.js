/* Wait for document to load */
$(document).ready(function () {
  const redHeader = $('#red_header');
  /* Does redHeader have content? */
  if (redHeader.length === 0) {
    console.error('There is no redHeader element.');
  } else {
    redHeader.on('click', function () {
      redHeader.css('color', ('#FF0000'));
    });
  }
});
