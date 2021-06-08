# try:
#     data = "10"
#     data = int(data)
#     data = data/ 0

#     print(data)
# except ValueError:
#     print("error casting to integer")
# except ZeroDivisionError:
#     print('error division by 0')
# except:
#     print("error is happening")
# finally:
#     print("using exception")


def count(num:str):
    try:
        data = num
        data = int(data)
        data = data/ 0

        print(data)
    except ValueError:
        print("error casting to integer")
    except ZeroDivisionError:
        print('error division by 0')
    except:
        print("error is happening")
    finally:
        print("using exception")

count("0")