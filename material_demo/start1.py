import os
file_path = r"C:\Users\imagine\Documents\test.blend"
python_file_path = r"C:\demo_code\AddonDataObject.py"

blender_path = r"C:\Program Files\Blender Foundation\Blender 3.6"
os.chdir(blender_path)

os.system(f"blender {file_path} --background --python {python_file_path}")