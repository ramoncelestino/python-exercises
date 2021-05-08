from sklearn.metrics import mean_squared_error

def mse_roi(file):
    # Using readlines()
    file1 = open(file, 'r')
    lines = file1.readlines()

    output = open("roi_output.txt", "a")

    for line in lines:
        attributes = line.split(";")
        input = "Image: " + attributes[0] + ", x_automatico: " + attributes[1] + ", y_automatico: " + attributes[2] + ", x_manual: " + attributes[3] + ", y_manual: " + attributes[4] + ", Mse: "
        print(input)
        current_image = attributes[0]
        x_automatic   = attributes[1]
        y_automatic   = attributes[2]
        x_manual      = attributes[3]
        y_manual      = attributes[4]

        center_automatic = [int(x_automatic), int(y_automatic)]
        center_manual    = [int(x_manual), int(y_manual)]

        #mse  = mean_squared_error(center_automatic, center_manual)
        mse = calculate_mse(center_automatic, center_manual)
        output.write(input + str(mse) + "\n")

    file1.close()
    output.close()

    return 1

def calculate_mse(center_automatic, center_manual):
    diff_x = abs(center_automatic[0] - center_manual[0])
    diff_y = abs(center_automatic[1] - center_manual[1])

    square_diffs = [diff_x * diff_x, diff_y * diff_y]

    mean_squares = (square_diffs[0] + square_diffs[1]) / 2

    return mean_squares





path = "roi.txt"
print(mse_roi(path))
