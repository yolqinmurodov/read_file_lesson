# #Rread file and convert to list
# def read_file(filename: str) -> list[int]:
#     """
#     Reads a file and returns a list of integers.

#     Args:
#         filename (str): The name of the file to read.
#     Returns:
#         data (list): A list of integers from the file.
#     """
#     # Open the file
#     # Read the file
    
#     return 0 

# #Print list from file






def read_file():
    f = open("data.txt", "r")
    data = f.read()
    list1 = data.split(",")
    return list1
print(read_file())
    