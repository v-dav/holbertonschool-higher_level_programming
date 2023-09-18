$.ajax({
	type: "GET",
	url: "https://swapi-api.hbtn.io/api/films/?format=json",
	success: function (data) {
		$.each(data.results, function (i, result) {
			$("#list_movies").append('<li>'+ result.title + '</li>')
		});
	}
});
