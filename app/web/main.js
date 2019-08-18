function send_filejs() {
	//var data = document.getElementById("data").value
	var data = $("#data").val();
	eel.send_file(data)(setImage)
}

function receive_filejs() {
	var data = document.getElementById("data2").value
	eel.receive_file(data)(setImage)
}

function setImage(base64) {
	document.getElementById("qr").src = base64
}
