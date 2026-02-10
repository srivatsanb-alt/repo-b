from libs.submodule.service import fetch_data, process_data

def run():
    d = fetch_data()
    print(process_data(d))

if __name__ == "__main__":
    run()
