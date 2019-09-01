function send_filejs() {
	eel.id_name()(set_id)
	var file = document.getElementById("data").value
	eel.send_file(file)(setImage)
}

function receive_filejs() {
	var data = document.getElementById("data2").value
	var file = document.getElementById("name_file").value
	eel.receive_file(data,file)(setImage)
}

function setImage(base64) {
	document.getElementById("qr").src = base64
}

function set_id(name) {
        document.getElementById("id_client").innerHTML = "id : " + name;
}
