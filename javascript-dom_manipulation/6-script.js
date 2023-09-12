const character = document.querySelector("#character")

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
	.then(response => {
		return response.json()
	})
	.then(data => {
		character.innerText = data.name;
	})
	.catch(error => {
		console.error("There is an error:", error);
	});
