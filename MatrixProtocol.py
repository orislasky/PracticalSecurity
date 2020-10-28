from matrix_client.client import MatrixClient

def redPill(msgStr):
	client = MatrixClient("https://matrix.org")
	token = client.login(username=" ", password="")
	# token = client.register_with_password(username="foobar", password="monkey")
	room = client.join_room("!:matrix.org") # find it in room's advanced settings
	room.send_text(msgStr)
	client.logout()

message = "You take the red pill - you stay in Wonderland \
and I show you how deep the rabbit-hole goes."
redPill(message)
