


from flask import Flask, request, jsonify
import cv2  # You might need to install OpenCV for image processing
# from .expp import predict_digit  # Import your digit prediction function

app = Flask(__name__)


# Route for digit comparison



@app.route('/compare_digits', methods=['POST'])
def compare_digits():
    # Get the uploaded image files
    image1 = request.files['image1']
    image2 = request.files['image2']

    if not image1 or not image2:
        return jsonify({'message': 'Both images are required'}), 400

    # Process the images if needed (resize, format conversion, etc.)
    # Example: convert to grayscale and resize to 28x28
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, (28, 28))
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.resize(img2, (28, 28))

    # Predict digits for both images
    digit1 = predict_digit(img1)  # Replace with your digit prediction function
    digit2 = predict_digit(img2)  # Replace with your digit prediction function

    # Compare the predicted digits and return the result
    result = digit1 == digit2

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
