import EasyLogFire as el

def main():
    el.initialize_Pydantic(serv_name="EasyLogFire")
    while(1):
        print("Please Type Log Context")
        context = input()
        el.send_logs(ctx=context)

if __name__ == "__main__":
    main()