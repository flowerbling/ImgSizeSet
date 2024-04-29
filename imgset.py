from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def resize_image():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        input_path = filedialog.askopenfilename()
        quality = int(quailty_entry.get())
        format = str(format_entry.get())
        if input_path:
            output_path = filedialog.asksaveasfilename(defaultextension="." + format)
            if output_path:
                image = Image.open(input_path)
                # 如果图像是 RGBA 模式，将其转换为 RGB 并处理透明度
                if image.mode == 'RGBA':
                    # 创建一个白色背景的图像
                    background = Image.new('RGB', image.size, (255, 255, 255))
                    # 将原始图像粘贴到背景上，忽略透明度
                    background.paste(image, mask=image.split()[3])
                    resized_image = background.resize((width, height))
                else:
                    resized_image = image.resize((width, height))
                if format == 'jpg':
                    resized_image = resized_image.convert('RGB')
                resized_image.save(output_path, quality=quality)
                messagebox.showinfo("完成", "图片已成功调整大小并保存。")
            else:
                messagebox.showwarning("保存取消", "未选择保存路径。")
        else:
            messagebox.showwarning("打开取消", "未选择图片文件。")
    except ValueError:
        messagebox.showerror("错误", "请检查参数。")

# Create the main window
root = tk.Tk()
root.title("图片大小调整")

# 设置窗口大小
root.geometry("300x250")

# Create input fields for width and height
width_label = tk.Label(root, text="宽度 (像素):")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="高度 (像素):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

quailty_label = tk.Label(root, text="质量 (1-95) 质量越低 内存越小:")
quailty_label.pack()
quailty_entry = tk.Entry(root)
quailty_entry.pack()

format_label = tk.Label(root, text="格式 (jpg/png):")
format_label.pack()
format_entry = tk.Entry(root)
format_entry.pack()

# Create a button to resize the image
resize_button = tk.Button(root, text="调整图片大小", command=resize_image)
resize_button.pack()

# Run the main loop
root.mainloop()
