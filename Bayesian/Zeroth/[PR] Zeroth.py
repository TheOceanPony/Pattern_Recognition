import asyncio
import websockets

SESSION_ID = "Coo1Hazcker2004"


async def zeroth():
    url = "wss://sprs.herokuapp.com/zeroth/" + SESSION_ID
    async with websockets.connect(url) as websocket:

        # Establishing connection
        print(">Establishing connection...")
        await websocket.send("Let's start")
        print(">Done! Collecting data...")

        # Receiving & parsing
        response = await websocket.recv()
        print(f">Collected : {response}")
        data = response.split(" ")
        num1 = int(data[1])
        num2 = int(data[3])
        operator = data[2]

        # Computing & Sending
        if operator == "+":
            answer = str(num1 + num2)
        if operator == "-":
            answer = str(num1 - num2)
        if operator == "*":
            answer = str(num1 * num2)

        # Confirming results
        print(">Done! Verifying...")
        await websocket.send(answer)
        response = await websocket.recv()
        print(f">{response}")
        input("Press Enter to end...")


asyncio.get_event_loop().run_until_complete(zeroth())
