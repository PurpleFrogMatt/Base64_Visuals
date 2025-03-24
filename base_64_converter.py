import os
import base64
import pandas as pd

# function to convert an image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # read and encode the image file in Base64
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string

# create dataframe to store base64 text
df = pd.DataFrame(columns=["Name", "Base64"])

# specify directory containing pictures to convert
directory = "images"
# iterate through the image files in the directory and save their base64 to a dataframe
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        print(f"Processing file: {file_path}")
        df.loc[len(df)] = [filename.split(".")[0], f"data:image/{filename.split(".")[1]};base64," + image_to_base64(file_path)]

# copy the result to the clipboard ready for pasting into Power BI
df.to_clipboard("report_images_base64.txt", index=False)




