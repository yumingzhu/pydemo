from retrying import retry

def todo():
    date=["a=b","c=d"]
    resut =dict(item.split("=") for item in date)
    print(resut)




if __name__ == '__main__':
    todo()

