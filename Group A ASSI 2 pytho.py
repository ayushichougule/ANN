def mcculloch_pitts_andnot(x1, x2):
    # Define weights and threshold
    w1 = 1
    w2 = -1
    theta = (2*1)-1 #nw-p

    # Calculate the weighted sum
    yin = x1 * w1 + x2 * w2

    # Activation function
    if yin >= theta:
        return 1
    else:
        return 0

# Input values
x1_values = [0, 0, 1, 1]
x2_values = [0, 1, 0, 1]

# Compute ANDNOT function
output_values = [mcculloch_pitts_andnot(x1, x2) for x1, x2 in zip(x1_values, x2_values)]

# Display the output
print("ANDNOT function output:", output_values)
