import easylogger as el

def main():
    el.initialize_Pydantic(serv_name="Easylogger")
    while(1):
        print("로그 내용을 입력해주세요")
        context = input()
        el.send_logs(ctx=context)

if __name__ == "__main__":
    main()
    
