import requests
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, ttk, Toplevel
import os
import time
from PIL import Image, ImageTk

# 假设网站的激活码获取接口地址
activation_url = "http://localhost/0.htm"

# 添加一个变量来存储获取到的激活码
fetched_activation_code = None

def get_activation_code():
    try:
        response = requests.get(activation_url)
        if response.status_code == 200:
            global fetched_activation_code
            fetched_activation_code = response.text
            return response.text
            print("访问成功...获取完成")
        else:
            print(f"获取激活码失败，状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")

def verify_activation(code):
    # 这里可以进行实际的激活码验证逻辑
    if code == "565327":  # 替换为实际期望的激活码
        # 将激活状态存储到文件
        with open("activation_status.txt", "w") as f:
            f.write("True")
        progress_bar['value'] = 100
        result_label.config(text="激活成功")
        # 运行另一个.py 文件
        os.system("runtime\python.exe open.py pause")
        time.sleep(2)  # 延迟 2 秒后关闭
        root.destroy()  # 添加这行来关闭窗口
    else:
        result_label.config(text="激活失败")

def handle_verify():
    user_code = code_entry.get()
    verify_activation(user_code)

def clear_activation_status():
    if os.path.exists("activation_status.txt"):
        os.remove("activation_status.txt")
        result_label.config(text="激活状态已清除")

def show_payment_window():
    payment_window = Toplevel(root)
    payment_window.title("支付方式")

    # 假设这里有两个付款码图片路径
    qr_code1_path = "qr_code1.jpg"
    qr_code2_path = "qr_code2.jpg"

    # 加载并显示图片
    image1 = Image.open(qr_code1_path)
    photo1 = ImageTk.PhotoImage(image1)
    label1 = tk.Label(payment_window, image=photo1)
    label1.image = photo1

    image2 = Image.open(qr_code2_path)
    photo2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(payment_window, image=photo2)
    label2.image = photo2

    label1.pack()
    label2.pack()

root = tk.Tk()

Label(root, text="请输入激活码:").pack()
code_entry = tk.Entry(root)
code_entry.pack()

verify_button = tk.Button(root, text="验证", command=handle_verify)
verify_button.pack()

clear_status_button = tk.Button(root, text="清除激活状态", command=clear_activation_status)
clear_status_button.pack()

payment_button = tk.Button(root, text="支付", command=show_payment_window)
payment_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()

# 检查激活状态文件
if os.path.exists("activation_status.txt"):
    with open("activation_status.txt", "r") as f:
        status = f.read().strip()
        if status == "True":
            os.system("runtime\python.exe open.py pause")
            root.destroy()  # 修改为 destroy 方法
else:
    activation_code = get_activation_code()

root.mainloop()