from predictions import app
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_predict(client):
    test_data = {
        "Gender": "Female",
        "Married": "No",
        "ApplicantIncome": 5000000,
        "LoanAmount": 5000,
        "Credit_History": 1.0
    }
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": 'Rejected'}

