$(() => {
	const newElement = '<li>Item</li>';
	$('#add_item').on('click', () => {
		$('.my_list').append(newElement);
	});

	$('#remove_item').on('click', () => {
		$('.my_list').children().last().remove();
	});

	$('#clear_list').on('click', () => {
		$('.my_list').empty();
	});
})
