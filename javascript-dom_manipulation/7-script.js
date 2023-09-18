const ul = document.querySelector("#list_movies")

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
	.then(response => {
		return response.json()
	})
	.then(data => {
		for (let i = 0; i < data.results.length; i++) {
			const li = document.createElement("li");
			ul.append(li);
			li.innerText = data.results[i].title;
		}
	})
