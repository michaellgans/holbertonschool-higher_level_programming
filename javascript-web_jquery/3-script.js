/* Wait for document to load */
$(document).ready(function () {
  const newHeader = $('header');
  /* Does header have content? */
  if (newHeader.length === 0) {
    console.error('There is no header element');
  } else {
    newHeader.on('click', function () {
      /* Creates a new class named "red" */
      newHeader.addClass('red');
    });
  }
});
