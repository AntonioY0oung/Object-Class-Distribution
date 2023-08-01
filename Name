import os
import json
import matplotlib.pyplot as plt

def count_obj_in_json(json_data, labels):
    objects = [0] * len(labels)  
    if "shapes" in json_data:
        for shape in json_data["shapes"]:
            for i, label in enumerate(labels):
                if shape["label"] == label:
                    objects[i] += 1
    return objects

def readFile(folder_path, objects, labels):
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(".json"):
                filepath = os.path.join(root, filename)
                with open(filepath, "r") as json_file:
                    try:
                        data = json.load(json_file)
                        obj_counts = count_obj_in_json(data, labels)
                        for i in range(len(objects)):
                            objects[i] += obj_counts[i]
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in file {filename}: {e}")
    return objects

def showPlt(objects, labels):    
    plt.bar(labels, objects, color='pink', label='Data Points')
    plt.xlabel('Object Labels')
    plt.title('total')
    for i, count in enumerate(objects):
        plt.text(i, count, str(count), ha='center', va='bottom', fontweight='bold', fontsize=10, color='black')
    plt.xticks(rotation=45, ha='right') 
    plt.grid(True)
    print("File name")
    output_filename = input()
    print("File path to save")
    file_path = input()
    fig_path = os.path.join(file_path, output_filename)
    plt.savefig(fig_path)
    plt.show()
    return

def main():
    print('File path to read')
    folder_path = input()
    labels = ["person", "bicycle", "car", "motorbike", "bus", "truck", "traffic light", "traffic cone", "traffic sign"] 
    objects = [0,0,0,0,0,0,0,0,0]
    objects = readFile(folder_path, objects, labels)
    showPlt(objects, labels)
if __name__ == "__main__":
    main()
