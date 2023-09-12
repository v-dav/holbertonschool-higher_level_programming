const addItem = document.querySelector("#add_item");
const ul = document.querySelector("ul.my_list")

addItem.addEventListener("click", function () {
	const li = document.createElement("li")
	ul.append(li)
	li.innerText = "Item"
})
