/* Wait for document to load */
$(document).ready(function () {
  const addHeader = $('#update_header');

  addHeader.click(function () {
    /* Creates a new list element */
    const myHeader = $('header');

    myHeader.text('New Header!!');
  });
});
