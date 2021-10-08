import os
import requests

def set_url():
    print("Welcome to IsItDown.py!")
    print("Please write a URLs you wnat to check. (separated by comma)")
    x = input('').lower().split(',') #url 통으로 받고 split으로 구분 후 리스트화
    
    #print(x[1].strip())
    for i in x:
        if('http' in i):
            r = requests.get(i)
            # if(r.status_code == 200):
            #     print(i + " is up!")
            # # elif(r.status_code == 404):
            # #     print(i + " is down!")
            # else:
            #     print(i + " is down!")
            try:
                print(i + " is up!")
            except HTTPError as e:
                print(i + " is down!")

        else: #http 빠진 것 채워넣기
            my_string = i
            split_str = my_string.split()
            split_str.insert(0,'https://')
            final_str = ''.join(split_str)
            r2 = requests.get(final_str)

            # print(r2.raise_for_status())
            if(r2.status_code == 200):
                print(final_str + " is up!")
            elif(r2.raise_for_status() == None):
                print(final_str + " is down!")

    num = input("Do you want to start over? y/n ")
    if(num == 'y'):
        set_url()
    else:
        print("k. bye!")


set_url()


# import os
# import requests

# def restart():
#   answer = str(input("Do you want to start over? y/n ")).lower()
#   if answer == "y" or answer =="n":
#     if answer == "n":
#         print("k. bye!")
#         return
#     elif answer == "y":
#       main()
#   else:
#     print("That's not a valid answer")
#     restart()


# def main():
#   os.system('clear')
#   print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
#   urls = str(input()).lower().split(",")
#   for url in urls:
#     url = url.strip()
#     if "." not in url:
#       print(url, "is not a valid URL.")
#     else:
#       if "http" not in url:
#         url = f"http://{url}"
#       try:
#         request = requests.get(url)
#         if request.status_code == 200:
#           print(url,"is up!")
#         else:
#           print(url, "is down!")
#       except:
#           print(url, "is down!")
#   restart()

