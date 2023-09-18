$(() => {
	const baseUrl = 'https://hellosalut.stefanbohacek.dev/';
	let url = '';

	$('#btn_translate').on('click', () => {
		let value = $('#language_code').val();
		url = baseUrl + '?lang=' + value;
		$.ajax({
			type: 'GET',
			url: url,
			success: (data) => {
				$('#hello').text(data.hello);
			}
		});
	});
});
