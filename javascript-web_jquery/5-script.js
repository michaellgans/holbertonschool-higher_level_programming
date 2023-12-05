/* Wait for document to load */
$(document).ready(function () {
  const addListItem = $('#add_item');

  addListItem.click(function () {
    /* Creates a new list element */
    const myList = $('.my_list');
    const newListItem = $('<li>Item</li>');

    myList.append(newListItem);
  });
});
