import asyncio
import websockets
import math
import second_module as sm

SessionID = "Coo1Hazcker3011"

width = 100 	# int[2, 1000]
loss = "51"		# L1 or int[0, width/2 - 1)
totalSteps = 10		# int[1, 1 000 000]
repeats = 1		# int[1, 1000]


async def second():
	url = "wss://sprs.herokuapp.com/second/" + SessionID
	async with websockets.connect(url) as websocket:

		# Connecting
		request = f"Let's start with {width} {loss} {totalSteps} {repeats}"
		await websocket.send(request)
		response = await websocket.recv()
		print(f"\n>Request: {request} \n<Response: {response}")

		# Main cycle
		for step in range(1, totalSteps + 1):

			request = "Ready"
			await websocket.send(request)
			response = await websocket.recv()
			print(f"\n>Request: {request} \n<Response: {response}")

			heatmap = sm.normalise(sm.parse(response))

			if int(loss) >= width/2:
				answer = math.floor(width / 2)
			elif loss == "L1":
				answer = str(sm.predict_L1(heatmap))
			else:
				answer = str(sm.predict_delta(heatmap, int(loss)))

			a = str(answer) + " "

			request = f"{step}\n{a*(repeats-1)}{answer}"
			await websocket.send(request)
			response = await websocket.recv()
			print(f"\n{request} \n-={response}")

		request = "Bye"
		await websocket.send(request)
		response = await websocket.recv()
		print(f"\n{request} \n-={response}")

		input("--==Press any key==--")

asyncio.get_event_loop().run_until_complete(second())
