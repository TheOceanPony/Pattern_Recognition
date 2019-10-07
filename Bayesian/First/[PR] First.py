import asyncio
import websockets
import utility as u

SessionID = "Coo1Hazcker1103"

hScale = 20
vScale =20
noise = 0.4
totalSteps = 15
shuffle = "on"  #"on" / "off"

async def First():
    url = "wss://sprs.herokuapp.com/first/" + SessionID
    async with websockets.connect(url) as websocket:

        #Establishing connection & receiving initiall details
        await websocket.send("Let's start") 
        response = await websocket.recv()
        print(f"\n>Request: Let's start \n<Response: {response}")

        temp = response.split(" ") 
        bWidth = int(temp[0])     #basic width
        bHeight = int(temp[1])    #basic height
        numAmount = int(temp[2])  #dictionary size

        width = bWidth * hScale
        height = bHeight * vScale


        
        #Sending settings & receiving perfect numbers
        temp = str(hScale)+" "+str(vScale)+" "+str(noise)+" "+str(totalSteps)+" "+shuffle

        await websocket.send(temp)
        response = await websocket.recv()
        print(f"\n>Request: {temp} \n<Response: collected")

        #Parsing it to the dictionary
        dictionary = u.dictionary(u.parseEven(response), numAmount, width*height)

        

        #Ready
        for step in range(0, totalSteps):
            await websocket.send("Ready")
            response = await websocket.recv()
            print("Ready")

            x = u.parseEven(response,1)

            probs = []
            for k in range(0,numAmount):
                a = u.compare(x, dictionary[k], noise)
                probs.append(a)

            answer = u.maxInd(probs)
            #print(f"<{u.maxInd(probs)}> \n {probs}")

            await websocket.send(f"{step + 1} {answer}")
            response = await websocket.recv()
            print(f"{step + 1} {answer}")

        await websocket.send("Bye")
        response = await websocket.recv()
        print(f"\n>Request: Bye \n<Response: {response}")


        input("Press Enter to end...")

asyncio.get_event_loop().run_until_complete(First())
