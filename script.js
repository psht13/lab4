function getFact() {
    let number = document.getElementById("number").value;
    if (number !== "") {
        let url = `http://numbersapi.com/${number}/?json`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                let fact = data.text;
                document.getElementById("fact").innerHTML = `<p>${fact}</p>`;
            })
            .catch(error => {
                console.error(error);
                document.getElementById("fact").innerHTML = "<p>Помилка отримання факту</p>";
            });
    }
}