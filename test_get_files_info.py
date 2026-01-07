from functions.get_files_info import get_files_info

def main():
    result = get_files_info("calculator", ".")
    print(result)

if __name__ == "__main__":
    main()