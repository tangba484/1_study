import os

folder_path = r"C:\Users\tangb\Study\hi"  # 폴더 경로를 적절히 수정해주세요
file_names = os.listdir(folder_path)

for file_name in file_names:
    if file_name.startswith("beakjoon_") and file_name.endswith(".py"):
        number_part = file_name.replace("beakjoon_", "").replace(".py", "")
        if number_part.isdigit():
            new_file_name = os.path.join(folder_path, file_name)
            new_number_part = os.path.join(folder_path, number_part + ".py")
            os.rename(new_file_name, new_number_part)
