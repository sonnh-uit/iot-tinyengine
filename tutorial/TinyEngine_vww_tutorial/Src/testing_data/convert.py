from PIL import Image
import numpy as np

def resize_and_convert_to_matrix(image_path, new_size=(80, 80)):
    # Mở ảnh bằng Pillow
    original_image = Image.open(image_path)
    
    # Resize ảnh
    resized_image = original_image.resize(new_size)
    
    # Chuyển đổi ảnh thành mảng NumPy
    image_array = np.array(resized_image.convert('RGB'))
    
    # Hiển thị thông tin về mảng ảnh
    print("Shape của mảng ảnh:", image_array.shape)
    #print("Mảng ảnh ban đầu:")
    #print(image_array)
    negative_image_array = (image_array - 128).astype(np.int8)
    negative_image_array=negative_image_array.flatten()
    np.savetxt("image_array.txt", negative_image_array,  fmt="%d", delimiter=",", newline=",")
    # Trả về mảng ảnh
    return negative_image_array

# Thay đổi đường dẫn của ảnh cần xử lý
image_path = "mountain.png"
# Gọi hàm để thực hiện chuyển đổi
result_matrix = resize_and_convert_to_matrix(image_path)

