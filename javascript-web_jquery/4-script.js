/* Wait for document to load */
$(document).ready(function () {
  const headerElement = $('header');
  /* Does header have content? */
  if (headerElement.length === 0) {
    console.error('There is no header element');
  } else {
    headerElement.on('click', function () {
      /* Creates a new class named "red" */
      headerElement.toggleClass('green');
      headerElement.toggleClass('red');
    });
  }
});
