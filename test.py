import asyncio

HOST = "127.0.0.1"  # Change to the server's IP if not running locally
PORT = 3000
BUFFER_SIZE = 1024

async def send_message(reader, writer, message):
    """Send a message to the server and await the echo response."""
    writer.write(message.encode())
    await writer.drain()
    print(f"Sent: {message}")

    data = await reader.read(BUFFER_SIZE)
    print(f"Received: {data.decode('utf-8', errors='ignore').strip()}")

    writer.close()
    await writer.wait_closed()


async def run_client():
    """Run the client connection and interaction with the server."""
    try:
        reader, writer = await asyncio.open_connection(HOST, PORT)
        print(f"Connected to server at {HOST}:{PORT}")

        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                print("Exiting client...")
                break

            await send_message(reader, writer, message)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Client disconnected.")

if __name__ == "_main_":
    asyncio.run(run_client())