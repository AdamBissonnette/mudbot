import asyncio, telnetlib3

@asyncio.coroutine
def shell(reader, writer):
    while True:
        outp = yield from reader.read(1024)
        # if not outp:
        #     # EOF
        #     return

        print(outp, flush=True)
        if 'enter name' in outp:
            # reply all questions with 'y'.
            writer.write('Derp\n')
        if 'password' in outp:
            # reply all questions with 'y'.
            writer.write('meowmeow\n')

    print()

loop = asyncio.get_event_loop()
coro = telnetlib3.open_connection('mud.landsofstone.org', 4801, shell=shell)
reader, writer = loop.run_until_complete(coro)
loop.run_until_complete(writer.protocol.waiter_closed)

# def output(text):
#     sys.stdout.write(text.decode('utf-8') + "\n\n\n _____ \n\n\n")

# PROMPT = b'?['
# tn = telnetlib.Telnet('mud.landsofstone.org', 4801, 25)
# output(tn.read_until(PROMPT, 2))
# tn.write(b'Derp\n')
# output(tn.read_until(PROMPT, 2))
# tn.write(b'meowmeow\n')
# output(tn.read_until(PROMPT, 2))
# tn.write(b'think\n')
# output (tn.read_until(PROMPT, 2))
# tn.write(b'quit\n')
# output(tn.read_until(PROMPT, 2))
