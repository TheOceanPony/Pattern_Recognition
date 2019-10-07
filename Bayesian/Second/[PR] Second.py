import asyncio
import websockets
import Ipy as I

SessionID = "Coo1Hazcker3011"

width = 100 	# int[2, 1000]
loss = "L1"	# L1 or int[0, width)
totalSteps = 10	# int[1, 1 000 000]
repeats = 3	# int[1, 1000]

async def Second():
	url = "wss://sprs.herokuapp.com/second/" + SessionID
	async with websockets.connect(url) as websocket:

		#Connecting
		request = (f"Let's start with {width} {loss} {totalSteps} {repeats}" )
		await websocket.send(request)
		response = await websocket.recv()
		print(f"\n>Request: {request} \n<Response: {response}")

		#Main cycle
		for step in range(1, totalSteps + 1):

			request = ("Ready")
			await websocket.send(request)
			response = await websocket.recv()
			print(f"\n>Request: {request} \n<Response: {response}")

			heatmap = I.Normalise(I.Parse(response))

			if(loss == "L1"):
				answer = str(I.predictL1(heatmap))
			else:
				answer = str(I.predictDelta(heatmap, int(loss)))

			a = answer + " "


			request = (f"{step}\n{a*(repeats-1)}{answer}" )
			await websocket.send(request)
			response = await websocket.recv()
			print(f"\n{request} \n-={response}")

			#input("--==Press any key==--")
		request = ("Bye")
		await websocket.send(request)
		response = await websocket.recv()
		print(f"\n{request} \n-={response}")



		input("--==Press any key==--")

asyncio.get_event_loop().run_until_complete(Second())
