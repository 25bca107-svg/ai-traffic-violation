from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)  # Enables communication between index.html and Flask

@app.route('/api/analyze', methods=['POST'])
def analyze_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400
    
    file = request.files['video']
    file_path = f"uploaded_{file.filename}"
    file.save(file_path)

    # Process video with OpenCV
    cap = cv2.VideoCapture(file_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    # Simulated response with detected violations
    return jsonify({
        'status': 'success',
        'filename': file.filename,
        'total_frames': total_frames,
        'fps': fps,
        'violations_detected': 1,
        'details': [
            {
                'type': 'Red-Light Violation',
                'confidence': '98%',
                'timestamp': '00:04',
                'vehicle_type': 'Sedan'
            }
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)