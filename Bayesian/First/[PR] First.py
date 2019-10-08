import asyncio
import websockets
import FirstModule as u

SessionID = "Coo1Hazcker2045"

hScale = 20
vScale = 20
noise = 0.4
totalSteps = 100
shuffle = "on"  # "on" / "off"


async def first():
    url = "wss://sprs.herokuapp.com/first/" + SessionID
    async with websockets.connect(url) as websocket:

        # Establishing connection & receiving initial details
        await websocket.send("Let's start") 
        response = await websocket.recv()
        print(f"\n>Request: Let's start \n<Response: {response}")

        temp = response.split(" ") 
        bWidth = int(temp[0])     # basic width
        bHeight = int(temp[1])    # basic height
        numAmount = int(temp[2])  # dictionary size

        width = bWidth * hScale
        height = bHeight * vScale


        # Sending settings & receiving perfect numbers
        request = f"{hScale} {vScale} {noise} {totalSteps} {shuffle}"
        await websocket.send(request)
        response = await websocket.recv()
        print(f"\n>Request: {request} \n<Response: collected")

        # Parsing them to dictionary
        dictionary = u.glossary(u.parse_even(response), numAmount, width*height)

        # Ready
        for step in range(0, totalSteps):
            await websocket.send("Ready")
            response = await websocket.recv()
            print("Ready")

            if step >= 99:
                x = u.parse_even(response, 3)
            elif (step >= 9) and (step < 99):
                x = u.parse_odd(response, 2)
            else:
                x = u.parse_even(response, 1)

            probs = []
            for k in range(0, numAmount):
                a = u.compare(x, dictionary[k], noise)
                probs.append(a)

            answer = u.max_index((probs))       # FIXME
            # print(f"<{u.maxInd(probs)}> \n {probs}")

            await websocket.send(f"{step + 1} {answer}")
            response = await websocket.recv()
            print(f"{step + 1} {answer}")

        await websocket.send("Bye")
        response = await websocket.recv()
        print(f"\n>Request: Bye \n<Response: {response}")

        input("Press Enter to end...")

asyncio.get_event_loop().run_until_complete(first())
