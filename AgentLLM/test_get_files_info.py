from functions.get_files_info import get_files_info

def test():
    print("start")
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))
    print(get_files_info("calculator", "main.py"))
    print("end")

if __name__ == "__main__":
    test()
