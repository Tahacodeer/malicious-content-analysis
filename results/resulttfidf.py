
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from models.tfidf_predict import predict_email

email = """
taha your account has been attacked 
"""

result = predict_email(email)

print(result)