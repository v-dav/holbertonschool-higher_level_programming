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

	$('#language_code').on('keypress', (event) => {
		if (event.which === 13) {
			let value = $('#language_code').val();
			url = baseUrl + '?lang=' + value;
			$.ajax({
				type: 'GET',
				url: url,
				success: (data) => {
					$('#hello').text(data.hello);
				}
			});
		};
	});
});
