# if i == 0 and j == 0:
#     for k in range(0,2):
#         for l in range(0,2):
#             if (clearField[k][l] == "M") and (clearField[i][j] != "M"):
#                 clearField[i][j] += 1
# #top right, mix
# if i == 3 and j == 0:
#     for k in range(-1,1):
#         for l in range(0,2):
#             if (clearField[i + k][j + l] == "M") and (clearField[i][j] != "M"):
#                 clearField[i][j] += 1

# #bottom left, mix
# if i == 0 and j == 3:
#     for k in range(0,2):
#         for l in range(-1,1):
#             if (clearField[i + k][j + l] == "M") and (clearField[i][j] != "M"):
#                 clearField[i][j] += 1

# #bottom right, mix
# if i == 3 and j == 3:
#     for k in range(-1,1):
#         for l in range(-1,1):
#             if (clearField[i + k][j + l] == "M") and (clearField[i][j] != "M"):
#                 clearField[i][j] += 1