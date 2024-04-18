import joblib
import warnings
warnings.filterwarnings('ignore')

def predict_class(input_fields, model_type = 'LogR'):
    # Define the model paths based on the model_type argument
    if model_type == 'LogR':
        model_path = './models/LogisticRegression_model.pkl'
    elif model_type == 'DT':
        model_path = './models/DecisionTree_model.pkl'
    elif model_type == 'MLP':
        model_path = './models/NeuralNetwork_model.pkl'
    else:
        raise ValueError('Invalid model_type argument')
    
    # import class and color encoders
    class_encoder = joblib.load('./models/LabEnc_class.pkl')
    color_encoder = joblib.load('./models/LabEnc_color.pkl')
    
    # Encode the color input
    input_fields[-1] = color_encoder.transform([input_fields[-1]])[0]

    # Load the trained model from the model path
    model = joblib.load(model_path)

    # Predict the class of the input using the model    
    prediction = model.predict([input_fields])
    
    # Decode the predicted class
    prediction = class_encoder.inverse_transform(prediction)[0]

    # Return the prediction results
    return prediction