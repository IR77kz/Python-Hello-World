from hellolib import HelloWorld

if __name__ == "__main__":
    try:
        hello_world = HelloWorld()
        response = hello_world.send()

        print(response)
    except Exception as exception:
        print("Hello, World\n<{}>".format(exception))
else:
    print("HeLLo% wOrlD!")
